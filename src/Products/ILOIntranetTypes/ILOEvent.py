# -*- coding: utf-8 -*-
#
# File: ILOEvent.py
#
# Copyright (c) 2011 by unknown <unknown>
# Generator: ArchGenXML Version 2.6
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
import interfaces

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.ATContentTypes.content.event import ATEvent
from Products.ATContentTypes.content.event import ATEventSchema
from Products.ILOIntranetTypes.config import *

# additional imports from tagged value 'import'
from Products.ILOIntranetTypes.ILOIntranetBase import ILOIntranetBase
from Acquisition import aq_parent
from Products.CMFCore.utils import getToolByName

##code-section module-header #fill in your manual code here
##/code-section module-header

copied_fields = {}
copied_fields['description'] = BaseSchema['description'].copy()
copied_fields['description'].required = True
copied_fields['description'].schemata = "default"
copied_fields['description'].widget.description = "Briefly describe this event."
copied_fields['office'] = ILOIntranetBase.schema['office'].copy()
copied_fields['office'].required = True
copied_fields['theme'] = ILOIntranetBase.schema['theme'].copy()
schema = Schema((

    copied_fields['office'],

    copied_fields['description'],

    LinesField(name='ilo_event_category',
                widget=SelectionWidget(
                    label="Category",
                    description="Select Meeting & Event category.",
                    label_msgid='ILOIntranetTypes_label_ilo_event_category',
                    description_msgid='ILOIntranetTypes_ilo_event_category_help',
                    i18n_domain='ILOIntranetTypes',
                ),
                vocabulary=["Internal Meeting","Staff Development","TC Project Meeting","Donor/UN Relations","Constituents Meeting","Regional Meeting"],
                multiValued=0,
            ),

    copied_fields['theme'],

    FileField(
        name='attachment_attendees',
        widget=FileField._properties['widget'](
            label="File Attachment 1",
            description="If you have a list of participants, an agenda or other supportive documentation click browse and select the file to be uploaded.",
            label_msgid='ILOIntranetTypes_label_attachment_attendees',
            description_msgid='ILOIntranetTypes_help_attachment_attendees',
            i18n_domain='ILOIntranetTypes',
        ),
        storage=AttributeStorage(),
        searchable=1,
    ),
    FileField(
        name='attachment2',
        widget=FileField._properties['widget'](
            label="File Attachment 2",
            description="If you have a list of participants, an agenda or other supportive documentation click browse and select the file to be uploaded.",
            label_msgid='ILOIntranetTypes_label_attachment2',
            description_msgid='ILOIntranetTypes_help_attachment2',
            i18n_domain='ILOIntranetTypes',
        ),
        storage=AttributeStorage(),
        searchable=1,
    ),
    FileField(
        name='attachment3',
        widget=FileField._properties['widget'](
            label="File Attachment 3",
            description="If you have a list of participants, an agenda or other supportive documentation click browse and select the file to be uploaded.",
            label_msgid='ILOIntranetTypes_label_attachment3',
            description_msgid='ILOIntranetTypes_help_attachment3',
            i18n_domain='ILOIntranetTypes',
        ),
        storage=AttributeStorage(),
        searchable=1,
    ),
    FileField(
        name='attachment4',
        widget=FileField._properties['widget'](
            label="File Attachment 4",
            description="If you have a list of participants, an agenda or other supportive documentation click browse and select the file to be uploaded.",
            label_msgid='ILOIntranetTypes_label_attachment4',
            description_msgid='ILOIntranetTypes_help_attachment4',
            i18n_domain='ILOIntranetTypes',
        ),
        storage=AttributeStorage(),
        searchable=1,
    ),
    FileField(
        name='attachment5',
        widget=FileField._properties['widget'](
            label="File Attachment 5",
            description="If you have a list of participants, an agenda or other supportive documentation click browse and select the file to be uploaded.",
            label_msgid='ILOIntranetTypes_label_attachment5',
            description_msgid='ILOIntranetTypes_help_attachment5',
            i18n_domain='ILOIntranetTypes',
        ),
        storage=AttributeStorage(),
        searchable=1,
    ),
    LinesField(
        name='invited_users',
        storage=AttributeStorage(),
        schemata='metadata',
    ),
    LinesField(
        name='attendees',
        storage=AttributeStorage(),
        schemata='metadata'
    ),
    BooleanField(
        name='reminder_sent',
        storage=AttributeStorage(),
        schemata='metadata',
        default=False
    )
),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

ILOEvent_schema = ATEventSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema
#ILOEvent_schema['reminder_sent'].widget.visible = {
#    'edit':'invisible','view':'invisible'
#}
class ILOEvent(ATEvent):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IILOEvent)

    meta_type = 'ILOEvent'
    _at_rename_after_creation = True

    schema = ILOEvent_schema

    reminder_sent = False

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    # Manually created methods

    def theme_vocab(self):
        portal_properties = getToolByName(self, 'portal_properties',
                None)
        themes = portal_properties.ilo_properties.getProperty('themesopts')

        return themes

    def office_vocab(self):
        portal_properties = getToolByName(self, 'portal_properties',
                None)
        offices = portal_properties.ilo_properties.getProperty('officeopts')

        return offices



registerType(ILOEvent, PROJECTNAME)
# end of class ILOEvent

##code-section module-footer #fill in your manual code here
##/code-section module-footer

