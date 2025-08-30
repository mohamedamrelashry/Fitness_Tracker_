from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ActivityViewSet
from rest_framework.authtoken import views as drf_auth_views

router = DefaultRouter()
router.register(r'activities', ActivityViewSet, basename='activity')

urlpatterns = [
    path('', include(router.urls)),
    path('token-auth/', drf_auth_views.obtain_auth_token, name='api_token_auth'),
]
