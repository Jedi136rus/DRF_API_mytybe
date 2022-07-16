from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views

urlpatterns = [
    path('posts/', views.APIPosts.as_view()),
    path('posts/<int:pk>/', views.APIPostDetails.as_view()),
    path('posts/<int:pk>/comments/', views.APIPostComments.as_view()),
    path('posts/<int:pk>/comments/<int:comment_id>/', views.APIPostCommentsDetails.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
