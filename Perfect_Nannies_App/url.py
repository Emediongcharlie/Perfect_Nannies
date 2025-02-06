from django.urls import path

from Perfect_Nannies_App.views import NannyRegistrationViewSet, GuardianRegistrationViewSet, NannyLoginViewSet, \
    GuardianLoginViewSet

urlpatterns = [
    path('api/register-nanny', NannyRegistrationViewSet.as_view(), name='register-nanny'),
    path('api/register-guardian', GuardianRegistrationViewSet.as_view(), name='register-guardian'),
    path('login-nanny/', NannyLoginViewSet.as_view(), name="login-nanny"),
    path('login-guardian/', GuardianLoginViewSet.as_view(), name="login-guardian")
]