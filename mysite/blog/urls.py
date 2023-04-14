from django.urls import path, include
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.postagem, name='postagem'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)