from segmentationAPP import views, common
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    path(r"process", csrf_exempt(getattr(views,common.TARGET).Process)),
]

