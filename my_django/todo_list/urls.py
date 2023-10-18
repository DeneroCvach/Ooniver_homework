from django.urls import path
from todo_list.views import index, create_todo

urlpatterns = [
    path('', index, name='index_todo'),
    path('create-todo', create_todo, name='create-todo'),

]
