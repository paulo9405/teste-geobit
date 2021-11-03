from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.api.viewsets import MulherViewSet, PessoaViewSet
from core.api.viewsets import geobit, upload_file

router = routers.DefaultRouter()
router.register(r'lista_mulheres', MulherViewSet, basename='lista_mulheres')
router.register(r'lista_pessoas', PessoaViewSet)

urlpatterns = [
    path('geobit', geobit, name='core_geobit'),
    path('upload', upload_file, name='upload_file'),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
