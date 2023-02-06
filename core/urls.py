from django.urls import path
from . import views
urlpatterns = [
    path('',views.frontpage,name='frontpage'),
    path('product/',views.product,name='product'),
    path('productdetails/<str:pk>/',views.productdetails,name='productdetails'),
]
