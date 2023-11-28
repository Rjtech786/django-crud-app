from django.contrib import admin
from django.urls import path
from projectapp import views

urlpatterns = [
    path('translate', views.translate, name='translaror_app'),
    path('', views.index, name='home'),
    path('add', views.add, name='save_data'),
    path('edit',views.edit, name="edit"),
    path('update/<str:id>',views.update,name='delete'),
    path('delete/<str:id>',views.delete,name='delete'),

]