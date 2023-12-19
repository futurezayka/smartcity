import json
import threading

from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse

from main.handler import handle_form
from main.models import News, Vacancy


# Create your views here.
def index(request):
    if request.method == 'GET':
        news = News.objects.all()
        vacancies = Vacancy.objects.all()
        context = {
            'news': news,
            'vacancies': vacancies,
        }
        return render(request, 'index.html', context)


def resume(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print(data)
            threading.Thread(target=handle_form, args=(data,)).start()
        except Exception as e:
            print(e)
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'Method not allowed'})
