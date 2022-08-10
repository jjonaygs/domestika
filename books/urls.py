from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from books import views

urlpatterns = [
    path('authors/', views.AuthortList.as_view()),
    # path('authors/<int:pk>/', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
