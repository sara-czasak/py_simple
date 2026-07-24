from datetime import timedelta


def seconds_to_hh_mm_ss(seconds: int):
    """
    Returns seconds in HH:MM:SS format.

    Arguments:
        seconds (int) -- number of seconds to convert

    Example:
        seconds_to_hh_mm_ss(90)
        (00:01:30)
    """
    return str(timedelta(seconds=seconds))


def km_to_mile(km: float):
    """
    Converts kilometers to miles. Returns miles as a float.

    Arguments:
        km (float) -- kilometers

    Example:
        km_to_mile(100)
        (62.13)
    """
    return float(f"{km * 0.621371:.2f}")


def miles_to_km(miles: float):
    """
        Converts miles to kilometers. Returns kilometers as a float.

        Arguments:
            miles (float) -- miles

        Example:
            miles_to_km(100)
            (160.93)
    """
    return float(f"{miles * 1.60934:.2f}")


