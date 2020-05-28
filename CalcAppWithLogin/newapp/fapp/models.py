from django.db import models

class ContactInfo(models.Model):
    fn = models.CharField(max_length=20)
    ln = models.CharField(max_length=20)
    subject = models.TextField(max_length=200)

    def __str__(self):
        return self.fn

