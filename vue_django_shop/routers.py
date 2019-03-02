from rest_framework import routers
from basket.viewsets import PhotoViewSet, ProductViewSet, BasketViewSet
router = routers.DefaultRouter()

router.register(r'products', ProductViewSet)
router.register(r'photos', PhotoViewSet)
router.register(r'baskets', BasketViewSet)