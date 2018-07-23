from django.http import JsonResponse
from django.views.generic.base import TemplateView
from django.db.models import Q

from .models import DotPlotStat as dps


class DotPlotView(TemplateView):
    template_name = 'dotplot/dotplot.html'


def retrieve_dot_plot_data(request, meeting_date=None):
    last_date = dps.objects.latest().meeting_date
    if meeting_date:
        data = dps.objects.filter(
            Q(meeting_date=last_date) | Q(meeting_date=meeting_date)
        ).values()
    else:
        dates = dps.objects.values_list(
            'meeting_date',
            flat=True
        ).order_by(
            '-meeting_date'
        ).distinct()
        data = dps.objects.filter(
            Q(meeting_date=last_date) | Q(meeting_date=dates[1])
        ).values()
    return JsonResponse(list(data), safe=False)

