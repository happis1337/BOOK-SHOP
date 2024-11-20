from django.urls import path
from django.contrib import admin
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('book/<int:book_id>/', BookView.as_view(), name='book_detail'),
    path('author/<int:author_id>/', AuthorView.as_view(), name='author_detail'),
]