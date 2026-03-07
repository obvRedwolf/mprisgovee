import platform
import shutil
import sys


def check_environment():
    errors = []

    print("checking environment...")

    if platform.system() != "Linux":
        errors.append("this program only works on linux, sorry!")

    if shutil.which("playerctl") is None:
        errors.append("playerctl is not installed.")

    if errors:
        print("\n".join(errors))
        sys.exit(1)
