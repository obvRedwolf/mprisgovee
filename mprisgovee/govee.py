import socket
import json


def set_color(ip, port, r, g, b):
    msg = {
        "msg": {
            "cmd": "colorwc",
            "data": {"color": {"r": r, "g": g, "b": b}, "colorTemInKelvin": 0},
        }
    }

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(json.dumps(msg).encode(), (ip, port))
    sock.close()
