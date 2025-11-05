from django.test import TestCase
from .models.models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(name='Test User', email='test@example.com', team='Test Team')
        self.assertEqual(user.name, 'Test User')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(user='Test User', type='Running', duration=30, date='2025-11-05')
        self.assertEqual(activity.type, 'Running')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        leaderboard = Leaderboard.objects.create(team='Test Team', points=100)
        self.assertEqual(leaderboard.points, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Push Ups', description='Upper body exercise', suggested_for='All')
        self.assertEqual(workout.name, 'Push Ups')
