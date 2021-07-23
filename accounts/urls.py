from django.urls import path

from . import views
from .views import SignupView

app_name = 'accounts'
urlpatterns = [
    path('', views.user_home, name='home'),
    path('signup/', SignupView.as_view(), name='signup')
]
