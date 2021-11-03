from django.shortcuts import render

def geobit(request):
    return render(request, 'core/form.html')
