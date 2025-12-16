from django.db import models
from django.db.models import Sum

class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    cups = models.IntegerField(default=0)
    title = models.CharField(max_length=100, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, related_name='members', blank=True, null=True)

    def __str__(self):
        return self.name

class TeamBonus(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='bonuses')
    points = models.IntegerField()
    reason = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.points} for {self.team.name}'
