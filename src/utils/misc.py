import math
from datetime import datetime


def hex_id_time_ms() -> str:
    """
    Generates a simple id based on the epoch time now in milliseconds.

    The '0x' hex identifier is omitted and the string is returned.
    """
    return hex(int(math.floor(datetime.now().timestamp() * 1000)))[2:]
