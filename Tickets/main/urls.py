from django.urls import path
from main import views as app

urlpatterns = [
    path('', app.home),
    path('signup/', app.signup, name="signup"),
]
