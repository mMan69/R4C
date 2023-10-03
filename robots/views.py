import http
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .forms import RobotForm


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
