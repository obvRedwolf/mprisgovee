import asyncio


async def watch_metadata(callback):
    proc = await asyncio.create_subprocess_exec(
        "playerctl",
        "metadata",
        "--follow",
        "mpris:artUrl",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.DEVNULL,
    )

    print("connected, listening for changes...")

    while True:
        line = await proc.stdout.readline()

        if not line:
            break

        url = line.decode().strip()

        if url:
            asyncio.create_task(callback(url))
