from billingWebApp import viewsets
from rest_framework import routers

router=routers.DefaultRouter()
router.register('user',viewsets.userViewSet)
router.register('item',viewsets.itemViewSet)
router.register('category',viewsets.categoryViewSet)
router.register('gstslab',viewsets.gstSlabViewSet)
router.register('order',viewsets.orderViewSet)
router.register('orderItem',viewsets.orderItemViewSet)
router.register('payment',viewsets.paymentViewSet)



