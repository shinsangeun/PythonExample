from django.contrib import admin
from rest_framework import routers
from sensor import views
import sensor.api
from django.urls import path

app_name='sensor'

router=routers.DefaultRouter()
router.register('sensors',sensor.api.SensorViewSet)

urlpatterns = [
    path('admin/',admin.site.urls),
    path('predict/premaintenance', views.predict),
    path('predict/acceler', views.acceler)
]