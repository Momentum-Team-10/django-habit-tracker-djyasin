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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
import debug_toolbar
from habit_tracker import views as habit_tracker_views
from api import views as api_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('add_habit/', habit_tracker_views.add_habit, name="add_habit"),
    path('habit_library/', habit_tracker_views.habit_library, name="habit_library"),
    path('', habit_tracker_views.home, name='home'),
    path('delete_habit/<int:pk>/', habit_tracker_views.delete_habit, name='delete_habit'),
    path('edit_habit/<int:pk>/', habit_tracker_views.edit_habit, name='edit_habit'),
    path('add_record/<int:pk>/', habit_tracker_views.add_record, name='add_record'),
    path('habit_detail/<int:pk>', habit_tracker_views.habit_detail, name='habit_detail'),
    path('accounts/', include('registration.backends.simple.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/habit_library',api_views.HabitLibraryView.as_view(), name="api_habit_library"),
    path('api/habit_detail/<int:pk>',api_views.HabitDetailView.as_view(), name="api_habit_detail"),
    path('api/create_habit', api_views.CreateHabitView.as_view(), name='api_create_habit'),
    path('api/delete_habit/<int:pk>', api_views.DeleteHabitView.as_view(), name='api_delete_habit'),
    
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]