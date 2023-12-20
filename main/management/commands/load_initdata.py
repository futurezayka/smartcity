from django.core.management.base import BaseCommand
import json

from main.models import News, Vacancy


class Command(BaseCommand):
    help = 'Load initial data if models are empty'

    def handle(self, *args, **options):
        if News.objects.exists():
            News.objects.all().delete()

        if Vacancy.objects.exists():
            Vacancy.objects.all().delete()

        self.loaddata('news.json')
        self.loaddata('vacancies.json')

    def loaddata(self, fixture_file):
        from django.core.management import call_command
        call_command('loaddata', fixture_file)
