from pathlib import Path

PROJECT_NAME = 'pytest'


class RootPath:

    _absolute_path = None

    @classmethod
    def get_absolute_path(cls) -> Path:
        if cls._absolute_path is None:
            cls._absolute_path = cls._get_calling_dir()
        return cls._absolute_path

    @classmethod
    def _get_calling_dir(cls) -> Path:
        walk_path = Path('.').resolve()
        while True:
            parent_dir = walk_path.parent
            if str(parent_dir).endswith(PROJECT_NAME):
                return parent_dir.resolve()
            else:
                walk_path = walk_path.parent


def get_absolute_path(path: str) -> Path:

    if path.startswith('~'):
        return Path(path).expanduser().resolve()
    elif path.startswith('/'):
        return Path(str(RootPath.get_absolute_path()) + path).resolve()
    else:
        raise ValueError(f'Unrecognised path pattern: {path}')


if __name__ == '__main__':
    # internal tests
    import os
    assert PROJECT_NAME in str(RootPath.get_absolute_path())
    assert os.getenv('USERPROFILE') == str(get_absolute_path('~'))
