"""
easy_date_formatter is meant to simplify getting formatted dates.
Built on top of the datetime module — no more memorizing strftime codes.
"""

from datetime import datetime, timedelta


# ── Format registry (strftime pattern → readable name) ──────────────
_FORMATS = {
    "pretty": "%A, %B %d, %Y",
    "dd-mm-yyyy": "%d-%m-%Y",
    "mm-dd-yyyy": "%m-%d-%Y",
    "dd/mm/yyyy": "%d/%m/%Y",
    "mm/dd/yyyy": "%m/%d/%Y",
}


def list_available_formats():
    """Return the supported format names for reference."""
    return list(_FORMATS.keys())


def _format_date(date_obj, fmt_key: str) -> str:
    """Apply a named format to a datetime object."""
    return date_obj.strftime(_FORMATS[fmt_key])


def _get_past_date(num_days_ago: int):
    """Calculate and return a past date."""
    return datetime.now() - timedelta(days=num_days_ago)


def _get_future_date(num_days_from_now: int):
    """Calculate and return a future date."""
    return datetime.now() + timedelta(days=num_days_from_now)


# ── Pretty dates ────────────────────────────────────────────────────

def get_pretty_date():
    """
    Returns the current date in a human-friendly format.

    Returns:
        str: Current date formatted as 'Weekday, Month Day, Year'
             (e.g., 'Monday, July 20, 2026').
    """
    return _format_date(datetime.now(), "pretty")


def get_past_pretty_date(num_days_ago: int):
    """
    Calculates a date from the past in pretty format.

    Args:
        num_days_ago (int): Number of days to subtract from today.

    Returns:
        str: Past date as 'Weekday, Month Day, Year'.
    """
    return _format_date(_get_past_date(num_days_ago), "pretty")


def get_future_pretty_date(num_days_from_now: int):
    """
    Calculates a future date in pretty format.

    Args:
        num_days_from_now (int): Number of days to add to today.

    Returns:
        str: Future date as 'Weekday, Month Day, Year'.
    """
    return _format_date(_get_future_date(num_days_from_now), "pretty")


# ── Hyphenated formats (DD-MM-YYYY or MM-DD-YYYY) ───────────────────

def dd_mm_yyyy():
    """Current date in 'DD-MM-YYYY' format (e.g., '20-07-2026')."""
    return _format_date(datetime.now(), "dd-mm-yyyy")


def past_dd_mm_yyyy(num_days_ago: int):
    """Past date in 'DD-MM-YYYY' format."""
    return _format_date(_get_past_date(num_days_ago), "dd-mm-yyyy")


def future_dd_mm_yyyy(num_days_from_now: int):
    """Future date in 'DD-MM-YYYY' format."""
    return _format_date(_get_future_date(num_days_from_now), "dd-mm-yyyy")


def mm_dd_yyyy():
    """Current date in 'MM-DD-YYYY' format (e.g., '07-20-2026')."""
    return _format_date(datetime.now(), "mm-dd-yyyy")


def past_mm_dd_yyyy(num_days_ago: int):
    """Past date in 'MM-DD-YYYY' format."""
    return _format_date(_get_past_date(num_days_ago), "mm-dd-yyyy")


def future_mm_dd_yyyy(num_days_from_now: int):
    """Future date in 'MM-DD-YYYY' format."""
    return _format_date(_get_future_date(num_days_from_now), "mm-dd-yyyy")


# ── Slashed formats (DD/MM/YYYY or MM/DD/YYYY) ──────────────────────

def slash_dd_mm_yyyy():
    """Current date in 'DD/MM/YYYY' format (e.g., '20/07/2026')."""
    return _format_date(datetime.now(), "dd/mm/yyyy")


def past_slash_dd_mm_yyyy(num_days_ago: int):
    """Past date in 'DD/MM/YYYY' format."""
    return _format_date(_get_past_date(num_days_ago), "dd/mm/yyyy")


def future_slash_dd_mm_yyyy(num_days_from_now: int):
    """Future date in 'DD/MM/YYYY' format."""
    return _format_date(_get_future_date(num_days_from_now), "dd/mm/yyyy")


def slash_mm_dd_yyyy():
    """Current date in 'MM/DD/YYYY' format (e.g., '07/20/2026')."""
    return _format_date(datetime.now(), "mm/dd/yyyy")


def past_slash_mm_dd_yyyy(num_days_ago: int):
    """Past date in 'MM/DD/YYYY' format."""
    return _format_date(_get_past_date(num_days_ago), "mm/dd/yyyy")


def future_slash_mm_dd_yyyy(num_days_from_now: int):
    """Future date in 'MM/DD/YYYY' format."""
    return _format_date(_get_future_date(num_days_from_now), "mm/dd/yyyy")
