from django.urls import path

from . import views

urlpatterns = [
    # ex: /app/
    path('', views.index, name='index'),
    # ex: /app/detail/
    path('/detail/', views.detail, name='detail'),
    # ex: /app/results/
    path('/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]