# -*- coding: utf-8 -*-
# Copyright (C) 2009 Luís Pedro Coelho <lpc@cmu.edu>
# Part of refsweb
# License: GPL 2 or later (see LICENSE file)
from __future__ import division, with_statement

from django.conf.urls.defaults import *

urlpatterns = patterns('wikirefs',
    (r'^$', 'index.index'),
    (r'^doi/$', 'views.get_doi'),
)

