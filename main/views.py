from django.shortcuts import render

from main.models import News, Vacancy


# Create your views here.
def index(request):
    news = News.objects.all()
    vacancies = Vacancy.objects.all()
    context = {
        'news': news,
        'vacancies': vacancies,
    }
    return render(request, 'index.html', context)
