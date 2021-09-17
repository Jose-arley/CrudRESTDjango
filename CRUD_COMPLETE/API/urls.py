from django.urls import path
from .views import DevelopersViews


urlpatterns = [
    path('Developers-items/', DevelopersViews.as_view()),
    path('Developers-items/<int:id>', DevelopersViews.as_view())
]
