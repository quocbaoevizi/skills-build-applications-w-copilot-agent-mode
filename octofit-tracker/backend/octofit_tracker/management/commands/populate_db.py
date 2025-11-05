from django.core.management.base import BaseCommand
from octofit_tracker.models.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Users (superheroes)
        users = [
            User(name='Iron Man', email='ironman@marvel.com', team='Marvel'),
            User(name='Captain America', email='cap@marvel.com', team='Marvel'),
            User(name='Spider-Man', email='spiderman@marvel.com', team='Marvel'),
            User(name='Batman', email='batman@dc.com', team='DC'),
            User(name='Superman', email='superman@dc.com', team='DC'),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team='DC'),
        ]
        for user in users:
            user.save()

        # Activities
        activities = [
            Activity(user='Iron Man', type='Running', duration=30, date='2025-11-01'),
            Activity(user='Batman', type='Cycling', duration=45, date='2025-11-02'),
            Activity(user='Wonder Woman', type='Swimming', duration=60, date='2025-11-03'),
        ]
        for activity in activities:
            activity.save()

        # Leaderboard
        Leaderboard.objects.create(team='Marvel', points=100)
        Leaderboard.objects.create(team='DC', points=120)

        # Workouts
        workouts = [
            Workout(name='Hero HIIT', description='High intensity for heroes', suggested_for='Marvel'),
            Workout(name='Power Yoga', description='Strength and flexibility', suggested_for='DC'),
        ]
        for workout in workouts:
            workout.save()

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
