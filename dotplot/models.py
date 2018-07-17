from django.db import models


class DotPlot(models.Model):
    meeting_date = models.DateField()
    year = models.PositiveIntegerField()
    rate = models.FloatField()

    class Meta:
        ordering = ['meeting_date', 'year', 'rate']

    def __str__(self):
        return self.meeting_date
