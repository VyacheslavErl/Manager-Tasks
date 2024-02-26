from django.urls import path

from companies.views import companies_main, workers


urlpatterns = [
    path('', companies_main),
    path('workers/', workers)
]
