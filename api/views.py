import json

from django.core import serializers
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from api.models import Car, Dht, Ph


class TestView(View):

    def get(self, request, *args, **kwargs):
        data = {
            'message': 'success'
        }
        return JsonResponse(data, status=200)


class CarView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(CarView, self).dispatch(request, *args, **kwargs)

    # POST 요청을 처리하기 위해서 post함수를 재정의
    def post(self, request, *args, **kwargs):
        if request.META['CONTENT_TYPE'] == 'application/json':
            req = json.loads(request.body)
            print('name: ' + req['name']+'\n')
            print('brand: ' + req['brand'] + '\n')
            print('price: ' + str(req['price']) + '\n')

            car = Car(name=req['name'], brand=req['brand'], price=req['price'])
            car.save()

            data = {
                'message': 'success'
            }
            return JsonResponse(data, status=200)

        data = {
            'massage': 'failed'
        }
        return JsonResponse(data, status=403)


class DHTView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(DHTView, self).dispatch(request, *args, **kwargs)

    # GET 요청을 처리하기 위해서 get함수를 재정의
    def get(self, request, *args, **kwargs):
        dhts = serializers.serialize("json", Dht.objects.all())
        print(dhts)
        return JsonResponse(dhts,
                            safe=False,
                            json_dumps_params={'ensure_ascii': False},
                            status=200
                            )

    # POST 요청을 처리하기 위해서 post함수를 재정의
    def post(self, request, *args, **kwargs):
        if request.META['CONTENT_TYPE'] == 'application/json':
            req = json.loads(request.body)
            print('temperature: ' + str(req['temperature'])+'\n')
            print('humidity: ' + str(req['humidity']) + '\n')

            dht = Dht(temperature=req['temperature'], humidity=req['humidity'])
            dht.save()

            data = {
                'message': 'success'
            }
            return JsonResponse(data, status=200)

        data = {
            'massage': 'failed'
        }
        return JsonResponse(data, status=403)


class PHView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(PHView, self).dispatch(request, *args, **kwargs)

    # GET 요청을 처리하기 위해서 get함수를 재정의
    def get(self, request, *args, **kwargs):
        phs = serializers.serialize("json", Ph.objects.all())
        print(phs)
        return JsonResponse(phs,
                            safe=False,
                            json_dumps_params={'ensure_ascii': False},
                            status=200
                            )

    # POST 요청을 처리하기 위해서 post함수를 재정의
    def post(self, request, *args, **kwargs):

        if request.META['CONTENT_TYPE'] == 'application/json':
            req = json.loads(request.body)
            pHValue = round(req['pH'], 2)
            print('pH: ' + str(pHValue) + '\n')
            ph = Ph(ph=pHValue)
            ph.save()

            data = {
                'message': 'success'
            }
            return JsonResponse(data, status=200)

        data = {
            'massage': 'failed'
        }
        return JsonResponse(data, status=403)