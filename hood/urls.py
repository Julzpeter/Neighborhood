from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.home,name='home'),
    url(r'^profile/(\d+)$',views.profile,name='profile'),
    url(r'^update/profile/(\d+)$',views.update_profile,name='update_profile'),
    url(r'^join/(\d+)$', views.join, name='join'),
    url(r'^neighborhood/(\d+)$', views.neighborhood, name='neighborhood'),
    url(r'^business/(\d+)$', views.business, name='business'),
    url(r'^add/business/(\d+)$', views.add_business, name='add-business'),
    url(r'^post/(/d+)$',views.post,name='post'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^leave/$', views.leave, name='leave'),
]
