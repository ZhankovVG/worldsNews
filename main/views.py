from django.shortcuts import render


def main(request):
    # главная страница
    return render(request, 'main/main.html')


def about(request):
    # страница про нас
    return render(request, 'main/about.html')