from django.shortcuts import render

def aurea_view(request):
    return render(request, 'meu_app/aurea.html')