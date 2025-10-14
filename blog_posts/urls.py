from django.urls import path
from . import views
urlpatterns = [
    path('', views.post_list, name='home'),   #Ana Sayfa
    #int:pk kavramı urldeki ID yi yakalamak için yazıldı integer:tam sayı , pk:primary key (değişken)
    path('<int:pk>/', views.post_detail, name='post_detail'),  #Detay Sayfası
]
