from django.urls import path

from . import views


app_name = 'dotplot'
urlpatterns = [
    path('', views.DotPlotView.as_view(), name='home'),
    path('retrieve-data', views.retrieve_dot_plot_data, name='data'),
]
