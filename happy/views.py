import json
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Avg
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

def point_graph(request):
    points = Point.objects.extra(
            {'agg_date':"date(created)"}).values(
            'agg_date').annotate(avg_level=Avg('level'))

    x = ['x']
    level = ['level']
    for point in points:
        level.append(point['avg_level'])
        x.append(point['agg_date'])

    json_data = {
        'data': {
            'x': 'x',
            'xFormat': '%Y-%m-%d',
            'columns': [
                x, level
            ]
        },
        'axis': {
            'x': {
                'type': 'timeseries',
                'tick': {
                    'format': '%Y-%m-%d'
                }
            },
            'y': {
                'max': 5,
                'min': 0
            }
        }
    }
    return render(request,
                'happy/point/graph.html',
                {'json_data': json.dumps(json_data)})
