# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, UpdateAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.parsers import MultiPartParser, FormParser

# our model
from torran_api.models import files
# our serializers
from torran_api.serializer import SR_TORRENT


# Create your views here.
class APIV(APIView):
    # renderer_classes = [JSONRenderer]

    def get(self, request):
        """this method is for get object with id and querying name"""
        if request.GET.get('id'):
            ob_file = get_object_or_404(files, id=request.GET.get('id'))
            sr = SR_TORRENT(ob_file, many=False)
        elif request.GET.get('q'):
            ob_file = files.objects.filter(name__contains=request.GET.get('q'))
            sr = SR_TORRENT(ob_file, many=True)
        else:
            return Response({'result': "just use q for query and id for getting specific object like     api/?q=the grand tour     api/?id=2"})
        return Response({'result': sr.data})


class CAPIV(CreateAPIView):
    # renderer_classes = [JSONRenderer]
    serializer_class = SR_TORRENT


class UAPIV(UpdateAPIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated, ]
    queryset = files.objects.all()
    serializer_class = SR_TORRENT
    lookup_field = 'id'


class MyModelViewSet(viewsets.ModelViewSet):
    queryset = files.objects.all()
    serializer_class = SR_TORRENT
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [
        IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
