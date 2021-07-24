from django.urls import path,include
from products import views
from accounts import urls
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    #  path('', include('p.urls')),
    path('accounts/', include('accounts.urls')),

# ] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

