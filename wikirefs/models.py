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
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models import *
from django.utils.translation import ugettext_lazy as tr
import djapian

class BibTexEntry(Model):
    title = CharField(tr(u'Title'), max_length=512)
    author = CharField(tr(u'Authors'), max_length=256)
    year = CharField(tr(u'Year'), max_length=16)
    month = CharField(tr(u'Month'), max_length=16)
    pages = CharField(tr(u'Pages'), max_length=32)
    doi = CharField(tr(u'DOI'), max_length=128)
    url = CharField(tr(u'url'), max_length=128)

class BibTexEntryIndexer(djapian.Indexer):
    fields=[]
    tags=[
        ('title','title'),
        ('author','author')
        ]
    def trigger(self,obj):
        return True

djapian.add_index(BibTexEntry, BibTexEntryIndexer, attach_as='indexer')

class BibTexField(Model):
    entry = ForeignKey(BibTexEntry)
    name = CharField('name', max_length=64)
    value = CharField('value', max_length=256)

class Revision(Model):
    entry = ForeignKey(BibTexEntry)
    editor = ForeignKey(User, verbose_name=tr(u'Editor'), null=True)
    editor_ip = IPAddressField(tr(u"IP Address of the Editor"))
    revision = IntegerField(tr(u"Revision Number"))
    modified = DateTimeField(tr(u"Modified at"), default=datetime.datetime.now)
    reverted = BooleanField(tr(u"Reverted Revision"), default=False)


class RevisionEntry(Model):
    '''
    This saves the *previous* values, i.e.,
    those *before* the revision.
    '''
    revision = ForeignKey(Revision)
    fieldname = CharField(tr(u'Field Name'), max_length=64)
    fieldvalue = CharField(tr(u'Field Value'), max_length=512)

# vim: set ts=4 sts=4 sw=4 expandtab smartindent:
