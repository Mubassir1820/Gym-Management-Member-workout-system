from django.core.management.base import BaseCommand
from django.core.management import call_command
import os

class Command(BaseCommand):
    help = 'Load initial data from fixture'

    def handle(self, *args, **kwargs):
        fixture_file = 'data.json'
        
        if os.path.exists(fixture_file):
            self.stdout.write('Loading data from data.json...')
            try:
                call_command('loaddata', fixture_file)
                self.stdout.write(self.style.SUCCESS('Successfully loaded data!'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error loading data: {e}'))
        else:
            self.stdout.write(self.style.WARNING('data.json not found, skipping...'))