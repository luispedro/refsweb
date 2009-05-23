# -*- coding: utf-8 -*-
# Copyright (C) 2009 Luís Pedro Coelho <lpc@cmu.edu>
# Part of refsweb
# License: GNU Affero GPL version 3 or later (see LICENSE file)
from __future__ import division, with_statement

from django.conf.urls.defaults import *
from django.contrib import admin
import models
admin.autodiscover()
admin.site.register(models.BibTexEntry)

urlpatterns = patterns('wikirefs',
    (r'^$', 'index.index'),
    (r'^doi/(.*)/(.*)$', 'views.get_doi'),
    (r'^admin/(.*)', admin.site.root),
)

