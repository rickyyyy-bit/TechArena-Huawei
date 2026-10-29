"""Development-only checks and ZIP packaging; never part of the submitted Skills."""

from __future__ import annotations

import argparse
import hashlib
from importlib.metadata import version
import os
from pathlib import Path
import re
import sys
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from career_sim_runner.report import format_validation_report  # noqa: E402
from career_sim_runner.validate import validate_submission  # noqa: E402

KEY_PATTERN = re.compile(rb"\bsk-(?:or-v1-)?[A-Za-z0-9_-]{20,}\b")
ENV_KEYS = {"API_BASE", "API_KEY", "MODEL_NAME"}


def read_local_values(root: Path, *, strict: bool = False) -> dict[str, str]:
    """Read only the local environment file; never print its values."""
    path = root / ".env"
    if not path.is_file():
        if strict:
            raise ValueError("Missing .env: copy .env.example and save the organiser values locally.")
        return {}
    values: dict[str, str] = {}
    for number, raw in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        name, separator, value = line.partition("=")
        name = name.strip()
        if strict and (not separator or name not in ENV_KEYS or name in values):
            raise ValueError(f"Invalid or duplicate .env assignment on line {number}; only three organiser keys allowed.")
        if separator and name in ENV_KEYS:
            values[name] = value.strip().strip('"').strip("'")
    if strict:
        if set(values) != ENV_KEYS or not all(values.values()):
            raise ValueError("Save all three nonempty organiser values in .env; no values are printed.")
        if values["API_BASE"] != "https://openrouter.ai/api/v1" or values["MODEL_NAME"] != "deepseek-v4-flash":
            raise ValueError("API_BASE or MODEL_NAME differs from this team's organiser email.")
    return values


def check_credentials_in_file(path: Path, root: Path, key: bytes) -> None:
    """Check streams without echoing a credential or loading a whole MP4."""
    overlap = max(256, len(key))
    previous = b""
    with path.open("rb") as handle:
        while chunk := handle.read(1024 * 1024):
            data = previous + chunk
            if (key and key in data) or KEY_PATTERN.search(data):
                raise ValueError(f"Credential-like content detected in {path.relative_to(root)}; export refused.")
            previous = data[-overlap:]


def inspect_solution(root: Path, *, final: bool = False) -> list[Path]:
    """Validate the actual prose-only solution without starting a model or service."""
    solution = root / "solution"
    if solution.is_symlink() or not solution.is_dir():
        raise ValueError("solution must be a real directory, not a symbolic link.")
    entries = sorted(solution.rglob("*"))
    if any(path.is_symlink() for path in entries):
        raise ValueError("Symbolic links are not allowed in this submission export.")
    files = [path for path in entries if path.is_file()]
    allowed = {"manifest.json", "README.md", "presentation.mp4", "design/skills_design.md", "design/decision_report.md"}
    for path in files:
        relative = path.relative_to(solution)
        skill_file = len(relative.parts) == 3 and relative.parts[0] == "skills" and relative.name == "SKILL.md"
        if relative.as_posix() not in allowed and not skill_file:
            raise ValueError(f"Unexpected submission file: {relative}. Review the export policy before adding support files.")
        if path.stat().st_size == 0:
            raise ValueError(f"Empty submission file: {relative}")
    key = read_local_values(root).get("API_KEY", "").encode()
    for path in files:
        check_credentials_in_file(path, solution, key)
    report = validate_submission(solution, require_presentation=final)
    if not report.ok:
        raise ValueError(format_validation_report(report))
    if final:
        with (solution / "presentation.mp4").open("rb") as video:
            if b"ftyp" not in video.read(64):
                raise ValueError("presentation.mp4 lacks an MP4 container marker. Supply the actual team recording.")
    return files


def digest(path: Path) -> str:
    """Hash a file without loading a whole video into memory."""
    with path.open("rb") as handle:
        return hashlib.file_digest(handle, "sha256").hexdigest()


def create_package(root: Path) -> Path:
    """Make and verify one solution-root ZIP after final structural checks pass."""
    files = inspect_solution(root, final=True)
    destination = root / "dist"
    if destination.is_symlink():
        raise ValueError("dist must not be a symbolic link.")
    destination.mkdir(exist_ok=True)
    destination = destination.resolve()
    archive = destination / "solution.zip"
    if archive.is_symlink():
        raise ValueError("Output ZIP must not be a symbolic link.")
    with tempfile.TemporaryDirectory(prefix=".verify-", dir=destination) as temporary:
        temporary_path = Path(temporary).resolve()
        if not temporary_path.is_relative_to(destination):
            raise ValueError("Verification directory escaped dist.")
        pending = temporary_path / "solution.zip"
        expected = {path.relative_to(root).as_posix(): digest(path) for path in files}
        with zipfile.ZipFile(pending, "w", compression=zipfile.ZIP_DEFLATED) as package:
            for path in files:
                package.write(path, path.relative_to(root).as_posix())
        extracted = temporary_path / "extracted"
        with zipfile.ZipFile(pending) as package:
            if set(package.namelist()) != set(expected):
                raise ValueError("ZIP contents differ from the approved files.")
            package.extractall(extracted)
        if {path.name for path in extracted.iterdir()} != {"solution"}:
            raise ValueError("ZIP does not have exactly one solution/ root.")
        if any(digest(extracted / name) != value for name, value in expected.items()):
            raise ValueError("Extracted content differs from the source.")
        if not validate_submission(extracted / "solution").ok:
            raise ValueError("Extracted submission failed official structural validation.")
        os.replace(pending, archive)
    return archive


def main() -> int:
    """Run checks or package without any model requests."""
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    check = commands.add_parser("check", help="Key-free development check; video optional")
    check.add_argument("--final", action="store_true", help="Require the actual nonempty MP4")
    check.add_argument("--credentials", action="store_true", help="Check three local values without printing them")
    commands.add_parser("package", help="Require final structure and produce verified dist/solution.zip")
    args = parser.parse_args()
    try:
        if version("jiuwenswarm") != "0.2.4b3":
            raise ValueError("JiuwenSwarm must be exactly 0.2.4b3; run uv sync --locked --python 3.12.")
        if args.command == "package":
            print(f"Verified ZIP: {create_package(ROOT)}")
            print("Manually confirm the real English recording, original speed and duration <= 10 minutes before upload.")
        else:
            if args.credentials:
                read_local_values(ROOT, strict=True)
                print("Local organiser settings checked; values were not displayed.")
            files = inspect_solution(ROOT, final=args.final)
            print(f"PASS: {'final structural' if args.final else 'development'} check; {len(files)} submission files.")
            if not args.final and not (ROOT / "solution/presentation.mp4").is_file():
                print("FINAL SUBMISSION BLOCKED: real presentation.mp4 is missing. Gameplay is allowed without it.")
            print("No model call was made. Structural checks do not certify competition compliance or agent quality.")
        return 0
    except (ValueError, OSError, zipfile.BadZipFile) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
