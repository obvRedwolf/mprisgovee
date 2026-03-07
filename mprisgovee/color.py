import requests
import subprocess

from io import BytesIO
from colorthief import ColorThief
from colorsys import rgb_to_hsv


def get_color(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        img_bytes = BytesIO(response.content)

        ct = ColorThief(img_bytes)
        palette = ct.get_palette(color_count=8, quality=1)

        best_color = palette[0]
        best_score = -1

        for r, g, b in palette:
            h, s, v = rgb_to_hsv(r / 255, g / 255, b / 255)

            if v > 0.95 or v < 0.15:
                continue

            score = s * (1 - abs(0.5 - v) * 2)

            if score > best_score:
                best_score = score
                best_color = (r, g, b)

        return best_color

    except Exception as e:
        print("error extracting color:", e)

        try:
            subprocess.run(
                [
                    "notify-send",
                    "-u",
                    "critical",
                    "mprisgovee: error extracting color:",
                    str(e),
                ]
            )
        except Exception as e:
            print("error sending notification:", e)

        # make it obvious that something went wrong
        return (255, 0, 255)
