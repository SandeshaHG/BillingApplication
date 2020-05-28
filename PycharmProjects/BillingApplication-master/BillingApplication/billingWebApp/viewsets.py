from rest_framework import viewsets
from . import models
from . import serializers

class gstSlabViewSet(viewsets.ModelViewSet):
    queryset = models.gstSlab.objects.all()
    serializer_class=serializers.gstSlabSerializer

class categoryViewSet(viewsets.ModelViewSet):
    queryset = models.category.objects.all()
    serializer_class = serializers.categorySerializer


class itemViewSet(viewsets.ModelViewSet):
    queryset = models.item.objects.all()
    serializer_class = serializers.itemSerializer


class userViewSet(viewsets.ModelViewSet):
    queryset = models.user.objects.all()
    serializer_class = serializers.userSerializer

class orderViewSet(viewsets.ModelViewSet):
    queryset = models.order.objects.all()
    serializer_class=serializers.orderSerializer

class orderItemViewSet(viewsets.ModelViewSet):
    queryset = models.orderItem.objects.all()
    serializer_class = serializers.orderItemSerializer

class paymentViewSet(viewsets.ModelViewSet):
    queryset = models.payment.objects.all()
    serializer_class = serializers.paymentSerializer


