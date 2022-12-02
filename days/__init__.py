import glob
from pathlib import Path

glob_str = f'{Path(__file__).parent}/day*.py'
modules = [Path(fp) for fp in glob.glob(glob_str)]
banned = ["__init__.py", "__main__.py"]
__all__ = [f.name[:-3] for f in modules if f.is_file() and f.name not in banned]
