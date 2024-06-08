from django.urls import include, path
from rest_framework.routers import DefaultRouter
from firstDjangoApp.views import BlogPostViewSet

router = DefaultRouter()
router.register(r'blogposts', BlogPostViewSet)

urlpatterns = [
	path('', include(router.urls)),
]