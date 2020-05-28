from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from .models import user,orderItem,order,category,payment,gstSlab,item
from . import serializers
from . import helpers
from django.shortcuts import render
from django.utils import timezone
from django.db import models

from django.core.exceptions import ObjectDoesNotExist
import json

@api_view(["POST"])
@csrf_exempt
def place_order(request):
    payload = json.loads(request.body)
    try:
        userObj=user.objects.get(userId=payload["userId"])
        orderObj = order.objects.create(
        user=userObj,
        orderDate = payload["date"],
        paymentMode = payload["mode"],
        orderSource = payload["source"]
        )
        helpers.createOrderItem(orderObj,payload["items"])
        subCost=helpers.calculateTotalSubCost(payload["items"])
        gst=helpers.calculateTotalGST(payload["items"])
        due=subCost+gst
        totalCost=subCost+gst

        paymentInvoice=payment.objects.create(
            orderId=orderObj.orderId,
            totalSubCost = subCost,
            totalGST = gst,
            totalCost = subCost+gst,
            totalPaid=0,
            totalDue=due,
            modeofPayment = orderObj.paymentMode,
            status = "PENDING"
        )
        items=[]
        for its in payload["items"]:
            itemsObj=item.objects.get(itemId=its)
            items.append(serializers.itemSerializer(itemsObj).data)
        return render(request,'invoice.html',{
            'userName' : userObj.name,
            'paymentId' : paymentInvoice.paymentId,
            'date' : orderObj.orderDate,
            'amountDue' : due,
            'totalSubCost' : subCost,
            'totalCost' : totalCost,
            'totalPaid' : 0,
            'items' : items

        })
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
