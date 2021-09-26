from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register("cart", ShoppingCartAPI, basename="cart")
router.register("articles", ArticleAPI, basename="articles")
urlpatterns = [
    path("crud/", include(router.urls))
]
