# mprisgovee
light anything up with govee, right from mpris.


[![OS - Linux](https://img.shields.io/badge/OS-Linux-blue?logo=linux&logoColor=white)](https://www.linux.org/ "Go to Linux homepage")
[![Made with Python](https://img.shields.io/badge/Python->=3.18-blue?logo=python&logoColor=white)](https://python.org "Go to Python homepage")
[![PyPI](https://img.shields.io/pypi/v/mprisgovee?label=pypi%20package)](https://aur.archlinux.org/packages/python-mprisgovee "Go to AUR package")
[![AUR](https://img.shields.io/aur/version/python-mprisgovee)](https://pypi.org/project/mprisgovee/ "Go to PyPI package")
[![License](https://img.shields.io/badge/License-MIT-blue)](#license)
[![contributions - welcome](https://img.shields.io/badge/contributions-welcome-blue)](/CONTRIBUTING.md "Go to contributions doc")

## showcase
<img src="https://raw.githubusercontent.com/obvRedwolf/mprisgovee/main/img/showcase.gif" width="600">

## features
- **detect song art** from **any mpris player** automatically
- change **govee** device **color** with dominant color from **song art**
    - uses the **lan api** for extremely **fast** updates
- **cache** colors to avoid reprocessing
- app **ignoring**
- **configurable** settings

## prerequisites
- a computer running **linux**
- a **network** connection
- a **govee lan api** capable device
    - remember to turn on the capability!
        - you can find this in the app by going to your device's settings page.
- **python** 3.9 or higher
- **[playerctl](https://github.com/altdesktop/playerctl)** installed
- your govee device's **ip address**:
    1. get the **mac address** of your device.
        - you can find this in the app by going to your device's settings page.
    2. use any method to match up the **mac address** with a **device ip** on your network.
        - i did this by going to my router settings and matching it up under "Device List".

## installation
### pip
`mprisgovee` is avaliable on **PyPI**:
```
pip install mprisgovee
```
### Arch (AUR)
`mprisgovee` is avaliable on the **AUR** for **Arch** users under `python-mprisgovee`:
```
# for yay users
yay -S python-mprisgovee

# for paru users
paru -S python-mprisgovee
```

## usage
you can start it by either manually running `mprisgovee` from your terminal or running at startup using your favorite method.

### example (niri):
```
spawn-sh-at-startup "mprisgovee"
```

## configuration
the config file can usually be found at `~/.config/mprisgovee/config.toml`.

### default configuration
```toml
govee_ip = "192.168.1.100"

govee_port = 4003

ignored_apps = [
    "firefox",
    "chromium",
    "chrome",
    "brave",
    "vivaldi",
    "zen",
    "opera"
```
- **govee_ip**:
    - sets the current **ip address**.
- **govee_port**:
    - sets the current **port**.
        - this can usually be left **default**.
- **ignored_apps**:
    - **ignores** all apps on list.

## thanks to:
- **[Dynamic Lights Home Assistant](https://github.com/muckelba/dynamic-lights-homeassistant/)** - original inspiration
- **[Govee Dynamic Lights](https://github.com/obvRedwolf/govee-dynamic-lights)** - my spicetify extension which took inspiration from the above
