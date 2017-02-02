from django.conf.urls import patterns, include, url
from django.contrib import admin
# from yaas_app.views import HelloTemplate
import yaas_app

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^auction/$', 'yaas_app.views.a'),
                       url(r'^auction/get/(?P<b_id>\d+)/$', 'yaas_app.views.b'),

                       url(r'^auction/search/$', 'yaas_app.views.search_auction'),

                        # for user
                       url(r'^auction/auth/$', 'yaas_app.views.auth_view'),
                       url(r'^login/$', 'yaas_app.views.login'),
                       url(r'^logout/$', 'yaas_app.views.logout'),
                       url(r'^edituser/$', 'yaas_app.views.edit_user'),
                       #url(r'^auction/loggedin/$', 'yaas_app.views.loggedin'),
                       url(r'^auction/invalid/$', 'yaas_app.views.invalid_login'),
                       url(r'^register/$', 'yaas_app.views.register_user'),
                       url(r'^auction/register_success/$', 'yaas_app.views.register_success'),

                        # for auction
                       url(r'^auction/create/$', 'yaas_app.views.create_auction'),
                       url(r'^auction/edit/(?P<id>\d+)/$', 'yaas_app.views.edit_auction'),
                       url(r'^auction/bid/(?P<id>\d+)/$', 'yaas_app.views.bid_acution'),
                       url(r'^auction/search/$', 'yaas_app.views.search_auction'),
                       url(r'^auction/saveauction/$', 'yaas_app.views.save_auction'),

                       url(r'^banauction/(?P<id>\d+)/$', 'yaas_app.views.ban_acution'),
                       url(r'^language/(?P<lang>\w+)/$', 'yaas_app.views.language'),



                       (r'^api/auc/$',                                 'yaas_app.rest_views.auc_list'),
                        (r'^api/auc/(?P<pk>\d+)/$',                     'yaas_app.rest_views.auc_list'),


                       url(r'^admin/', include(admin.site.urls)),

                       )
