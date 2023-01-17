from django.contrib import admin
from django.urls import path, include
from myapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='url_index'),
    path('crud/', crud, name='url_crud'),
    path('createP/', createP, name='url_createP'),
    path('deleteProfessor/<int:id>/', delP, name='url_delP'),
    path('apdateProfessor/<int:id>/', updateP, name='url_updateP'),
    path('consulta/', consulta, name='url_consulta'),
    path('listagem/', listagem, name='url_listagem'),
    path('sobre/', sobre, name='url_sobre'),
    path('account/', include('django.contrib.auth.urls')),
]
