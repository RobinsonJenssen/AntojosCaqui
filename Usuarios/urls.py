from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register('users', APIUser)
router.register('doc_type', APIDocumentType)
router.register('profile', APIProfile)
router.register('country', APICountry)
router.register('state', APIState)
router.register('city', APICity)
router.register('address', APIAddress)
urlpatterns = [
    path('crud/', include(router.urls))
]
