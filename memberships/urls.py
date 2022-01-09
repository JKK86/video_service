from django.urls import path
from . import views

urlpatterns = [
    path('', views.MembershipListView.as_view(), name="select_membership"),
]
