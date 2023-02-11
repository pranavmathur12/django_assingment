from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from excel_upload.views import ProductViewSet

router = routers.SimpleRouter()
router.register("products", ProductViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]


