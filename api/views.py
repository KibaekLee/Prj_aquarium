import datetime
import json

from django.core import serializers
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from api.models import Ph


class PHView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(PHView, self).dispatch(request, *args, **kwargs)

    # GET 요청을 처리하기 위해서 get함수를 재정의
    def get(self, request, *args, **kwargs):
        phs = serializers.serialize("json", Ph.objects.filter(
            created_at__gte=datetime.date.today()
        ))
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