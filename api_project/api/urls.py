from django.urls import path,include
from .views import BookList,BookViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('books',BookViewSet)


urlpatterns = [
    path('api-token-auth/', obtain_auth_token),
    path('',include(router.urls)),
    path('books/', BookList.as_view(),name='book_list'),
]

