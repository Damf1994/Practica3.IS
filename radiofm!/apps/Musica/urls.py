from django.urls import path

from apps.Musica.views import IndexView, Top_SongsView 

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('top', Top_SongsView.as_view(), name='top_songs'),

]