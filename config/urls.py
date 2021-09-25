from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('quiz/', include('quiz.urls')),
    path('admin/', admin.site.urls),
]
