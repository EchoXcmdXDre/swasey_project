from django.urls import path
from apartments import views as apartments_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #path('', apartments_views.index, name='home'),
    path('', apartments_views.index.as_view(), name='home'),
    path('api/apartments/', apartments_views.apartment_list),
    path('api/apartments/<int:pk>/', apartments_views.apartment_detail),
    path('api/apartments/published/', apartments_views.apartment_list_published)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)