"""
easy_date_formatter is meant to simplify getting formatted dates.
built on top of the datetime module.
"""


from datetime import datetime, timedelta


def _get_past_date(num_days_ago: int):
    """Calculate and return past date"""
    return datetime.now() - timedelta(days=num_days_ago)


def get_pretty_date():
    """
    Returns the current date in a human-friendly format.

    Returns:
        str: Current date formatted as 'Weekday, Month Day, Year'
             (e.g., 'Monday, July 20, 2026').
    """
    return datetime.now().strftime("%A, %B %d, %Y")


def dd_mm_yyyy():
    """
    Returns the current date using hyphen separators.

    Returns:
        str: Current date in 'DD-MM-YYYY' format (e.g., '20-07-2026').
    """
    return datetime.now().strftime("%d-%m-%Y")


def mm_dd_yyyy():
    """
    Returns the current date using hyphen separators.

    Returns:
        str: Current date in 'MM-DD-YYYY' format (e.g., '07-20-2026').
    """
    return datetime.now().strftime("%m-%d-%Y")


def slash_dd_mm_yyyy():
    """
    Returns the current date using slash separators.

    Returns:
        str: Current date in 'DD/MM/YYYY' format (e.g., '20/07/2026').
    """
    return datetime.now().strftime("%d/%m/%Y")


def slash_mm_dd_yyyy():
    """
    Returns the current date using slash separators.

    Returns:
        str: Current date in 'MM/DD/YYYY' format (e.g., '07/20/2026').
    """
    return datetime.now().strftime("%m/%d/%Y")


def get_past_pretty_date(num_days_ago: int):
    """
    Calculates a date from the past and returns it in a pretty format.

    Args:
        num_days_ago (int): The number of days to subtract from today.

    Returns:
        str: Past date formatted as 'Weekday, Month Day, Year'
             (e.g., 'Friday, July 17, 2026').
    """
    past_date = _get_past_date(num_days_ago)
    return past_date.strftime("%A, %B %d, %Y")


def past_dd_mm_yyyy(num_days_ago: int):
    """
    Calculates a past date and returns it with hyphen separators.

    Args:
        num_days_ago (int): The number of days to subtract from today.

    Returns:
        str: Past date in 'DD-MM-YYYY' format (e.g., '17-07-2026').
    """
    past_date = _get_past_date(num_days_ago)
    return past_date.strftime("%d-%m-%Y")


def past_mm_dd_yyyy(num_days_ago: int):
    """
    Calculates a past date and returns it with hyphen separators.

    Args:
        num_days_ago (int): The number of days to subtract from today.

    Returns:
        str: Past date in 'MM-DD-YYYY' format (e.g., '07-17-2026').
    """
    past_date = _get_past_date(num_days_ago)
    return past_date.strftime("%m-%d-%Y")


def past_slash_dd_mm_yyyy(num_days_ago: int):
    """
    Calculates a past date and returns it with slash separators.

    Args:
        num_days_ago (int): The number of days to subtract from today.

    Returns:
        str: Past date in 'DD/MM/YYYY' format (e.g., '17/07/2026').
    """
    past_date = _get_past_date(num_days_ago)
    return past_date.strftime("%d/%m/%Y")


def past_slash_mm_dd_yyyy(num_days_ago: int):
    """
    Calculates a past date and returns it with slash separators.

    Args:
        num_days_ago (int): The number of days to subtract from today.

    Returns:
        str: Past date in 'MM/DD/YYYY' format (e.g., '07/17/2026').
    """
    past_date = _get_past_date(num_days_ago)
    return past_date.strftime("%m/%d/%Y")
