# -*- coding: utf-8 -*-
#
# File: MissionReport.py
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
from Products.ATContentTypes.content.image import ATCTImageTransform
from Products.ATContentTypes.content.base import ATCTContent
from Products.ATContentTypes.lib.historyaware import HistoryAwareMixin
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.ILOIntranetTypes.config import *

##code-section module-header #fill in your manual code here

from Products.ATContentTypes.content.event import ATEvent
from Products.ATContentTypes.content.event import ATEventSchema
from Products.ILOIntranetTypes.ILOIntranetBase import ILOIntranetBase

from simplejson import dumps as jsondumps
from collective.atautocomplete.widgets import LinesAutoCompleteWidget
from Products.CMFCore.utils import getToolByName

##/code-section module-header

copied_fields = {}
copied_fields['title'] = BaseSchema['title'].copy()
copied_fields['title'].default_method = "defTitle"
copied_fields['title'].widget.label = "Mission Title"
copied_fields['title'].widget.description = "Brief title of mission. eg. ICT Skills Training Workshop."
copied_fields['description'] = BaseSchema['description'].copy()
copied_fields['description'].required = 1
copied_fields['description'].schemata = "default"
copied_fields['description'].default_method = "MissionDescription"
copied_fields['description'].widget.label = "Overall Objective"
copied_fields['description'].widget.description = "Briefly describe the objectives of the mission."
#copied_fields['members'] = ILOIntranetBase.schema['members'].copy()
#copied_fields['members'].imports = "ILOIntranetBase"
#copied_fields['members'].default_method = "defMembers"
copied_fields['office'] = ILOIntranetBase.schema['office'].copy()
copied_fields['office'].required = 1
copied_fields['office'].default_method = "defOffice"
copied_fields['office'].widget.label = "ILO Office"
copied_fields['startDate'] = ATEventSchema['startDate'].copy()
copied_fields['startDate'].required = 1
#copied_fields['startDate'].default_method = "defStartDate"
copied_fields['startDate'].widget.show_hm = False
copied_fields['startDate'].widget.label = "Mission Start Date"
copied_fields['startDate'].widget.starting_year = 2009
copied_fields['startDate'].widget.ending_year = 2015
copied_fields['endDate'] = ATEventSchema['endDate'].copy()
copied_fields['endDate'].required = 1
#copied_fields['endDate'].default_method = "defEndDate"
copied_fields['endDate'].widget.show_hm = False
copied_fields['endDate'].widget.starting_year = 2009
copied_fields['endDate'].widget.ending_year = 2015
copied_fields['endDate'].widget.label = "Mission End Date"
copied_fields['domestic'] = ILOIntranetBase.schema['domestic'].copy()
copied_fields['domestic'].default_method = "mission_type"
copied_fields['mission_location'] = ILOIntranetBase.schema['mission_location'].copy()
copied_fields['mission_location'].imports = "ILOIntranetBase"
copied_fields['mission_location'].required = 1
copied_fields['mission_location'].default_method = "defMission_Location"
copied_fields['mission_location'].widget.label = "Mission Location"
copied_fields['theme'] = ILOIntranetBase.schema['theme'].copy()
copied_fields['theme'].imports = "ILOIntranetBase"
copied_fields['theme'].default_method = "defTheme"
schema = Schema((

    copied_fields['title'],

    copied_fields['description'],

    StringField(
        name='outcome',
        widget=StringField._properties['widget'](
            label="Country / Regional Programme Outcome",
            description="Enter outcome code here eg. IDN 101",
            label_msgid='ILOIntranetTypes_label_outcome',
            description_msgid='ILOIntranetTypes_help_outcome',
            i18n_domain='ILOIntranetTypes',
        ),
        searchable=1,
    ),
    TextField(
        name='outcome_text',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label="Contribution to Outcome",
            description="Please describe briefly how your mission has contributed to realizing the relevant country/regional outcome.",
            label_msgid='ILOIntranetTypes_label_outcome_text',
            description_msgid='ILOIntranetTypes_help_outcome_text',
            i18n_domain='ILOIntranetTypes',
        ),
        default_output_type='text/html',
        searchable=1,
    ),
    LinesField(
        name='authors',
        widget=LinesField._properties['widget'](
            label="Author(s)",
            description="List of authors. One name per line, with principal author first.",
            label_msgid='ILOIntranetTypes_label_authors',
            description_msgid='ILOIntranetTypes_help_authors',
            i18n_domain='ILOIntranetTypes',
        ),
        required=True,
        searchable=True,
    ),
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

    copied_fields['office'],

    copied_fields['startDate'],

    copied_fields['endDate'],

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
        searchable=True,
        default_method="defCity",
    ),
    copied_fields['mission_location'],

    StringField(
        name='mission_location_other',
        widget=StringField._properties['widget'](
            label="Other",
            description="If Other was selected, please specify country location.",
            label_msgid='ILOIntranetTypes_label_mission_location_other',
            description_msgid='ILOIntranetTypes_help_mission_location_other',
            i18n_domain='ILOIntranetTypes',
        ),
        default_method="defMission_Location_Other",
    ),
    copied_fields['theme'],

    StringField(
        name='theme_other',
        widget=StringField._properties['widget'](
            label="Theme (Other)",
            description="If Other is selected, please fill in this field.",
            label_msgid='ILOIntranetTypes_label_theme_other',
            description_msgid='ILOIntranetTypes_help_theme_other',
            i18n_domain='ILOIntranetTypes',
        ),
        default_method="defTheme_Other",
    ),
    TextField(
        name='SummaryAchievements',
        widget=RichWidget(
            label="Summary of Main Achievements",
            description="Please fill this section in short telex style.",
            label_msgid='ILOIntranetTypes_label_SummaryAchievements',
            description_msgid='ILOIntranetTypes_help_SummaryAchievements',
            i18n_domain='ILOIntranetTypes',
        ),
        default_output_type='text/html',
        searchable=1,
    ),
    TextField(
        name='MissionFindings',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label="Mission Findings",
            description="Please keep to approx 500 words. Other relevant documents can be attached below.",
            label_msgid='ILOIntranetTypes_label_MissionFindings',
            description_msgid='ILOIntranetTypes_help_MissionFindings',
            i18n_domain='ILOIntranetTypes',
        ),
        default_output_type='text/html',
        searchable=1,
    ),
    TextField(
        name='followup',
        widget=RichWidget(
            label="Follow-up actions/next steps",
            description="In point form, include who should be doing what. One follow-up action per line.",
            label_msgid='ILOIntranetTypes_label_followup',
            description_msgid='ILOIntranetTypes_help_followup',
            i18n_domain='ILOIntranetTypes',
        ),
        default_output_type='text/html',
        searchable=1,
    ),
    TextField(
        name='contacts',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label="List of Contacts",
            description="List of professionals and/or organizations met with during the mission",
            label_msgid='ILOIntranetTypes_label_contacts',
            description_msgid='ILOIntranetTypes_help_contacts',
            i18n_domain='ILOIntranetTypes',
        ),
        default_output_type='text/html',
        searchable=1,
    ),
    LinesField(
        name='distribution',
        widget=LinesAutoCompleteWidget(
            label="Distribution List",
            description="Comma separated list of who a copy of this mission report should be sent to. Select previous email addresses from drop down list, or type new email address followed by a comma. Copy will be sent, when Mission Report state is submitted.",
            label_msgid='ILOIntranetTypes_label_distribution',
            description_msgid='ILOIntranetTypes_help_distribution',
            i18n_domain='ILOIntranetTypes',
        ),
        default_content_type='text/plain',
        allowable_content_types="('text/plain')",
        validators=('isEmailList',),
        vocabularyjsonurl="distributionlist",
    ),
    FileField(
        name='attachment1',
        widget=FileField._properties['widget'](
            label="File attachment 1",
            description="Additional files to be attached to this report.",
            label_msgid='ILOIntranetTypes_label_attachment1',
            description_msgid='ILOIntranetTypes_help_attachment1',
            i18n_domain='ILOIntranetTypes',
        ),
        storage=AttributeStorage(),
        maxsize=3,
        searchable=1,
        validators=('isMaxSize',),
    ),
    FileField(
        name='attachment2',
        widget=FileField._properties['widget'](
            label="File Attachment 2",
            description="Additional files to be attached to this report.",
            label_msgid='ILOIntranetTypes_label_attachment2',
            description_msgid='ILOIntranetTypes_help_attachment2',
            i18n_domain='ILOIntranetTypes',
        ),
        storage=AttributeStorage(),
        maxsize=3,
        searchable=1,
        validators=('isMaxSize',),
    ),
    FileField(
        name='attachment3',
        widget=FileField._properties['widget'](
            label="File Attachment 3",
            description="Additional files to be attached to this report.",
            label_msgid='ILOIntranetTypes_label_attachment3',
            description_msgid='ILOIntranetTypes_help_attachment3',
            i18n_domain='ILOIntranetTypes',
        ),
        storage=AttributeStorage(),
        maxsize=3,
        searchable=1,
        validators=('isMaxSize',),
    ),
    FileField(
        name='attachment4',
        widget=FileField._properties['widget'](
            label="File Attachment 4",
            description="Additional files to be attached to this report.",
            label_msgid='ILOIntranetTypes_label_attachment4',
            description_msgid='ILOIntranetTypes_help_attachment4',
            i18n_domain='ILOIntranetTypes',
        ),
        storage=AttributeStorage(),
        maxsize=3,
        searchable=1,
        validators=('isMaxSize',),
    ),
    FileField(
        name='attachment5',
        widget=FileField._properties['widget'](
            label="File Attachment 5",
            description="Additional files to be attached to this report.",
            label_msgid='ILOIntranetTypes_label_attachment5',
            description_msgid='ILOIntranetTypes_help_attachment5',
            i18n_domain='ILOIntranetTypes',
        ),
        storage=AttributeStorage(),
        maxsize=3,
        searchable=1,
        validators=('isMaxSize',),
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

MissionReport_schema = BaseSchema.copy() + \
    getattr(ATCTContent, 'schema', Schema(())).copy() + \
    getattr(HistoryAwareMixin, 'schema', Schema(())).copy() + \
    getattr(ATCTImageTransform, 'schema', Schema(())).copy() + \
    getattr(ATCTContent, 'schema', Schema(())).copy() + \
    getattr(HistoryAwareMixin, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class MissionReport(BaseContent, ATCTContent, HistoryAwareMixin, ATCTImageTransform, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IMissionReport)

    meta_type = 'MissionReport'
    _at_rename_after_creation = True

    schema = MissionReport_schema
    schema['startDate'].widget.show_hm = False
    schema['startDate'].widget.format = '%b %d, %Y'
    schema['endDate'].widget.show_hm = False
    schema['endDate'].widget.format = '%b %d, %Y'

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    # Manually created methods

    def getMission(self):
        catalog = getToolByName(self,'portal_catalog')
        referrer = self.REQUEST.environ.get('HTTP_REFERER')
        if referrer:
            path = self.REQUEST.physicalPathFromURL(referrer)
            if path[-1] in ['view']:
                path = path[:-1]
            
            mission = catalog.searchResults(path={'query':"/".join(path),'depth':0},
                                portal_type='Mission')
            if len(mission):
                return mission[0].getObject()
        return None

    def defTitle(self):
        mission = self.getMission()
        if mission:
            return mission.Title()
        else:
            return ''

    def mission_type(self):
        mission = self.getMission()
        if mission:
            return mission.getDomestic()
        else:
            return ''

    def defStartDate(self):
        mission = self.getMission()
        if mission:
            return mission.startDate
        else:
            return ''

    def defEndDate(self):
        mission = self.getMission()
        if mission:
            return mission.endDate
        else:
            return ''

    def MissionDescription(self):
        mission = self.getMission()
        if mission:
            return mission.Description()
        else:
            return ''

    def defMembers(self):
        mission = self.getMission()
        if mission:
            return mission.getMembers()
        else:
            return ''

    def defOffice(self):
        mission = self.getMission()
        if mission:
            return mission.getOffice()
        else:
            return ''

    def defCity(self):
        mission = self.getMission()
        if mission:
            return mission.getCity()
        else:
            return ''

    def defMission_Location(self):
        mission = self.getMission()
        if mission:
            return mission.getMission_event_location()
        else:
            return ''

    def defMission_Location_Other(self):
        mission = self.getMission()
        if mission:
            return mission.getMission_location_other()
        else:
            return ''

    def defTheme(self):
        mission = self.getMission()
        if mission:
            return mission.getTheme()
        else:
            return ''

    def defTheme_Other(self):
        mission = self.getMission()
        if mission:
            return mission.getTheme_other()
        else:
            return ''

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
    
    def post_validate(self, REQUEST, errors):
        if REQUEST['startDate'] and REQUEST['endDate']:
            if REQUEST['startDate'] > REQUEST['endDate']:
                errors['endDate'] = "End date should not be earlier than start date."



registerType(MissionReport, PROJECTNAME)
# end of class MissionReport

##code-section module-footer #fill in your manual code here
##/code-section module-footer

