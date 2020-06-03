from django.urls import include, path
from blogging.views import list_view, detail_view, PostViewSet
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'post', PostViewSet)

urlpatterns = [
    path("", list_view, name="blog_index"),
    path("api/", include(router.urls)),
    path("posts/<int:post_id>/", detail_view, name="blog_detail"),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
]
