from django.core.exceptions import ValidationError
from django.test import TestCase
from pytest import raises

from .models import ClubMember


class VariableResolutionDateFieldTest(TestCase):
    def test_it_can_create_vrd_with_year(self):
        ClubMember(name='adam', member_since='1996').full_clean()

    def test_it_can_create_vrd_with_year_and_month(self):
        ClubMember(name='bob', member_since='1996-02').full_clean()

    def test_it_can_create_vrd_with_full_date(self):
        ClubMember(name='charlie', member_since='1996-02-29').full_clean()

    def test_it_cannot_create_vrd_with_invalid_full_date(self):
        with raises(ValidationError) as ex:
            ClubMember(name='dave', member_since='1997-02-29').full_clean()
        assert ex.value.messages == ['Enter a year, year-month, or year-month-day.']

    def test_it_cannot_create_vrd_with_extra_characters(self):
        with raises(ValidationError) as ex:
            ClubMember(name='earl', member_since='20001').full_clean()
        assert ex.value.messages == ['Enter a year, year-month, or year-month-day.']

    def test_it_cannot_create_vrd_with_month_day(self):
        with raises(ValidationError) as ex:
            ClubMember(name='fred', member_since='02-03').full_clean()
        assert ex.value.messages == ['Enter a year, year-month, or year-month-day.']
