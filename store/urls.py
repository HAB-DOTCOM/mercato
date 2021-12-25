from django.urls import path
from .models import Product
from . import views

urlpatterns = [
    
    path('',views.store,name='store'),
    path('<slug:catagory_slug>/',views.store,name='product_by_catagory'),
    path('<slug:catagory_slug>/<slug:product_slug>/',views.product_detial,name='product_detial'),
    
]
#+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
