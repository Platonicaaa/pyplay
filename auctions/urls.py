from django.urls import path

from . import views

app_name = 'auctions'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('<int:pk>/edit/', views.EditView.as_view(), name='edit'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:auction_id>/bid/', views.bid, name='bid'),
]
