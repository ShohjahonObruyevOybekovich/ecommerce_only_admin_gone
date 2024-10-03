"""
URL configuration for khalifa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="E-commerce API",
      default_version='v1',
      description="Project documentation",

   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('auth/',include('account.urls')),
    path('api/', include('body.urls')),
    path('admin-api/',include('custom_admin.urls')),


    path('docs<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
from django.views.i18n import set_language

# urlpatterns_LANG = [
#     # Other URL patterns
#     path('set-language/', set_language, name='set_language'),
# ]
#
# urlpatterns+=urlpatterns_LANG
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)