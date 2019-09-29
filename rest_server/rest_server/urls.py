from django.conf.urls import url,include
from django.contrib import admin
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from sensor import views
import sensor.api

app_name='sensor'

router=routers.DefaultRouter()
router.register('sensors',sensor.api.SensorViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/doc', get_swagger_view(title='Rest API Document')),
    url(r'^predict/premaintenance/', include((router.urls, 'sensor'), namespace='predict')),
    url(r'^predict/premaintenance', views.predict)
]

# /predict/premaintenance