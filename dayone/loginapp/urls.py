from django.urls import path
from . import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',user_views.index,name='index'),
    path('register/',user_views.RegisterUser,name="register"),
    path('login/',auth_views.LoginView.as_view(template_name = 'users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'users/logout.html'),name='logout'),
    path('home/',user_views.home,name='home'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name = 'Email/password_reset.html'),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name = 'Email/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name = 'Email/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name = 'Email/password_reset_complete.html'),name='password_reset_complete'),
    path('profile/',user_views.profile,name='profile'),
    path('gallery/',user_views.gallery,name='gallery'),
    path('upload_gallery/',user_views.gallery_upload,name='upload_gallery'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 