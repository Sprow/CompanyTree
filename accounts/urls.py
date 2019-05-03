from django.conf.urls import url

from accounts.views import sign_out, sign_in, register_user, view_profile, edit_profile, change_password


urlpatterns = [
    url(r'^logout/$', sign_out, name="logout"),
    url(r'^login/$', sign_in, name="login"),
    url(r'^registration/$', register_user, name="registration"),

    url(r'^profile/$', view_profile, name='view_profile'),
    url(r'^profile/edit/$', edit_profile, name='edit_profile'),
    url(r'^change-password/$', change_password, name='change_password'),
]
