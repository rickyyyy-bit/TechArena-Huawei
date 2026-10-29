"""Tests for participant submission installation."""

from pathlib import Path

import pytest

from career_sim_runner import install
from career_sim_runner.install import install_submission


def fixture_submission() -> Path:
    """Return the real sample submission path."""
    return Path(__file__).resolve().with_name("fixtures") / "solution"


def test_install_submission_generates_skill(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Installing a real submission should mirror only participant skills."""
    skills_dir = tmp_path / "skills"
    (tmp_path / "memory").mkdir()
    monkeypatch.setattr(install, "ensure_runtime_dirs", lambda: None)
    monkeypatch.setattr(install, "ensure_instance_initialized", lambda: tmp_path / "instance")
    monkeypatch.setattr(install, "jiuwenswarm_data_dir", lambda: tmp_path / "instance")
    monkeypatch.setattr(install, "jiuwenswarm_skills_state_path", lambda: skills_dir / "skills_state.json")
    monkeypatch.setattr(install, "active_install_path", lambda: tmp_path / "active_install.json")
    record = install_submission(fixture_submission(), skills_dir=skills_dir)

    assert Path(record.skill_dir) == skills_dir
    assert record.submission_name == "flash-tomato"
    assert record.manifest["submission_mode"] == "skill_bundle"
    assert sorted(record.manifest["participant_skill_names"]) == ["dummy-skill"]
    assert record.skill_name == "submission-skills"
    assert not (skills_dir / "career-emulator-player").exists()
    assert (skills_dir / "dummy-skill" / "SKILL.md").is_file()
    assert (skills_dir / "skills_state.json").is_file()
    assert (tmp_path / "active_install.json").is_file()
    assert (tmp_path / "instance/agent/workspace/IDENTITY.md").is_file()
