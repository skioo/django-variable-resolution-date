from django.db import models

from variable_resolution_date import VariableResolutionDateField


class ClubMember(models.Model):
    name = models.CharField(max_length=100)
    member_since = VariableResolutionDateField()
