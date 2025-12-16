from django.shortcuts import render
from .models import Student, Team
from django.db.models import Sum, F
from django.db.models.functions import Coalesce

def individual_leaderboard(request):
    students = Student.objects.order_by('-score')
    return render(request, 'leaderboard/individual_leaderboard.html', {'students': students})

def team_leaderboard(request):
    teams = Team.objects.annotate(
        student_score_sum=Coalesce(Sum('members__score'), 0),
        bonus_points_sum=Coalesce(Sum('bonuses__points'), 0)
    ).annotate(
        team_score=F('student_score_sum') + F('bonus_points_sum')
    ).order_by('-team_score').prefetch_related('members')

    return render(request, 'leaderboard/team_leaderboard.html', {'teams': teams})
