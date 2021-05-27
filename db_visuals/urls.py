from django.urls import path, include
from .views import home, results_view

urlpatterns = [
    path('', home, name="home"),
    # path('results_view/<str:res>', results_view, name='results_view'),
    path('<str:query>', results_view, name='results_view'),
]
