from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', views.home, name='home'),
    path('add_client/', views.add_client, name='add_client'),
    path('client_list/', views.client_list, name='client_list'),
    path('signin/', views.signin, name='signin'),
    path('add_campaign/', views.add_campaign, name='add_campaign'),
    path('campaign_list/', views.campaign_list, name='campaign_list')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

