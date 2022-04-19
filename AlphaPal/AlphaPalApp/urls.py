from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('process/', views.process, name='process'),
    path('summary/', views.summary, name='summary'),
    path('transaction/', views.transaction, name='transaction'),
    path('createform/', views.createform, name='createform'),
    path('update/<str:pk>/', views.update, name='update'),
    path('detail/<str:pk>/', views.detail, name='detail'),
    path('delete/<str:pk>/', views.delete, name='delete'),
    path('createaccount/', views.createaccount, name='createaccount'),
    path('loansafe/', views.loansafe, name='loansafe'),
]


