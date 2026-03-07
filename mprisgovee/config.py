import json

from pathlib import Path

CONFIG_DIR = Path.home() / ".config" / "mprisgovee"
CONFIG_FILE = CONFIG_DIR / "config.json"

DEFAULT_CONFIG = {
    "govee_ip": "192.168.1.100",
    "govee_port": 4003,
}


def load_config():
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)

    if not CONFIG_FILE.exists():
        with open(CONFIG_FILE, "w") as f:
            json.dump(DEFAULT_CONFIG, f, indent=4)
        print("running with first-launch default settings!")
        print(f'edit "{CONFIG_FILE}" to change settings!')
        return DEFAULT_CONFIG

    with open(CONFIG_FILE) as f:
        return json.load(f)
