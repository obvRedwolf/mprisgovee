import sys
import tomllib

from pathlib import Path

CONFIG_DIR = Path.home() / ".config" / "mprisgovee"
CONFIG_FILE = CONFIG_DIR / "config.toml"

DEFAULT_CONFIG_TOML = """
# ip address of your govee devices
# you can find this by going to your device's settings page, getting the mac, and matching it up with a device ip on your network
# format this as a list
# ex: ["192.168.1.100", "192.168.1.101", "192.168.1. ..."]
govee_ip = ["192.168.1.100", "192.168.1.101"]

# lan port of your govee device
# you can usually leave this default
govee_port = 4003

# change brightness on play/pause
brightness_on_play_pause = true

# brightness level when playing
brightness_playing = 100

# brightness level when paused
brightness_paused = 10

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
