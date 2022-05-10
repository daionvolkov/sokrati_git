from django.contrib import admin
from django.urls import path, include
from links import views as linksViews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('link/', linksViews.LinksView.as_view(), name='links'),


]
