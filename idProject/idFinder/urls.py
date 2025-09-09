from django.urls import path
from . import views
from .views import found_id_api, lost_id_api

urlpatterns = [
    path('', views.home, name='home'),
    path('upload-found/', views.upload_found, name='upload_found'),
    path('report-lost/', views.report_lost, name='report_lost'),
    path('found/', views.found_list, name='found_list'),
    path('lost-reports/', views.view_lost_reports, name='view_lost_reports'),
    path('search-suggestions/', views.search_suggestions, name='search_suggestions'),
    path('api/found-ids/', found_id_api, name='found_id_api'),
    path('api/lost-ids/', lost_id_api, name='lost_id_api'),
]
