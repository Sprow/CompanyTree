from django.conf.urls import url
from django.contrib import admin
from accounts.views import accounts, single_account

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', accounts, name="home"),
    url(r'^(?P<account_id>[\d]+)$', single_account, name="single_account"),
]
