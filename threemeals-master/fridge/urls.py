from django.contrib import admin
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings


from fridge.views import *
#
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'ingredients', IngredientViewSet)

urlpatterns=[
    url(r'^$', FridgeHomeView.as_view(), name='recommendation'),
    url(r'^ingredient/$', IngredientHomeView.as_view(), name='ingredient'),
    url(r'^scrap/$', ScrapHomeView.as_view(), name="scrap"),
    url(r'^shopping/$', ShoppingHomeView.as_view(), name="shopping"),
    url(r'^ingredient/add/$', AddIngredient.as_view(), name="addinng"),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]