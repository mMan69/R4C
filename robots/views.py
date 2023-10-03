import http
import json
import datetime as dt

from django.shortcuts import render
from django.http import JsonResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET

from .utils import RobotsReport
from .forms import RobotForm


@require_GET
def index(request):
    return render(request, 'index.html')


@csrf_exempt
def create_robot(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

        except json.JSONDecodeError:
            return JsonResponse({'message': 'Invalid json'})

        form = RobotForm(data)

        if form.is_valid():
            robot = form.save(commit=False)
            robot.model = form.cleaned_data['model'].upper()
            robot.version = form.cleaned_data['version'].upper()
            robot.serial = form.get_serial()
            robot.save()
            return JsonResponse({'message': 'Robot created successfully'}, status=http.HTTPStatus.CREATED)

        else:
            return JsonResponse({'errors': form.errors}, status=http.HTTPStatus.BAD_REQUEST)

    else:
        return JsonResponse({'message': 'Invalid request method'}, status=http.HTTPStatus.METHOD_NOT_ALLOWED)


@require_GET
def download_report(request):
    file = RobotsReport()
    file_path = file.get_report()
    return FileResponse(
        open(file_path, 'rb'),
        filename=f'Отчет производства роботов {dt.datetime.now().strftime("%d-%B-%Y")}.xlsx'
    )
