import json
import threading

from django.core.serializers import serialize
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse

from main.handler import handle_resume, handle_application
from main.models import News, Vacancy


def index(request):
    if request.method == 'GET':
        news = News.objects.all()
        vacancies = Vacancy.objects.all()
        context = {
            'news': news,
            'vacancies': serialize('json', vacancies),
            'vacancies_jinja': vacancies,
        }
        return render(request, 'index.html', context)


def handle_request(request, function):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print(data)
            threading.Thread(target=function, args=(data,)).start()
        except Exception as e:
            print(e)
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'Method not allowed'})


def resume(request):
    return handle_request(request, handle_resume)


def incoming_application(request):
    return handle_request(request, handle_application)
