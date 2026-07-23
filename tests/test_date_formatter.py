"""Tests for easy_date_formatter module."""

import re
from datetime import datetime, timedelta
import pytest
from py_simple_package.src.py_simple.easy_date_formatter import (
    get_pretty_date,
    get_past_pretty_date,
    get_future_pretty_date,
    dd_mm_yyyy,
    past_dd_mm_yyyy,
    future_dd_mm_yyyy,
    mm_dd_yyyy,
    past_mm_dd_yyyy,
    future_mm_dd_yyyy,
    slash_dd_mm_yyyy,
    past_slash_dd_mm_yyyy,
    future_slash_dd_mm_yyyy,
    slash_mm_dd_yyyy,
    past_slash_mm_dd_yyyy,
    future_slash_mm_dd_yyyy,
    list_available_formats,
    _FORMATS,
)


class TestPrettyDates:
    """Tests for human-friendly pretty date formats."""

    def test_get_pretty_date_format(self):
        """Should return 'Weekday, Month Day, Year' format."""
        result = get_pretty_date()
        assert re.match(r'[A-Z][a-z]+, [A-Z][a-z]+ \d{1,2}, \d{4}', result)

    def test_get_past_pretty_date_returns_string(self):
        """Should return a string for valid input."""
        result = get_past_pretty_date(7)
        assert isinstance(result, str)
        assert re.match(r'[A-Z][a-z]+, [A-Z][a-z]+ \d{1,2}, \d{4}', result)

    def test_get_past_pretty_date_zero_days(self):
        """Zero days ago should equal today."""
        assert get_past_pretty_date(0) == get_pretty_date()

    def test_get_past_pretty_date_one_day(self):
        """Yesterday should be one day before today."""
        past = get_past_pretty_date(1)
        today = datetime.now()
        yesterday = today - timedelta(days=1)
        expected = yesterday.strftime("%A, %B %d, %Y")
        assert past == expected

    def test_get_future_pretty_date(self):
        """Future pretty date should exist and differ from today."""
        result = get_future_pretty_date(7)
        assert isinstance(result, str)
        assert result != get_pretty_date()

    def test_get_future_pretty_date_zero_days(self):
        """Zero days from now should equal today."""
        assert get_future_pretty_date(0) == get_pretty_date()

    def test_get_future_pretty_date_one_day(self):
        """Tomorrow should be one day after today."""
        future = get_future_pretty_date(1)
        today = datetime.now()
        tomorrow = today + timedelta(days=1)
        expected = tomorrow.strftime("%A, %B %d, %Y")
        assert future == expected


class TestHyphenatedDates:
    """Tests for DD-MM-YYYY and MM-DD-YYYY formats."""

    def test_dd_mm_yyyy_format(self):
        """Should return DD-MM-YYYY pattern."""
        result = dd_mm_yyyy()
        assert re.match(r'\d{2}-\d{2}-\d{4}', result)

    def test_mm_dd_yyyy_format(self):
        """Should return MM-DD-YYYY pattern."""
        result = mm_dd_yyyy()
        assert re.match(r'\d{2}-\d{2}-\d{4}', result)

    def test_dd_mm_yyyy_vs_mm_dd_yyyy_are_different(self):
        """Should generally produce different values (unless day==month)."""
        d = dd_mm_yyyy()
        m = mm_dd_yyyy()
        parts_d = d.split('-')
        parts_m = m.split('-')
        # DD-MM-YYYY first two are day,month; MM-DD-YYYY first two are month,day
        if parts_d[0] != parts_m[0]:  # day may equal month on same numbers
            assert parts_d[0] == parts_m[1]
            assert parts_d[1] == parts_m[0]

    def test_past_dd_mm_yyyy(self):
        """Past date should differ from current and have correct format."""
        result = past_dd_mm_yyyy(30)
        assert re.match(r'\d{2}-\d{2}-\d{4}', result)
        assert result != dd_mm_yyyy()

    def test_future_dd_mm_yyyy(self):
        """Future date should differ from current."""
        result = future_dd_mm_yyyy(30)
        assert re.match(r'\d{2}-\d{2}-\d{4}', result)
        assert result != dd_mm_yyyy()

    def test_past_vs_future_symmetry(self):
        """Past N days ago should differ from future N days from now."""
        assert past_dd_mm_yyyy(7) != future_dd_mm_yyyy(7)


class TestSlashDates:
    """Tests for DD/MM/YYYY and MM/DD/YYYY formats."""

    def test_slash_dd_mm_yyyy_format(self):
        """Should return DD/MM/YYYY pattern."""
        result = slash_dd_mm_yyyy()
        assert re.match(r'\d{2}/\d{2}/\d{4}', result)

    def test_slash_mm_dd_yyyy_format(self):
        """Should return MM/DD/YYYY pattern."""
        result = slash_mm_dd_yyyy()
        assert re.match(r'\d{2}/\d{2}/\d{4}', result)

    def test_past_slash_vs_current(self):
        """Past slash date should differ from current slash date."""
        assert past_slash_dd_mm_yyyy(14) != slash_dd_mm_yyyy()

    def test_future_slash_vs_current(self):
        """Future slash date should differ from current."""
        assert future_slash_dd_mm_yyyy(14) != slash_dd_mm_yyyy()


class TestUtilityFunctions:
    """Tests for helper/utility functions."""

    def test_list_available_formats(self):
        """Should list all registered format keys."""
        formats = list_available_formats()
        assert isinstance(formats, list)
        assert "pretty" in formats
        assert "dd-mm-yyyy" in formats
        assert "mm/dd/yyyy" in formats
        assert set(formats) == set(_FORMATS.keys())

    def test_negative_days_ago(self):
        """Negative days_ago should effectively be a future date."""
        past = past_dd_mm_yyyy(-7)
        future = future_dd_mm_yyyy(7)
        assert past == future

    def test_negative_days_future(self):
        """Negative days_from_now should effectively be a past date."""
        future = future_dd_mm_yyyy(-7)
        past = past_dd_mm_yyyy(7)
        assert future == past

    @pytest.mark.parametrize("days", [1, 3, 7, 30, 365])
    def test_various_past_periods(self, days):
        """Should produce valid dates for various periods."""
        result = past_dd_mm_yyyy(days)
        assert re.match(r'\d{2}-\d{2}-\d{4}', result)

    @pytest.mark.parametrize("days", [1, 3, 7, 30, 365])
    def test_various_future_periods(self, days):
        """Should produce valid dates for various future periods."""
        result = future_dd_mm_yyyy(days)
        assert re.match(r'\d{2}-\d{2}-\d{4}', result)
