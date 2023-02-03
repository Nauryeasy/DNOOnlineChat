from django.db import models
from django.urls import reverse


class Contacts(models.Model):
    person1 = models.CharField(max_length=100)
    person2 = models.CharField(max_length=100)


class Messages(models.Model):
    id_contact = models.CharField(max_length=100)
    sender = models.TextField('Отправитель')
    message = models.TextField('Текст сообщения')

    def get_absolute_url(self):
        return reverse("contact_chat", kwargs={'pk': self.id_contact})