from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from disciplina.views import listar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('disciplina.urls')),
    path('user/', include('user.urls')),
    path('professor/', include('professor.urls')),
    #path('disciplina/', include('disciplina.urls')),
    #path('accounts/', listar),
    #path('accounts/', include('django.contrib.auth.urls')),
    #path('login/', include('django.contrib.auth.urls'), name='login')



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
