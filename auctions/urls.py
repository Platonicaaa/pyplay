from django.urls import path

from . import views

app_name = 'auctions'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:auction_id>/bid/', views.bid, name='bid'),
]
