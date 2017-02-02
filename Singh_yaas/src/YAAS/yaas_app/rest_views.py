__author__ = 'RAJ'
from rest_framework.decorators import api_view, renderer_classes, authentication_classes, permission_classes
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from yaas_app.serializer import AuctionSerializer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from django.http import Http404
from yaas_app.models import Auction

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@api_view(['GET'])
@renderer_classes([JSONRenderer,])
def auc_list(request, pk=''):
    if pk:
        try:
            auc = Auction.objects.get(id=pk)
        except Auction.DoesNotExist:
            return HttpResponse(status=404)

        if request.method == 'GET':
            serializer = AuctionSerializer(auc)
            return JSONResponse(serializer.data)
    else:
        if request.method == 'GET':
            auc = Auction.objects.all()
            serializer = AuctionSerializer(auc, many=True)
            return JSONResponse(serializer.data)





class AuthView(APIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Auction.objects.get(pk=pk)
        except Auction.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        auc = self.get_object(pk)
        serializer = AuctionSerializer(auc)
        return Response(serializer.data)