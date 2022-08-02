from email.mime import image
from django.db import models

# Create your models here.


# lets us explicitly set upload path and filename
def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)


class files(models.Model):
    name = models.CharField(max_length=100, blank=False)
    info = models.TextField()
    magnet_url = models.TextField(blank=False)
    DandT = models.DateTimeField()
    # se = models.IntegerField()
    # le = models.IntegerField()
    CHOICES_CATEGORY = [
        ('MO', 'Movie'),
        ('SE', 'series'),
        ('MS', 'Music'),
        ('SO', 'Software and app'),
        ('GM', 'Game'),
    ]
    category = models.CharField(max_length=20, choices=CHOICES_CATEGORY)
    Downloads = models.IntegerField(default=0)
    size = models.CharField(max_length=10)
    uploader = models.CharField(max_length=20)
    image_url = models.ImageField(
        upload_to=upload_to, blank=True, null=True)

    def __str__(self):
        return f'{self.name} | {self.DandT} | {self.uploader}'
