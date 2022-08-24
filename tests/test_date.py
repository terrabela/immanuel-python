"""
    This file is part of immanuel - (C) The Rift Lab
    Author: Robert Davies (robert@theriftlab.com)


    Gregorian UTC / Julian Day conversions ran against
    figures from direct swisseph functions.
"""

from datetime import datetime
from zoneinfo import ZoneInfo

from pytest import approx, fixture
import swisseph as swe

from immanuel.tools import date


@fixture
def utc_date_tuple():
    return (2000, 1, 1, 18, 0, 0)

@fixture
def utc_date():
    return datetime(2000, 1, 1, 18, tzinfo=ZoneInfo('UTC'))

@fixture
def pst_date():
    return datetime(2000, 1, 1, 10, tzinfo=ZoneInfo('America/Los_Angeles'))

@fixture
def ambiguous_date():
    return datetime(2022, 11, 6, 1, 30, tzinfo=ZoneInfo('America/Los_Angeles'))

@fixture
def utc_coords():
    return 51.509865, -0.118092     # London lat/lon

@fixture
def pst_coords():
    return 32.715736, -117.161087   # San Diego lat/lon

@fixture
def jd():
    return 2451545.1250041085       # 2000-01-01 15:00 UTC


def test_timezone_utc(utc_coords):
    assert date.timezone(*utc_coords) == 'Europe/London'


def test_timezone_pst(pst_coords):
    assert date.timezone(*pst_coords) == 'America/Los_Angeles'


def test_localize(pst_coords):
    dt = datetime(2000, 1, 1, 18)
    aware = date.localize(dt, *pst_coords)
    assert aware.tzinfo == ZoneInfo('America/Los_Angeles')


def test_localize_dst(ambiguous_date, pst_coords):
    dt_no_dst = date.localize(ambiguous_date, *pst_coords, False)
    dt_dst = date.localize(ambiguous_date, *pst_coords, True)
    jd_no_dst = date.datetime_to_jd(dt_no_dst)
    jd_dst = date.datetime_to_jd(dt_dst)
    assert dt_no_dst.hour == dt_dst.hour
    assert jd_no_dst - jd_dst == approx(1/24)


def test_ambiguous(ambiguous_date, pst_date):
    assert date.ambiguous(ambiguous_date) == True
    assert date.ambiguous(pst_date) == False


def test_datetime_to_jd_calc(utc_date_tuple, utc_date, pst_date):
    jd_utc = date.datetime_to_jd(utc_date)
    jd_pst = date.datetime_to_jd(pst_date)
    jd_utc_swe = swe.utc_to_jd(*utc_date_tuple)[1]
    assert jd_utc == jd_utc_swe
    assert jd_pst == jd_utc_swe


def test_jd_to_datetime_utc(jd):
    dt = date.jd_to_datetime(jd)
    assert dt.year == 2000
    assert dt.month == 1
    assert dt.day == 1
    assert dt.hour == 15
    assert dt.minute == 0
    assert dt.second == 0
    assert dt.tzinfo == ZoneInfo('UTC')


def test_jd_to_datetime_pst(jd, pst_coords):
    dt = date.jd_to_datetime(jd, *pst_coords)
    assert dt.year == 2000
    assert dt.month == 1
    assert dt.day == 1
    assert dt.hour == 7
    assert dt.minute == 0
    assert dt.second == 0
    assert dt.tzinfo == ZoneInfo('America/Los_Angeles')
