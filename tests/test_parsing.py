from django.core.exceptions import ValidationError
from django.test import TestCase
from pytest import raises

from variable_resolution_date import parse


class VariableResolutionDateFieldTest(TestCase):
    def test_it_can_parse_vrd_with_year(self):
        y, m, d = parse('1996')
        assert y == 1996
        assert m is None
        assert d is None

    def test_it_can_parse_vrd_with_year_and_month(self):
        y, m, d = parse('1996-02')
        assert y == 1996
        assert m == 2
        assert d is None

    def test_it_can_parse_vrd_with_full_date(self):
        y, m, d = parse('1996-02-29')
        assert y == 1996
        assert m == 2
        assert d is 29

    def test_it_cannot_parse_vrd_with_invalid_full_date(self):
        with raises(ValidationError) as ex:
            parse('1997-02-29')
        assert ex.value.messages == ['Must be a valid year, year-month, or year-month-day.']

    def test_it_cannot_parse_vrd_with_extra_characters(self):
        with raises(ValidationError) as ex:
            parse('20001')
        assert ex.value.messages == ['Must be a valid year, year-month, or year-month-day.']

    def test_it_cannot_parse_vrd_with_month_day(self):
        with raises(ValidationError) as ex:
            parse('02-03')
        assert ex.value.messages == ['Must be a valid year, year-month, or year-month-day.']
