from django.db import models


class DotPlot(models.Model):
    meeting_date = models.DateField()
    year = models.PositiveIntegerField()
    rate = models.FloatField()

    class Meta:
        ordering = ['meeting_date', 'year', 'rate']

    def __str__(self):
        return self.meeting_date


class DotPlotStat(models.Model):
    meeting_date = models.DateField()
    year = models.PositiveIntegerField()
    rate = models.FloatField()
    count = models.PositiveIntegerField()
    median = models.FloatField()

    class Meta:
        managed = False
        get_latest_by = "meeting_date"
