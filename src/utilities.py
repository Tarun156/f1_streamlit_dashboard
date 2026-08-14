from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def ensure_directory_exists(directory: Path) -> Path:
	directory.mkdir(parents=True, exist_ok=True)
	return directory

