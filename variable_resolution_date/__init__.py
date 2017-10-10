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

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.encoding import force_text
import re

VARIABLE_RESOLUTION_DATE_RE = re.compile(r'^(\d{4})(?:-(\d{2})(?:-(\d{2}))?)?$')
VARIABLE_RESOLUTION_DATE_LENGTH = 10


def validate_variable_resolution_date(value):
    match = VARIABLE_RESOLUTION_DATE_RE.match(force_text(value))
    if match:
        year = int(match.group(1))
        month = int(match.group(2) or 1)
        day = int(match.group(3) or 1)
        try:
            datetime.date(year, month, day)
            return
        except:
            pass
    raise ValidationError('Enter a year, year-month, or year-month-day.')


class VariableResolutionDateField(models.CharField):
    default_validators = [validate_variable_resolution_date]
    description = 'A year, year-month, or year-month-day date'

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = VARIABLE_RESOLUTION_DATE_LENGTH
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        if kwargs['max_length'] == VARIABLE_RESOLUTION_DATE_LENGTH:
            del kwargs['max_length']
        return name, path, args, kwargs
