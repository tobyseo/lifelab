from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^point/', include('happy.urls',
                            namespace='happy',
                            app_name='happy')),
]
