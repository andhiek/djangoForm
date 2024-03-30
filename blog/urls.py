from django.urls import re_path


from . import views


app_name = 'blog'
urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^category/(?P<categoryInput>[\w ]+)/$',
            views.categoryPost, name='category'),
    re_path(r'^detail/(?P<slugInput>[\w-]+)/$',
            views.detailPost, name='detail'),
]
