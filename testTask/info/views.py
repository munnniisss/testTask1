from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Info
from .serializers import InfoSerializer


class InfoView(APIView):
    def get(self, request):
        data = Info.objects.all()
        serializer = InfoSerializer(data, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        pk = request.data.get('pk')

        try:
            data = Info.objects.get(pk=pk)

            if data.quarters <= 20:
                return Response({'status': True})
            return Response({'status': False})

        except Exception as ex:
            return Response({'status': None})


def index(request):
    data = Info.objects.all()
    return render(request, 'info/index.html', {'data': data})

