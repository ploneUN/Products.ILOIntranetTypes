# -*- coding: utf-8 -*-
#
# File: Mission.py
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
from Products.ATContentTypes.content.base import ATCTContent
from Products.ATContentTypes.lib.historyaware import HistoryAwareMixin
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.ILOIntranetTypes.config import *

##code-section module-header #fill in your manual code here

from Products.ATContentTypes.content.event import ATEvent
from Products.ATContentTypes.content.event import ATEventSchema
from Products.ILOIntranetTypes.ILOIntranetBase import ILOIntranetBase
from Products.CMFCore.utils import getToolByName

from simplejson import dumps as jsondumps
from collective.atautocomplete.widgets import LinesAutoCompleteWidget

##/code-section module-header

copied_fields = {}
copied_fields['title'] = BaseSchema['title'].copy()
copied_fields['title'].widget.label = "Mission Title"
copied_fields['title'].widget.description = "Please enter using format of Full Name, Purpose. eg. Johan Arvling, Knowledge Management Training."
copied_fields['description'] = BaseSchema['description'].copy()
copied_fields['description'].required = 1
copied_fields['description'].schemata = "default"
copied_fields['description'].searchable = 1
copied_fields['description'].widget.label = "Mission Objective"
copied_fields['description'].widget.description = "Briefly describe the objectives of the mission."
copied_fields['domestic'] = ILOIntranetBase.schema['domestic'].copy()
copied_fields['mission_event_location'] = ILOIntranetBase.schema['mission_event_location'].copy()
copied_fields['mission_event_location'].imports = "ILOIntranetBase"
copied_fields['mission_event_location'].required = 1
copied_fields['mission_event_location'].widget.label = "Mission Event Location"
copied_fields['mission_event_location'].widget.description = "Country or Location"
copied_fields['startDate'] = ATEventSchema['startDate'].copy()
copied_fields['startDate'].required = 1
copied_fields['startDate'].widget.label = "Mission Start Date"
copied_fields['endDate'] = ATEventSchema['endDate'].copy()
copied_fields['endDate'].required = 1
copied_fields['endDate'].widget.label = "Mission End Date"
copied_fields['endDate'].widget.description = "Please change the the time to pm, so that the Calendar shows the right date for your Mission return."
#copied_fields['members'] = ILOIntranetBase.schema['members'].copy()
#copied_fields['members'].imports = "ILOIntranetBase"
copied_fields['text'] = ATEventSchema['text'].copy()
copied_fields['text'].widget.label = "Notes"
copied_fields['office'] = ILOIntranetBase.schema['office'].copy()
copied_fields['office'].required = 1
copied_fields['theme'] = ILOIntranetBase.schema['theme'].copy()
copied_fields['theme'].imports = "ILOIntranetBase"
copied_fields['contactName'] = ATEventSchema['contactName'].copy()
copied_fields['contactName'].widget.label = u'Contact Person'
copied_fields['contactEmail'] = ATEventSchema['contactEmail'].copy()
copied_fields['contactEmail'].widget.label = u'Contact Person Email'
copied_fields['contactPhone'] = ATEventSchema['contactPhone'].copy()
copied_fields['contactPhone'].widget.label = u'Contact Person Phone'

schema = Schema((

    copied_fields['title'],

    copied_fields['description'],

    copied_fields['domestic'],

    StringField(
        name='city',
        widget=StringField._properties['widget'](
            label="City",
            description="Please enter the city (or cities) for this mission.",
            label_msgid='ILOIntranetTypes_label_city',
            description_msgid='ILOIntranetTypes_help_city',
            i18n_domain='ILOIntranetTypes',
        ),
        searchable=1,
    ),
    copied_fields['mission_event_location'],

    copied_fields['startDate'],

    copied_fields['endDate'],

    #copied_fields['members'],
    LinesField(
        name='members',
        widget=LinesAutoCompleteWidget(
            label="Mission Members",
            description="List of Mission Members, separated with comma with principal member first.",
            label_msgid='ILOIntranetTypes_label_members',
            description_msgid='ILOIntranetTypes_help_members',
            i18n_domain='ILOIntranetTypes',
        ),
        default_content_type='text/plain',
        allowable_content_types="('text/plain')",
        vocabularyjsonurl="missionmembers",
    ),

    copied_fields['text'],

    copied_fields['office'],

    copied_fields['theme'],

    StringField(
        name='theme_other',
        widget=StringField._properties['widget'](
            description="If Other is selected, please fill in this field.",
            label="Theme (Other)",
            label_msgid='ILOIntranetTypes_label_theme_other',
            description_msgid='ILOIntranetTypes_help_theme_other',
            i18n_domain='ILOIntranetTypes',
        ),
    ),
    StringField(
        name='mission_location_other',
        widget=StringField._properties['widget'](
            label="Other Regions",
            description="If Other Regions was selected, please specify country location.",
            label_msgid='ILOIntranetTypes_label_mission_location_other',
            description_msgid='ILOIntranetTypes_help_mission_location_other',
            i18n_domain='ILOIntranetTypes',
        ),
    ),

    copied_fields['contactName'],

    copied_fields['contactEmail'],

    copied_fields['contactPhone']

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Mission_schema = BaseSchema.copy() + \
    getattr(ATCTContent, 'schema', Schema(())).copy() + \
    getattr(HistoryAwareMixin, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Mission(BaseContent, ATCTContent, HistoryAwareMixin, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IMission)

    meta_type = 'Mission'
    _at_rename_after_creation = True

    schema = Mission_schema
    schema['startDate'].widget.show_hm = False
    schema['startDate'].widget.format = '%b %d, %Y'
    schema['endDate'].widget.show_hm = False
    schema['endDate'].widget.format = '%b %d, %Y'

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods
    def post_validate(self, REQUEST, errors):
        if REQUEST['startDate'] and REQUEST['endDate']:
            if REQUEST['startDate'] > REQUEST['endDate']:
                errors['endDate'] = "End date should not be earlier than start date."
    

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



registerType(Mission, PROJECTNAME)
# end of class Mission

##code-section module-footer #fill in your manual code here
##/code-section module-footer

