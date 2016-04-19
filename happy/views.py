from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import JsonResponse
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

def point_json(request):
    points = Point.objects.all()
    l = [{'level': point.level,
        'created': point.created.strftime("%Y%m%d%H%M%S")} for point in points]
    return JsonResponse({"data": l})
