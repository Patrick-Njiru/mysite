from django.urls import path
from . import views

# app_name is convenient when you have many apps with similar urls for differentiation. View templates with url links
app_name = "polls"

urlpatterns = [
    path("", views.index, name='index'),
    path("<int:question_id>/", views.detail, name='detail'),
    path("<int:question_id>/results/", views.results, name='results'),
    path("<int:question_id>/vote/", views.vote, name='vote')
]