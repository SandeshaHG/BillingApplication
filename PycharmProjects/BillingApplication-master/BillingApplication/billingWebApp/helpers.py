from . import models
from . import serializers
def createOrderItem(orderObj,items):
    for its in items:
        orderItemObj=models.orderItem.objects.create(
            orderId=orderObj.orderId,
            itemId=its
        )

def calculateTotalSubCost(items):
    returnCost=0
    for its in items:
        itemObj=models.item.objects.get(itemId=its)
        returnCost = returnCost + itemObj.itemCostinINR
    return returnCost


def calculateTotalGST(items):
    returnGSTCost=0
    for its in items:
        itemObj = models.item.objects.get(itemId=its)
        category=itemObj.category
        gstSlab=category.gstSlab
        slabPercentage=gstSlab.slabPercentage
        returnGSTCost= returnGSTCost + (itemObj.itemCostinINR)*slabPercentage
    return returnGSTCost


