import sys
import tomllib

from pathlib import Path

CONFIG_DIR = Path.home() / ".config" / "mprisgovee"
CONFIG_FILE = CONFIG_DIR / "config.toml"

DEFAULT_CONFIG_TOML = """
# ip address of your govee device
# you can find this by going to your device's settings page, getting the mac, and matching it up with a device ip on your network
govee_ip = "192.168.1.100"

# lan port of your govee device
# you can usually leave this default
govee_port = 4003

# apps to ignore ignore when looking for song art
# by default, common browsers are ignored
ignored_apps = [
    "firefox",
    "chromium",
    "chrome",
    "brave",
    "vivaldi",
    "zen",
    "opera"
]
"""


def load_config():
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)

    if not CONFIG_FILE.exists():
        with open(CONFIG_FILE, "w") as f:
            f.write(DEFAULT_CONFIG_TOML)
        print("running with first-launch default settings!")
        print(f'edit "{CONFIG_FILE}" to change settings!')

    try:
        with open(CONFIG_FILE, "rb") as f:
            return tomllib.load(f)
    except Exception as e:
        print(f"failed to load config: {e}")
        sys.exit(1)
