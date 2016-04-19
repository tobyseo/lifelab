from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Point


def point_create(request):
    if request.method == 'POST':
        user = User.objects.get(username='toby')
        level = int(request.POST['level'])
        point = Point.objects.create(user=user, level=level)
        point.save()

    return render(request, 'happy/point/create.html')

def point_list(request):
    points = Point.objects.all()
    return render(request, 'happy/point/list.html', {'points': points})
