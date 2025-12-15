# blogicum/blogicum/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # Главная страница
    path('pages/', include('pages.urls')),  # Страницы about и rules
]
