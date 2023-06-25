from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from profiles.views import (
    UserLoginView,
    UserLogoutView,
    UserRegistrationView,
    profile_view,
    profile_edit,
    pattern_upload,
    pattern_list,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profiles/login/', UserLoginView.as_view(), name='login'),
    path('profiles/logout/', UserLogoutView.as_view(), name='logout'),
    path('profiles/register/', UserRegistrationView.as_view(), name='register'),
    path('profiles/profile/', profile_view, name='profile'),
    path('profiles/profile/edit/', profile_edit, name='profile_edit'),
    path('profiles/pattern/upload/', pattern_upload, name='pattern_upload'),
    path('profiles/patterns/', pattern_list, name='pattern_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
