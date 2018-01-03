"""
A django field that can represent either a year, or a year and a month, or a full calendar date.

This is useful when the precision of your data varies (perhaps your legacy data only contains a year whereas
you now start collecting full dates).

The representation in the database is simply a string in https://en.wikipedia.org/wiki/ISO_8601 format.
This means we cannot use date-specific database operations, but we can still leverage the fact that the
lexicographical order corresponds to the chronological order:

- Sorting on a VariableResolutionDateField column will sort chronologically.
- We can filter for dates within a range by using string operations, for instance: `member_since > '2000'`
"""

import datetime

import re
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.encoding import force_text

VARIABLE_RESOLUTION_DATE_RE = re.compile(r'^(\d{4})(?:-(\d{2})(?:-(\d{2}))?)?$')
VARIABLE_RESOLUTION_DATE_LENGTH = 10


def parse(value):
    """ returns a triple: year, month, day (month and day may be None) """
    match = VARIABLE_RESOLUTION_DATE_RE.match(force_text(value))
    if match:
        year = int(match.group(1))
        month = int(match.group(2)) if match.group(2) else None
        day = int(match.group(3)) if match.group(3) else None
        try:
            # Make sure the different parts taken together represent a valid date.
            datetime.date(year, month or 1, day or 1)
            return year, month, day
        except ValueError:
            pass
    raise ValidationError('Must be a valid year, year-month, or year-month-day.')


def validate(value):
    parse(value)


class VariableResolutionDateField(models.CharField):
    default_validators = [validate]
    description = 'A year, year-month, or year-month-day date'

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = VARIABLE_RESOLUTION_DATE_LENGTH
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        if kwargs['max_length'] == VARIABLE_RESOLUTION_DATE_LENGTH:
            del kwargs['max_length']
        return name, path, args, kwargs
