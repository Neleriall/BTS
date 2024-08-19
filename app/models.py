from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Parcel(BaseModel):
    TRACKING_STATUS_CHOICES = [
        ('В пути', 'Pending'),
        ('Едут за посылкой', 'In Transit'),
        ('Доставлен', 'Delivered'),
        ('Отменен', 'Canceled'),
    ]
    CHOOSE_TYPE = [
        ('Экспресс', 'Express'),
        ('Логистическая', 'Logistic'),
        ('Курьерская', 'Courier'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sender_name = models.CharField(max_length=255)
    receiver_name = models.CharField(max_length=255)
    sender_address = models.TextField()
    receiver_address = models.TextField()
    weight = models.FloatField()
    sender_number = models.CharField(max_length=30)
    receiver_number = models.CharField(max_length=30)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=TRACKING_STATUS_CHOICES, default='In_Transit')
    type = models.CharField(max_length=50, choices=CHOOSE_TYPE, default='Express')

    def __str__(self):
        return self.sender_name

class ParcelInfo(BaseModel):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.title

class About(BaseModel):
    title = models.CharField(max_length=50)
    video = models.URLField()
    text = models.TextField()

    def __str__(self):
        return self.title

class Contact(BaseModel):
    title = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    tel = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    
    
    def __str__(self):
        return self.title


class Form(BaseModel):
    name = models.CharField(max_length=50, default='')
    number = models.CharField(max_length=30, default='')
    message = models.TextField()

    def __str__(self):
        return self.name

class ProfileForm(Parcel):

    def __str__(self):
        return self.sender_address
    

class Slider(BaseModel):
    image = models.ImageField(upload_to='media/')


class Why(BaseModel):
    image = models.ImageField(upload_to='media/')
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title