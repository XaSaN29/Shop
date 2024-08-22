"""
URL configuration for root project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps.views import (
PraductListView, PraductDetaiView, AuthWizardView,
AuthCardConfirmView, AuthCardForgotView, AuthCardLockView,
AuthCardLoginView, AuthCardLogoutView, AuthCardRegisterView,
AuthCardResetView, UserProfile, UserSettings,
WishlistView, WishlistCreateView
)
from root import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', PraductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', PraductDetaiView.as_view(), name='product'),
    path('like/<int:pk>/', WishlistCreateView.as_view(), name='like'),
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
    
    path('wizard/', AuthWizardView.as_view(), name='wizard'),
    path('confirm/', AuthCardConfirmView.as_view(), name='confirm'),
    path('forgot/', AuthCardForgotView.as_view(), name='forgot'),
    path('lock/', AuthCardLockView.as_view(), name='lock'),
    
    path('login/', AuthCardLoginView.as_view(), name='login'),
    path('logout/', AuthCardLogoutView.as_view(), name='logout'),
    path('register/', AuthCardRegisterView.as_view(), name='register'),
    path('reset/', AuthCardResetView.as_view(), name='reset'),
    
    path('profil/', UserProfile.as_view(), name='profil'),
    path('profil-settings/', UserSettings.as_view(), name='profil-settings')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)