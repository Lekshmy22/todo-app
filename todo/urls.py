"""
URL configuration for todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.SignUpView.as_view(),name='signup'),
    path('',views.SignInView.as_view(),name='signin'),
    path('todo/add/',views.TodoCreateView.as_view(),name='todo-add'),
    path('todo/details/',views.TodoDetailsView.as_view(),name='todo-list'),
    path('todo/<int:pk>/change/',views.TodoUpdateView.as_view(),name='todo-edit'),
    path('todo/<int:pk>/remove/',views.TodoDeleteView.as_view(),name='todo-delete'),
    path('signout/',views.SignOutView.as_view(),name='signout'),
    path('todo/status/',views.TodoCompletedView.as_view(),name='todo-status'),
    path('todo/index/',views.TodoIndexView.as_view(),name="todo-index"),
]
