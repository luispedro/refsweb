# -*- coding: utf-8 -*-
# Copyright (C) 2009 Luís Pedro Coelho <lpc@cmu.edu>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published
# by the Free Software Foundation; either version 2 of the License,
# or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.

from __future__ import division, with_statement
from django.http import HttpResponse

def get_doi(request):
    '''
    get_doi

    Lookup a reference based on its DOI.
    '''
    r = HttpResponse()
    if request.GET and 'doi' in request.GET:
        doi = request.GET['doi'] 
        r.write('<h1>Query</h1><p>You looked for doi:%s.</p>' % request.GET['doi'])
    else:
        r.write('<h1>Hello, world.</h1><p>No GET')
    return r


