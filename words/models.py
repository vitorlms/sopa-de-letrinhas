from django.db import models

# Create your models here.
class Word(models.Model):
  text = models.CharField(max_length=46)

  def __str__(self):
    return self.text
    