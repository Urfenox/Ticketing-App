from django.urls import path
from ticketing import views as app

urlpatterns = [
    path('', app.home, name="home"),
    path('/create/', app.create, name="create"),
    path('/edit/<int:id>', app.edit, name="edit"),
    path('/delete/<int:id>', app.delete, name="delete"),
]
