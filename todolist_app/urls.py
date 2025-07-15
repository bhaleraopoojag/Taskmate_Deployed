from django.urls import path
from todolist_app import views

urlpatterns = [
    path('',views.todolist,name='todolist'),

    path('delete/<taskid>',views.deleteTask,name='deleteTask'),
    path('edit/<taskid>',views.editTask,name='editTask'),
    path('complete/<taskid>',views.completestatus,name='completestatus'),
    path('pending/<taskid>',views.pendingstatus,name='pendingstatus')
    
]
