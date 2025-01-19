from django.urls import path
from main import views as app

app_name = "main"
urlpatterns = [
    path('', app.home, name="home"),
    path('signup/', app.signup, name="signup"),
]
