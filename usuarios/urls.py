from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UsuarioCreate, ProfileUpdate, ProfileCreate, teste, alterar_senha
from . import views as v
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('registrar/', UsuarioCreate.as_view(),name='registrar'),
    path('login/', auth_views.LoginView.as_view(
        template_name='login.html'
    ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile-update/', ProfileUpdate.as_view(), name='profile-update'),
    path('profile-create/', ProfileCreate.as_view(), name='profile-create'),
    path('teste/', v.teste, name='teste'),
    path('password_reset/', v.MyPasswordReset.as_view(), name='password_reset'),
    path('password_reset/done/', v.MyPasswordResetDone.as_view(), name='password_reset_done'),
    path('alterar_senha/', v.alterar_senha, name='alterar_senha'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)