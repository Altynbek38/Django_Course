from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('register/', views.register, name="register"),
    path('profile/<int:id>/', views.profile_view, name="profile_view"),
    path('profile/<int:id>/edit/', views.profile_edit, name="profile_edit"),
    path('profile/<int:id>/follow/', views.follow_user, name="follow_user"),
    path('profile/<int:id>/unfollow/', views.unfollow_user, name="unfollow_user"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)