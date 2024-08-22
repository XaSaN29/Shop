from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.views.generic import (
TemplateView, ListView, DetailView,
CreateView, FormView, View, 
UpdateView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product, ProductImage, User, Wishlist
from .form import UserRegisterForm, UserLoginForm, UserUpdateForm
from .mixins import NotLoginRequiredMixin
from django.urls import reverse_lazy
# from django.core.mail import send_mail

# Create your views here.

class PraductListView(ListView):
    template_name = 'product/products.html'
    model = Product
    context_object_name = 'Product'

    def get_queryset(self):
        qs = super().get_queryset()
        data = self.request.GET.get('search')
        if data is not None and len(data) > 0:
            qs = qs.filter(name__icontains=data)
        return qs

class PraductDetaiView(DetailView):
    template_name = 'product/product-details.html'
    model = Product

class AuthWizardView(TemplateView):
    template_name = 'auth/wizard.html'

class AuthCardConfirmView(TemplateView):
    template_name = 'auth/card/confirm-mail.html'

class AuthCardForgotView(TemplateView):
    template_name = 'auth/card/forgot-password.html'

class AuthCardLockView(TemplateView):
    template_name = 'auth/card/lock-screen.html'

class AuthCardLoginView(NotLoginRequiredMixin,FormView):
    form_class = UserLoginForm
    template_name = 'auth/card/login.html'
    success_url = '/'

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = User.objects.filter(username=username).first()
        if user is not None and user.check_password(password):
            login(self.request, user)
            return redirect('/')

        else:
            return redirect('register')

        return super().form_valid(form)

class AuthCardLogoutView(View):
    def get(self, request):
        logout(self.request)
        return redirect('login')
        

class AuthCardRegisterView(NotLoginRequiredMixin,CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'auth/card/register.html'
    success_url = '/'
    # send_mail(
    # "Subject here",
    # "Here is the message.",
    # "fatxuddinovx@gmail.com",
    # ["fatxuddinovxasan@gmail.com"],
    # fail_silently=False,
    # )


class AuthCardResetView(TemplateView):
    template_name = 'auth/card/reset-password.html'


class UserProfile(LoginRequiredMixin, TemplateView):
    template_name = 'user/profile.html'
    login_url = reverse_lazy('login')
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        user = self.request.user
        data['user'] = user
        return data

class UserSettings(UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'user/settings.html'
    success_url = reverse_lazy('profil')
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        user = self.request.user
        data['user'] = user
        return data
    
    def get_object(self, queryset=None):
        user = self.request.user
        return user
    

class WishlistCreateView(LoginRequiredMixin, View):
    def get(self,*args, **kwargs):
        user = self.request.user
        pk = self.kwargs.get('pk')
        product = Product.objects.filter(pk=pk).first()
        if user and pk :
            if not Wishlist.objects.filter(product=product).exists():
                Wishlist.objects.create(
                    user=user,
                    product=product 
                )
            else:
                wishlist = Wishlist.objects.filter(product=product).first()
                wishlist.delete()
        return redirect('/')
    

class WishlistView(ListView):
    model = Wishlist
    template_name = 'product/shopping-cart.html'
    context_object_name = 'wishlist'