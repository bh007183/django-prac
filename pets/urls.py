from django.urls import path, include
from . import views
from rest_framework import routers
router = routers.SimpleRouter()
router.register(r'userprofile', views.UserProfileViewSet)

urlpatterns = router.urls
urlpatterns = [
    path("", include(router.urls)),
    # path("userprofile/<int:pk>/", views.UserProfileDetailView.as_view())
]