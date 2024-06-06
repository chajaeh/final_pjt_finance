from django.urls import path
from . import views

urlpatterns = [
    path('', views.update_detail),
    path('add_deposit/', views.add_deposit),
    path('recommend/', views.recommend),
    path('recommend_loan/', views.recommend_loan),
    path('warn/', views.warn),
    path('warn_signout/', views.warn_signout)
    ]