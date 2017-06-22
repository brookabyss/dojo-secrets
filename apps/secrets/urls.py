from django.conf.urls import url,include
from . import views2
from ..reg import views1


urlpatterns = [
    url(r'^$', views1.index ,name="login_reg"),
    url(r'^secrets$', views2.show, name='secrets'),
    url(r'^secrets/new_post$', views2.create_post, name='create_post'),
    url(r'^secrets/(?P<post_id>\d+)/like$', views2.like, name='like'),
    url(r'^secrets/popular$', views2.popular, name='popular'),
    url(r'^secrets/delete_secret/(?P<post_id>\d+)$', views2.delete, name='delete_secret')
]
