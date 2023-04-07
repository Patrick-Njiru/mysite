from django.urls import path
from . import views

# app_name is convenient when you have many apps with similar urls for differentiation. View templates with url links
app_name = "polls"

urlpatterns = [
    # for generic views, use pk in url instead of ids
    path("", views.IndexView.as_view(), name='index'),
    path("<int:pk>/", views.DetailView.as_view(), name='detail'),
    path("<int:pk>/results/", views.ResultsView.as_view(), name='results'),
    path("<int:question_id>/vote/", views.vote, name='vote')
]