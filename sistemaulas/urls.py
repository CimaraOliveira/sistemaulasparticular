from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from disciplina.disciplina_service import listarDisciplina
from professor.professor_service import  listarProfesor
from user.user_service import listarUsuario, listarReservasUsuario,UsuariosViewSet
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view


router = routers.DefaultRouter()
router.register(r'disciplina', listarDisciplina)
router.register(r'professor', listarProfesor)
router.register(r'user', listarUsuario)
router.register(r'userDisciplina', listarReservasUsuario)
router.register(r'cadastrar_usuario', UsuariosViewSet)

schema_view = get_swagger_view(title='API Sistema de Aulas Particulares')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('disciplina.urls')),
    path('user/', include('user.urls')),
    path('professor/', include('professor.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('api/',include(router.urls)),
    #path('apii/', include('rest_framework.urls')),
    path('swagger/', schema_view),
    path('relatorio/',include('relatorio.urls')),


    path('rest_auth/', include('rest_auth.urls')),
    #path('registration/',include('rest_auth.registration.urls'))


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
