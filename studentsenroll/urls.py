from django.urls import path
from . import views

urlpatterns = [
    path('',views.show,name='Show'),
    path('delete/<int:id>/',views.deletedata,name='Deletedata'),
    path('<int:id>/',views.updatedata,name='Updatedata')


    
]
