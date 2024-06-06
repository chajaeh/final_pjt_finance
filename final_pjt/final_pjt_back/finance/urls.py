from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list),
    path('deposit/<str:fin_prdt_cd>/', views.deposit_detail),
    path('saving/<str:fin_prdt_cd>/', views.saving_detail),
    path('get_deposit_list/', views.get_deposit_list),
    path('get_saving_list/', views.get_saving_list),
    path('exchange/', views.exchange),
    path('chatbot/', views.chatbot),
    path('chatbot/usercommand/', views.usercommand),
    path('get_loan/', views.get_loan),
    path('get_loan_list/', views.get_loan_list),
    ]