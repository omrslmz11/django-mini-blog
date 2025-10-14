from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)   #Blog Başlığıdır.
    content = models.TextField()                 #Ana içerik
    author = models.CharField(max_length=100)    #Yazarın adı
    created_at = models.DateTimeField(default=timezone.now)   #Oluşturulma Tarihi
#Model objesinin başlığını döndürme amacıyla (Panelde okunurluk)
    def __str__(self):
        return super().__str__()
    