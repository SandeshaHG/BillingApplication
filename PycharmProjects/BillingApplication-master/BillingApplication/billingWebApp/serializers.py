from rest_framework import serializers
from .models import user,order,item,gstSlab,category,payment,orderItem

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model=user
        fields='__all__'
class orderSerializer(serializers.ModelSerializer):
    class Meta:
        model=order
        fields='__all__'
class itemSerializer(serializers.ModelSerializer):
    class Meta:
        model=item
        fields='__all__'
class gstSlabSerializer(serializers.ModelSerializer):
    class Meta:
        model=gstSlab
        fields='__all__'
class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model=category
        fields='__all__'
class paymentSerializer(serializers.ModelSerializer):
    class Meta:
        model=payment
        fields='__all__'
class orderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=orderItem
        fields='__all__'