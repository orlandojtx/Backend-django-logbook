"""backend_logbook URL Configuration

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
from django.contrib                 import admin
from django.urls                    import path
from logbook_app                    import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bitacora/create/', views.LogbookCreateView.as_view()),
    path('bitacora/<str:user>/', views.LogbookDetailView.as_view()),
    path('entrada/create/', views.EntryCreateView.as_view()),
    path('entrada/<str:logbook>/', views.EntryDetailView.as_view()),
    path('entrada/get/<int:pk>/', views.EntrySingleDetailView.as_view()),
    path('entrada/update/<int:pk>/', views.EntryUpdateView.as_view()),
    path('entrada/remove/<int:pk>/', views.EntryDeleteView.as_view()),
]
