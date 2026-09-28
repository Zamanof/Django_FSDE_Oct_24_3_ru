# from django.contrib import admin
from django.urls import path, include

from notes import views as notes_views

urlpatterns = [
    #    path('admin/', admin.site.urls),
    path('', notes_views.index, name='home'),
    path('about/', notes_views.about, name='about'),
    path('notes/', include('notes.urls')),
    path('accounts/', include('accounts.urls')),

]
