"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import include
import debug_toolbar
from habit_tracker import views as habit_tracker_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('add_habit/', habit_tracker_views.add_habit, name="add_habit"),
    path('', habit_tracker_views.home, name='home'),
    path('<int:pk>/delete_habit/', habit_tracker_views.delete_habit, name='delete_habit'),
    path('<int:pk>/edit_habit/', habit_tracker_views.edit_habit, name='edit_habit'),
]
