from django.urls import path
from . import views

urlpatterns = {
    path ('',views.home, name='home'),
    path('proxpag/',views.contato,name='proxpag'),
}