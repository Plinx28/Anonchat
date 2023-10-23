from django.db import models
from django.urls import reverse

# Create your models here.

class Message(models.Model):
    text = models.TextField()
    secret_phrase = models.TextField()
    note_hash = models.TextField(null=True)
    create_time = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return self.secret_phrase
    
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})
    
    class Meta:
        verbose_name = 'Анонимные записки'
        verbose_name_plural = 'Анонимные записки'
        ordering = ['create_time', 'secret_phrase']