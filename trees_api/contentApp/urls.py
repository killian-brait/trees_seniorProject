# contentApp/urls.py

from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'contents', views.ContentViewSet)
router.register(r'videos', views.VideoViewSet)
router.register(r'steps', views.StepViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path(r'api-auth/', include('rest_framework.urls',
                                 namespace='rest_framework'))
]

