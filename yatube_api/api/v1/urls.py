from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router_v1 = DefaultRouter()
router_v1.register(r'posts', PostViewSet)
router_v1.register(r'groups', GroupViewSet)
router_v1.register(r'follow', FollowViewSet, basename='followers')
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
    basename='comment')

urlpatterns = [
    path('', include(router_v1.urls)),
    path('', include('djoser.urls.jwt')),
]
