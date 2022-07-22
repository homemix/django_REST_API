from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'book', views.BookViewSet)
router.register(r'review', views.ReviewSerializer)
router.register(r'genre', views.GenreSerializer)

urlpatterns = [
    path('', include(router.urls)),
]
