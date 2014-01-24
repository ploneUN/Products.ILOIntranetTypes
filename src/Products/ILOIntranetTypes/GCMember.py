# -*- coding: utf-8 -*-
#
# File: GCMember.py
#
# Copyright (c) 2011 by unknown <unknown>
# Generator: ArchGenXML Version 2.6
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'

#GCMember

from AccessControl import ClassSecurityInfo
from Acquisition import aq_base

from Products.CMFCore.utils import getToolByName

from Products.Archetypes.Field import ObjectField,encode,decode
from Products.Archetypes.Registry import registerField
from Products.Archetypes.utils import DisplayList
from Products.Archetypes import config as atconfig
from Products.Archetypes.Widget import *
from Products.Archetypes.Field  import *
from Products.Archetypes.Schema import Schema


from Products.ILOIntranetTypes import config

##code-section module-header #fill in your manual code here
##/code-section module-header

from zope.interface import implements

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin



from Products.CompoundField.CompoundField import CompoundField
######CompoundField
schema = Schema((

    StringField(
        name='gc_name',
        widget=StringField._properties['widget'](
            label="Name",
            label_msgid='ILOIntranetTypes_label_gc_name',
            i18n_domain='ILOIntranetTypes',
        ),
    ),
    StringField(
        name='gc_type',
        widget=MultiSelectionWidget(
            label="Type",
            format="select",
            description="Please select member type. Hold down CTRL for multiple selections.",
            label_msgid='ILOIntranetTypes_label_gc_type',
            description_msgid='ILOIntranetTypes_help_gc_type',
            i18n_domain='ILOIntranetTypes',
        ),
        vocabulary=['Government: Regular Member','Government: Deputy Member','Employer: Regular Member','Employer: Deputy Member','Employer: Subsitute','Worker: Regular Member','Worker: Deputy Member','Worker: Substitute'],
    ),

),
)




class GCMember(CompoundField):
    """
    """
    ##code-section class-header #fill in your manual code here
    ##/code-section class-header



    _properties = CompoundField._properties.copy()
    _properties.update({
        'type': 'gcmember',
        ##code-section field-properties #fill in your manual code here
        ##/code-section field-properties

        })

    security  = ClassSecurityInfo()

    schema=schema

    security.declarePrivate('set')
    security.declarePrivate('get')


    def getRaw(self, instance, **kwargs):
        return CompoundField.getRaw(self, instance, **kwargs)

    def set(self, instance, value, **kwargs):
        return CompoundField.set(self, instance, value, **kwargs)

    def get(self, instance, **kwargs):
        return CompoundField.get(self, instance, **kwargs)


registerField(GCMember,
              title='GCMember',
              description='')

##code-section module-footer #fill in your manual code here
##/code-section module-footer

