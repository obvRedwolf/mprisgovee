import asyncio


async def watch_metadata(callback):
    proc = await asyncio.create_subprocess_exec(
        "playerctl",
        "--follow",
        "--format",
        "{{playerName}}|{{mpris:artUrl}}|{{status}}",
        "metadata",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.DEVNULL,
    )

    print("connected, listening for changes...")

    while True:
        line = await proc.stdout.readline()
        if not line:
            break

        line = line.decode().strip()
        if not line:
            continue

        try:
            player, url, status = line.split("|", 2)
        except ValueError:
            continue

        asyncio.create_task(callback(url, player, status))
