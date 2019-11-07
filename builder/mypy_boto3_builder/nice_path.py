from pathlib import Path
from dataclasses import dataclass


@dataclass
class NicePath:
    path: Path

    def __str__(self) -> str:
        path = self.path
        try:
            path = path.relative_to(Path.cwd())
        except ValueError:
            pass

        return path.as_posix()
