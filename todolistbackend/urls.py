
from django.contrib import admin
from django.urls import path
from todolist.views import login_View, Todo_View

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_View.as_view()),
    path('todos/', Todo_View.as_view())
]
