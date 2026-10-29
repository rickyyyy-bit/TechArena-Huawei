"""Regression checks for the development-only export boundary."""

from pathlib import Path
import shutil
import zipfile

import pytest

from scripts.submission import create_package, inspect_solution


@pytest.fixture
def project(tmp_path: Path) -> Path:
    """Use the official fixture, not a real competition recording."""
    source = Path(__file__).parent / "fixtures/solution"
    shutil.copytree(source, tmp_path / "solution")
    # Minimal container-like bytes test plumbing only; this is NOT a real video.
    (tmp_path / "solution/presentation.mp4").write_bytes(b"\x00\x00\x00\x18ftypmp42fixture-only")
    return tmp_path


def test_missing_video_allows_development_but_refuses_final_package(project: Path) -> None:
    (project / "solution/presentation.mp4").unlink()
    assert inspect_solution(project)
    with pytest.raises(ValueError, match="presentation.mp4"):
        create_package(project)
    assert not (project / "dist/solution.zip").exists()


def test_package_exports_only_solution_and_retains_content(project: Path) -> None:
    (project / ".env").write_text("API_KEY=private-unit-test-value\n", encoding="utf-8")
    archive = create_package(project)
    with zipfile.ZipFile(archive) as package:
        assert {name.split("/")[0] for name in package.namelist()} == {"solution"}
        assert all(not name.endswith(".env") for name in package.namelist())
        assert package.read("solution/manifest.json") == (project / "solution/manifest.json").read_bytes()


def test_actual_local_key_in_submission_is_rejected(project: Path) -> None:
    local_key = "private-unit-test-value"
    (project / ".env").write_text(f"API_KEY={local_key}\n", encoding="utf-8")
    with (project / "solution/README.md").open("a", encoding="utf-8") as handle:
        handle.write(local_key)
    with pytest.raises(ValueError, match="Credential-like"):
        create_package(project)


def test_unknown_files_are_rejected_instead_of_silently_exported(project: Path) -> None:
    (project / "solution/credentials.txt").write_text("not for export", encoding="utf-8")
    with pytest.raises(ValueError, match="Unexpected submission file"):
        create_package(project)


def test_empty_or_non_mp4_recording_is_rejected(project: Path) -> None:
    video = project / "solution/presentation.mp4"
    video.write_bytes(b"")
    with pytest.raises(ValueError, match="Empty submission file"):
        create_package(project)
    video.write_bytes(b"not a media container")
    with pytest.raises(ValueError, match="MP4 container marker"):
        create_package(project)


def test_token_pattern_is_rejected_without_local_environment_file(project: Path) -> None:
    synthetic_token = "sk-" + "x" * 32
    with (project / "solution/README.md").open("a", encoding="utf-8") as handle:
        handle.write(synthetic_token)
    with pytest.raises(ValueError, match="Credential-like"):
        create_package(project)
