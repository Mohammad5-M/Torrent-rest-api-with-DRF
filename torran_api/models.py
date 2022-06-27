from django.db import models

# Create your models here.
class files(models.Model):
    name = models.CharField(max_length=100, blank=False)
    info = models.TextField()
    magnet_url = models.TextField(blank=False)
    DandT = models.DateTimeField()
    # se = models.CharField()
    # le = models.CharField()
    CHOICES_CATEGORY = [
        ('AM', 'Adult Movie'),
        ('MO', 'Movie and series'),
        ('MS', 'Music'),
        ('SO', 'Software and app'),
        ('GM', 'Game'),
    ]
    category = models.CharField(max_length=20,choices=CHOICES_CATEGORY)
    Downloads = models.IntegerField(default=0)
    size = models.CharField(max_length=10)
    uploader = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name} | {self.DandT} | {self.uploader}'