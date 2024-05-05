from django.urls import path
from .views import DisplayListView

urlpatterns = [
        path("", DisplayListView.as_view(), name="index")
]
