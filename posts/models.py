import time
from django.db import models
from accounts.models import User
from django.utils.crypto import get_random_string

def generate_unique_token():
    while True:
        token = get_random_string(length=7)
        if not info.objects.filter(token=token).exists():
            return id


def upload_to(instance, filename):
    return f'posts/{filename}'

class info(models.Model):
    title = models.CharField(max_length=63)
    description = models.TextField(max_length=2047)

    meterage = models.FloatField()
    room = models.IntegerField()
    build = models.IntegerField()

    floor = models.IntegerField(null=True, blank=True)
    total_floors = models.IntegerField(null=True, blank=True)
    unit_per_floor = models.IntegerField(null=True, blank=True)

    elevator = models.BooleanField()
    parking = models.BooleanField()
    storage = models.BooleanField()

    province = models.CharField(max_length=63)
    city = models.CharField(max_length=63)
    neighbourhood = models.CharField(max_length=63)
    location = models.CharField(max_length=1023, null=True, blank=True)

    photo_0 = models.ImageField(upload_to=upload_to, null=True, blank=True)
    photo_1 = models.ImageField(upload_to=upload_to, null=True, blank=True)
    photo_2 = models.ImageField(upload_to=upload_to, null=True, blank=True)
    photo_3 = models.ImageField(upload_to=upload_to, null=True, blank=True)
    photo_4 = models.ImageField(upload_to=upload_to, null=True, blank=True)
    photo_5 = models.ImageField(upload_to=upload_to, null=True, blank=True)
    photo_6 = models.ImageField(upload_to=upload_to, null=True, blank=True)
    photo_7 = models.ImageField(upload_to=upload_to, null=True, blank=True)
    photo_8 = models.ImageField(upload_to=upload_to, null=True, blank=True)
    photo_9 = models.ImageField(upload_to=upload_to, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    timestamp = models.CharField(max_length=30, blank=True)
    visible = models.BooleanField(default=True)
    token = models.CharField(
        max_length=8,
        unique=True,
        null=True,
        editable=False
    )


    class Meta:
        abstract = True

    def __str__(self):
        return self.title + ' : ' + str(self.token)


class ApartmentSell(info):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sellPosts')

    total_price = models.IntegerField()
    price_per_meter = models.IntegerField()


    def save(self, *args, **kwargs):
        if not self.pk:

            while True:
                self.token = 'S' + get_random_string(length=8)
                if not ApartmentSell.objects.filter(token=self.token).exists():
                    self.token = 'S' + get_random_string(length=8)
                    break

            self.timestamp = '1' + str(time.time()).split('.')[0]
        return super().save(*args, **kwargs)


class ApartmentRent(info):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rentPosts')

    low_deposite = models.IntegerField()
    low_rent = models.IntegerField()
    high_deposite = models.IntegerField()
    high_rent = models.IntegerField()

    
    def save(self, *args, **kwargs):
        if not self.pk:

            while True:
                self.token = 'R' + get_random_string(length=8)
                if not ApartmentRent.objects.filter(token=self.token).exists():
                    self.token = 'R' + get_random_string(length=8)
                    break

            self.timestamp = '2' + str(time.time()).split('.')[0]
        return super().save(*args, **kwargs)

    





    

