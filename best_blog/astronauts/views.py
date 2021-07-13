import json

from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView            #низкий уровень абстракции (для DRF)

from .serializers import CraftSerializer
from .models import Craft


# class CraftView(viewsets.ModelViewSet):         #наследуемся от абстратктного класса (сам по себе не работает, его нужно наследовать)
#     serializer_class = CraftSerializer
#     queryset = Craft.objects.all()
#     permission_classes = [permissions.AllowAny]

class CraftView(APIView):
    def get(self, request):
        data = {}
        crafts = Craft.objects.all()
        data['number'] = len(crafts)
        craft_list = []
        for craft in crafts:
            craft_list.append({'name': craft.name, "origin": craft.origin})
        data['crafts'] = craft_list
        return Response(json.dumps(data))

    def post(self, request):
        print(request.body.decode('UTF-8'))
        specs = json.loads(request.body.decode('UTF-8'))
        new_craft = Craft()
        # for key,value in specs.items():
        new_craft.name = specs['name']
        new_craft.origin = specs['origin']
        new_craft.save()
        return Response(new_craft)






