import datetime
import json

from django.core import serializers
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from api.models import Arduino


class ArduinoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ArduinoView, self).dispatch(request, *args, **kwargs)

    # GET 요청을 처리하기 위해서 get함수를 재정의
    def get(self, request, *args, **kwargs):

        # day = request.GET.get('dayNumber', None)
        # month = request.GET.get('month', None)
        # year = request.GET.get('year', None)

        arduinos = serializers.serialize("json", Arduino.objects.filter(
            created_at__gte=datetime.date.today()

            # created_at__gte=datetime.date(int(year), int(month), int(day))
            
        ))

        return JsonResponse(arduinos,
                            safe=False,
                            json_dumps_params={'ensure_ascii': False},
                            status=200
                            )

    # POST 요청을 처리하기 위해서 post함수를 재정의
    def post(self, request, *args, **kwargs):

        if request.META['CONTENT_TYPE'] == 'application/json':
            req = json.loads(request.body)
            pHValue = round(req['pH'], 2)
            TValue = round(req['T'], 1)
            print('pH: ' + str(pHValue) + '\n')
            print('T: ' + str(TValue) + '\n')
            arduino= Arduino(ph=pHValue, temperature=TValue)
            arduino.save()

            data = {
                'message': 'success'
            }
            return JsonResponse(data, status=200)

        data = {
            'massage': 'failed'
        }
        return JsonResponse(data, status=403)

# class nowPHView(View):
#     @method_decorator(csrf_exempt)
#     def dispatch(self, request, *args, **kwargs):
#         return super(nowPHView, self).dispatch(request, *args, **kwargs)
#
#     # GET 요청을 처리하기 위해서 get함수를 재정의
#     def get(self, request, *args, **kwargs):
#
#         day = request.GET.get('dayNumber', None)
#         month = request.GET.get('month', None)
#         year = request.GET.get('year', None)
#
#         phs = serializers.serialize("json", Ph.objects.filter(
#             created_at__gte=datetime.date.today()
#
#         ))
#
#
#         return JsonResponse(phs,
#                             safe=False,
#                             json_dumps_params={'ensure_ascii': False},
#                             status=200
#                             )
#
#
#     # POST 요청을 처리하기 위해서 post함수를 재정의
#     def post(self, request, *args, **kwargs):
#
#         if request.META['CONTENT_TYPE'] == 'application/json':
#             req = json.loads(request.body)
#             pHValue = round(req['pH'], 2)
#             print('pH: ' + str(pHValue) + '\n')
#             ph = Ph(ph=pHValue)
#             ph.save()
#
#             data = {
#                 'message': 'success'
#             }
#             return JsonResponse(data, status=200)
#
#         data = {
#             'massage': 'failed'
#         }
#         return JsonResponse(data, status=403)