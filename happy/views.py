from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import JsonResponse
from .models import Point
import json


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

def point_graph(request):
    points = Point.objects.all()
    x = ['x']
    level = ['level']
    for point in points:
        level.append(point.level)
        x.append(point.created.strftime("%Y%m%d%H%M%S"))

    json_data = {
        'data': {
            'x': 'x',
            'xFormat': '%Y%m%d%H%M%S',
            'columns': [
                x, level
            ]
        },
        'axis': {
            'x': {
                'type': 'timeseries',
                'tick': {
                    'format': '%Y%m%d%H%M%S'
                }
            }
        }
    }
    return render(request,
                'happy/point/graph.html',
                {'json_data': json.dumps(json_data)})
