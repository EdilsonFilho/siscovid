
from django.contrib import admin
from django.urls import path,include

from scheduling.urls import scheduling_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('scheduling', include(scheduling_urls)),

]
