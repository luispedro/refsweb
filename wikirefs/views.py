# -*- coding: utf-8 -*-
# Copyright (C) 2009 Luís Pedro Coelho <lpc@cmu.edu>
# Part of refsweb
# License: GNU Affero GPL version 3 or later (see LICENSE file)
from __future__ import division, with_statement
from django.http import HttpResponse
from django.shortcuts import render_to_response
from .models import BibTexEntry

def get_doi(request, doi, format):
    '''
    get_doi

    Lookup a reference based on its DOI.
    '''
    if format != 'bibtex':
        r = HttpResponse()
        r.write('Sorry mate, I only know how to display in BibTeX')
        return r
    results = BibTexEntry.objects.filter(doi=doi)
    if not results:
        r = HttpResponse()
        r.write('<p>Sorry mate, not found.')
        return r
    if len(results) > 1:
        r = HttpResponse()
        r.write('<p>Sorry mate, this is all very confusing.</p>')
        return r
    b = results[0]
    bibvalues = b.__dict__.items()
    return render_to_response('wikirefs/templates/bibtex.html',
        {
            'bibtype' : 'article',
            'bibcode' : 'wikirefs_download',
            'bibentries' : bibvalues,
        })


