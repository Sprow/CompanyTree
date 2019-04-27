from django.conf.urls import url, include
from django.contrib import admin
from accounts.views import accounts, single_account, all_accounts, search

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', accounts, name="home"),
    url(r'^all_accounts/search', search, name="search"),
    url(r'^all_accounts', all_accounts, name="all_accounts"),
    url(r'^(?P<account_id>[\d]+)$', single_account, name="single_account"),

    url(r'^accounts/', include('accounts.urls')),
]
