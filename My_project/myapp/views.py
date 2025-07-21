from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import News  # Предполагается, что есть модель News

def home(request):
    latest_news = News.objects.order_by('-date')[:3]
    return render(request, 'myapp/home.html', {'latest_news': latest_news})

def about(request):
    return render(request, 'myapp/about.html')

def contacts(request):
    if request.method == 'POST':
        # Обработка формы обратной связи (можно расширить)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Тут можно сохранить или отправить письмо
        # Для простоты — перенаправим на страницу с благодарностью или обратно
        return HttpResponseRedirect('/')
    return render(request, 'myapp/contacts.html')

def news_list(request):
    news_items = News.objects.order_by('-date')
    return render(request, 'myapp/news.html', {'news_list': news_items})

def news_detail(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    return render(request, 'myapp/news_detail.html', {'news': news_item})

def help_page(request):
    return render(request, 'myapp/help.html')