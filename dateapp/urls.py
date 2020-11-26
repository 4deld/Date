from django.urls import path

from . import views


urlpatterns = [
    # ex: /dateapp/
    path('', views.index, name='index'),
    # ex: /dateapp/detail/
    path('detail/', views.detail, name='detail'),
    # ex: /dateapp/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # ex: /dateapp/calendar/
    path('calendar/', views.calendar, name='calendar'),
]

app_name='dateapp'
