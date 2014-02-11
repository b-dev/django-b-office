from django.conf.urls import patterns, url, include
from django.contrib.auth import views as auth_views
from django.core.urlresolvers import reverse_lazy

from boffice.core.application import Application

#from oscar.apps.customer import forms
from boffice.core.loading import get_class
from boffice.views.decorators import login_forbidden


class Shop(Application):
    name = None

    cliente_app = get_class('cliente.app', 'application')

    def get_urls(self):
        urlpatterns = patterns('',
            (r'^i18n/', include('django.conf.urls.i18n')),
            (r'^clienti/', include(self.cliente_app.urls)),

            # Password reset - as we're using Django's default view functions,
            # we can't namespace these urls as that prevents
            # the reverse function from working.
            # url(r'^password-reset/$',
            #     login_forbidden(auth_views.password_reset),
            #     {'password_reset_form': forms.PasswordResetForm,
            #      'post_reset_redirect': reverse_lazy('password-reset-done')},
            #     name='password-reset'),
            # url(r'^password-reset/done/$',
            #     login_forbidden(auth_views.password_reset_done),
            #     name='password-reset-done'),
            # url(r'^password-reset/confirm/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            #     login_forbidden(auth_views.password_reset_confirm),
            #     {'post_reset_redirect': reverse_lazy('password-reset-complete')},
            #     name='password-reset-confirm'),
            # url(r'^password-reset/complete/$',
            #     login_forbidden(auth_views.password_reset_complete),
            #     name='password-reset-complete'),
            # (r'', include(self.promotions_app.urls)),
        )
        return urlpatterns


# 'shop' kept for legacy projects - 'application' is a better name
application = Shop()
