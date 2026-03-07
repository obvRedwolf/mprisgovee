import json
from pathlib import Path

CACHE_DIR = Path.home() / ".cache" / "mprisgovee"
CACHE_FILE = CACHE_DIR / "colors.json"


def load_cache():
    CACHE_DIR.mkdir(parents=True, exist_ok=True)

    if not CACHE_FILE.exists():
        print("no cache found, generating an empty one.")
        print(f'find this file in "{CACHE_FILE}".')
        return {}
    with open(CACHE_FILE) as f:
        return json.load(f)


def save_cache(cache):
    with open(CACHE_FILE, "w") as f:
        json.dump(cache, f, indent=4)
