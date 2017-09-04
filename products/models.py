from django.db import models
from django.utils import timezone
# Create your models here.
class Farm_produces(models.Model):
      author = models.ForeignKey('auth.User')
      name = models.CharField(max_length=200)
      photo = models.FileField(upload_to='uploads/')
      description = models.TextField()
      created_date = models.DateTimeField(
              default=timezone.now)
      published_date = models.DateTimeField(
              blank=True, null=True)

      def publish(self):
              self.published_date = timezone.now()
              self.save()

      def __str__(self):
               return self.name

class Latest_farm_produces(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    photo = models.FileField(upload_to='uploads/')
    description = models.TextField()
    created_date = models.DateTimeField(
             default=timezone.now)
    published_date = models.DateTimeField(
             blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.name

class Rolgezfarm_services(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200, default="Rolgezfarm Services")
    photo = models.FileField(upload_to='uploads/')
    service_info = models.TextField()
    principleone = models.CharField(max_length=200, default="Principal One")
    principletwo = models.CharField(max_length=200, default="Principal Two")
    principlethree = models.CharField(max_length=200, default="Principal Three")
    principlefour = models.CharField(max_length=200, default="Principal Four")
    rolgezfarm_history = models.TextField()
    created_date = models.DateTimeField(
             default=timezone.now)
    published_date = models.DateTimeField(
             blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.name

class Rolgezfarm_contacts(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200, default="Rolgezfarm Contact Info")
    about_us = models.TextField()
    postal_address = models.CharField(max_length=200)
    email_address = models.CharField(max_length=200)
    phone_numbers = models.CharField(max_length=200)
    facebook_link = models.CharField(max_length=200)
    twitter_link = models.CharField(max_length=200)
    created_date = models.DateTimeField(
             default=timezone.now)
    published_date = models.DateTimeField(
             blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.name
