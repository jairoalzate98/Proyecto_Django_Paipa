from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'estratos', views.EstratosViewSet, basename='estratos')
router.register(r'animales', views.AnimalesViewSet, basename='animales')
router.register(r'animalesVacunados', views.AnimalesVacunadosViewSet, basename='animales')


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]