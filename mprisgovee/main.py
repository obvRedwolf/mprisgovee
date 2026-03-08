import asyncio

from .mpris import watch_metadata
from .color import get_color
from .govee import set_color, set_brightness
from .cache import load_cache, save_cache
from .config import load_config
from .environment import check_environment


config = load_config()
cache = load_cache()


async def handle_art(url, player, status):
    if player in config["ignored_apps"]:
        print(f"ignored {player}")
        return

    print("\n")

    if config["brightness_on_play_pause"]:
        if (status == "Paused") or (status == "Stopped"):
            set_brightness(
                config["govee_ip"], config["govee_port"], config["brightness_paused"]
            )
            print(f"set brightness {config['brightness_playing']} from paused {player}")
        elif status == "Playing":
            set_brightness(
                config["govee_ip"], config["govee_port"], config["brightness_playing"]
            )
            print(
                f"set brightness {config['brightness_playing']} from playing {player}"
            )

    if url in cache:
        print("cached color found")
        r, g, b = cache[url]

    else:
        r, g, b = get_color(url)
        cache[url] = [r, g, b]

        # only save cache if no error
        if not ((r, g, b) == (255, 0, 255)):
            save_cache(cache)

    set_color(config["govee_ip"], config["govee_port"], r, g, b)

    print(f"set color {r}, {g}, {b} from {player}")


def main():
    check_environment()
    print("mprisgovee running...")

    asyncio.run(watch_metadata(handle_art))
