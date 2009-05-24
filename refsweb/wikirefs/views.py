# -*- coding: utf-8 -*-
# Copyright (C) 2009 Luís Pedro Coelho <lpc@cmu.edu>
# Part of refsweb
# License: GNU Affero GPL version 3 or later (see LICENSE file)
from __future__ import division, with_statement
from django.http import HttpResponse
from django.shortcuts import render_to_response
from .models import BibTexEntry

def _wrong_format(format):
    r = HttpResponse()
    r.write('Sorry mate, I only know how to display in BibTeX+html')
    return r


def get_doi(request, doi, format):
    '''
    get_doi

    Lookup a reference based on its DOI.
    '''
    if format != 'bibtex+html':
        return _wrong_format(format)
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



def search(request, query, format):
    '''
    search(request, query, format)

    Lookup a reference based on the full text.
    '''
    if format != 'bibtex+html':
        return _wrong_format(format)
    results = BibTexEntry.indexer.search(query)
    if not results:
        r = HttpResponse()
        r.write('<p>Sorry mate, not found.')
        return r
    b = results[0]
    bibvalues = b.__dict__.items()
    return render_to_response('wikirefs/templates/bibtex.html',
        {
            'bibtype' : 'article',
            'bibcode' : 'wikirefs_download',
            'bibentries' : bibvalues,
        })



