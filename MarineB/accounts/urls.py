from django.urls import path
from . import views


urlpatterns = [
    path('checkout', views.checkout,name="checkout"),
    
    path('success/', views.success,name="success"),  
    
    path('webhooks/stripe/', views.webhook, name='webhook'),

    
    path('create-payment-intent', views.StripeIntentView.as_view(), name='create-payment-intent'),


]
