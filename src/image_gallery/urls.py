"""image_gallery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

#teste
from pages.views import home_view
from images.views import images_view
from contact.views import contact_create_view

#paginas utilizadas
from pages.views import index_view
from pages.views import about_view
from pages.views import code_view
from pages.views import solutions_view
from pages.views import faq_view


#static
from django.conf import settings
from django.conf.urls.static import static
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
	# TESTE
    # path('', home_view, name='home'), 
	path('images/', images_view, name='images'),
    path('contact/', contact_create_view, name='contact_form'),
    
    # a ser utilizado
    path('', index_view, name='home'),
    path('about/', about_view, name='about'),
    path('code/', code_view, name='code'),
    path('solutions/', solutions_view, name='solutions'),
    path('FAQ/', faq_view, name='faq'),
    path('admin/', admin.site.urls),
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)