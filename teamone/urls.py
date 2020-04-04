from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url



router = DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name ='index'),
    path('zwierzaki', views.ZwierzetaLista.as_view()),
    path('zwierzaki/<int:pk>', views.ZwierzetaDetail.as_view()),
    path('zfiltr/<str:filtr>', views.ZwierzetaFiltry.as_view()),
    url(r'^accounts/', include('accounts.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)