from django.contrib import admin
from django.urls import path, include, re_path
from products.views import ProductAPIList, ProductAPIDestroy, ProductAPIUpdate, GroupAPIList, GroupAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'product', ProductViewSet)
# print(router.urls)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),# session
    # path('api/v1/', include(router.urls)), /api/v1/product/
    path('api/v1/group/', GroupAPIList.as_view()),
    path('api/v1/group/<int:pk>/', GroupAPIView.as_view()),
    path('api/v1/product/', ProductAPIList.as_view()),
    path('api/v1/product/<int:pk>/', ProductAPIUpdate.as_view()),
    path('api/v1/productdelete/<int:pk>/', ProductAPIDestroy.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/v1/token/', TokenObtainPairView.as_view, name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view, name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view, name='token_verify'),
]
