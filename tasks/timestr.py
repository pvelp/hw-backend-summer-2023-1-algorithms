__all__ = (
    'seconds_to_str',
)


def seconds_to_str(seconds: int) -> str:
    """
    Функция должна вернуть текстовое представление времени
    20 -> 20s
    60 -> 01m00s
    65 -> 01m05s
    3700 -> 01h01m40s
    93600 -> 01d02h00m00s
    """
    days = int((seconds / 3600) / 24)
    hours = int((seconds / 3600)) - (24 * days)
    minutes = int((seconds / 60)) - (24 * days * 60) - (hours * 60)
    seconds -= (hours * 3600) + (minutes * 60) + (days * 24 * 3600)
    seconds_str = f"0{seconds}s" if seconds < 10 else f"{seconds}s"
    hours_str = f"0{hours}h" if hours < 10 else f"{hours}h"
    minutes_str = f"0{minutes}m" if minutes < 10 else f"{minutes}m"
    days_str = f"0{days}d" if days < 10 else f"{days}d"

    if days == 0 and hours == 0 and minutes == 0:
        result = seconds_str
    elif days == 0 and hours == 0:
        result = minutes_str + seconds_str
    elif days == 0:
        result = hours_str + minutes_str + seconds_str
    else:
        result = days_str + hours_str + minutes_str + seconds_str
    return result

