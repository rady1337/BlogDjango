from django.urls import path
from .views import BlogListView, AboutListView

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('about/', AboutListView.as_view(), name='about')
]