from django.urls import path
from . import views

urlpatterns = [
#используем именованный URL и определяем направление запроса для начальной страницы
    path('', views.post_list, name='post_list'),
]