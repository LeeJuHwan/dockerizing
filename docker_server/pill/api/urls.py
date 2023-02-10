from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
 
app_name = "api"
 
urlpatterns = [
    path('', views.upload_file, name = 'index'),
    path('<int:user_id>/', views.show_image, name = 'result')
]
 
if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )