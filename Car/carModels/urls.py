from django.urls import path,include
from django.urls.resolvers import URLPattern
from .views import CarCreateAPIView
from . import views
app_name = "carModels"


urlpatterns=[
      path('carList/' , views.CarListAPIView.as_view(), name="carList"),
      path('carUpdate/<int:pk>', views.CarUpdateAPIView.as_view(), name="carUpdate"),
      path('carRetrieve/<int:pk>' , views.CarRetrieveAPIView.as_view(), name="carRetrieve"),
      path('carCreate/',views.CarCreateAPIView.as_view(), name="carCreate"),
      path('carDelete/<int:pk>' , views.CarDeleteAPIView.as_view(), name="carDelete"),
]
