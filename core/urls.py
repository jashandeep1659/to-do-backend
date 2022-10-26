from .views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", Todo_ViewSet, basename="todo")
urlpatterns = [
    path("", include(router.urls)),
]
