from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list),
    path('Add/', views.AddUser,name='add'),
    path('Edit/<id>', views.EditUser, name='edit'),
    path('Delete/<eid>', views.DeleteUser, name='delete'),
    path('View/<eid>', views.ViewUser, name='view'),
]
