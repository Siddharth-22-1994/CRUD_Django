from . import views
from django.urls import path

urlpatterns = [
    path('', views.empbase, name='empdet'),
    path('newemp/', views.createemp, name='createemp'),
    path('update/<emp_id>', views.Update_emp, name='update'),
    path('delete/<emp_id>', views.delete_emp, name='delete')
]