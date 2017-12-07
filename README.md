django-variable-resolution-date
===============================

[![Build Status](https://travis-ci.org/skioo/django-variable-resolution-date.svg?branch=master)](https://travis-ci.org/skioo/django-variable-resolution-date)
[![PyPI version](https://badge.fury.io/py/django-variable-resolution-date.svg)](https://badge.fury.io/py/django-variable-resolution-date)
[![Requirements Status](https://requires.io/github/skioo/django-variable-resolution-date/requirements.svg?branch=master)](https://requires.io/github/skioo/django-variable-resolution-date/requirements/?branch=master)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)


A django field that can represent either a year, or a year and a month, or a full calendar date.

This is useful when the precision of your data varies (perhaps your legacy data only contains a year whereas you now start collecting full dates).

The representation in the database is simply a string in https://en.wikipedia.org/wiki/ISO_8601 format.
This means we cannot use date-specific database operations, but we can still leverage the fact that the 
lexicographical order corresponds to the chronological order:

- Sorting on a VariableResolutionDateField column will sort chronologically.
- We can filter for dates within a range by using string operations, for instance: `member_since > '2000'`



Requirements
------------

* Python: 3.4 and over
* Django: 1.10 and over


Usage
-----

Install from pip:

    pip install django-variable-resolution-date
   
   
Use in your models:

    from django.db import models
    from variable_resolution_date import VariableResolutionDateField


    class ClubMember(models.Model):
        name = models.CharField(max_length=100)
        member_since = VariableResolutionDateField()


The input widget for such fields is a text field that verifies the input is valid. For instance:
* `1996`, `1996-02`, `1996-02-29` are valid
* `1997-02-29` is invalid


