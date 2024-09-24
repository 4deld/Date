from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls import url
from django.views.static import serve


urlpatterns = [
    # ex: /dateapp/
    path('', views.index, name='index'),
    # ex: /dateapp/detail/
    path('detail/', views.detail, name='detail'),
    # ex: /dateapp/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # ex: /dateapp/calendar/
    path('calendar/', views.calendar, name='calendar'),
 url(r'^static/(?P<path>.*)', serve, kwargs={'insecure': True})

]

app_name='dateapp'
