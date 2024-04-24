from django.urls import path
from ticketing import views as app

urlpatterns = [
    path('', app.home, name="home"),
    path('create/', app.create, name="create"),
    path('edit/<int:id>', app.edit, name="edit"),
    path('delete/<int:id>', app.delete, name="delete"),
    path('view/<int:id>', app.view, name="view"),
    path('view/<int:id>/comment', app.view, name="view_comment"),
    path('adjuntos/<str:uid>', app.adjuntos, name="adjunto"),
]
