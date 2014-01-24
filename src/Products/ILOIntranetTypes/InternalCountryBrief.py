# -*- coding: utf-8 -*-
#
# File: InternalCountryBrief.py
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
from Products.ILOIntranetTypes.GCMember import GCMember
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.CompoundField.ArrayField import ArrayField
from Products.CompoundField.ArrayWidget import ArrayWidget
from Products.CompoundField.EnhancedArrayWidget import EnhancedArrayWidget
from Products.CompoundField.EnhancedArrayWidget import EnhancedArrayWidget
from Products.ILOIntranetTypes.config import *

# additional imports from tagged value 'import'
from Products.ILOIntranetTypes.ILOIntranetBase import ILOIntranetBase
from Products.ATContentTypes.content.event import ATEvent
from Products.ATContentTypes.content.event import ATEventSchema
from Products.ILOIntranetTypes.MissionReport import MissionReport
from Products.CompoundField.EnhancedArrayWidget import EnhancedArrayWidget
from Products.CMFCore.utils import getToolByName

##code-section module-header #fill in your manual code here

names_default = '''
<p>Political Inclination his/her party or coalition and government</p>
<p>In office since when:</p>
<p> Date of next Parliament/Presidential election:<p>
'''

connection_default = '''

<h3>Key initiative(s) s/he is pursuing</h3>
<p>&nbsp;</p>
<h3>Personal role in key national development (legislation/policy
etc.)</h3>
<p>&nbsp;</p>
<h3>Areas of special connection with the ILO and with the
Director-General</h3>
<p>&nbsp;</p>
<h3>Salient personal events, interests or achievements</h3>
<p>&nbsp;</p>
<h3>Any key points the DG should raise?</h3>
<p>&nbsp;</p>
'''

overall_situation_default = '''
<h3>Country Director's brief analysis of the political situation</h3>
<p>&nbsp;</p>
<h3>Highlights of particular interest for the ILO since last year</h3>
<p>&nbsp;</p>
'''

impact_default = '''
<h3>Decent Work Country Programme / ILO Programme</h3>
<p>&nbsp;</p>
<h3>Key Themes: one or two illustrations of impact</h3>
<p>&nbsp;</p>
<h3>Approximate total TC expenditure 2009</h3>
<p>&nbsp;</p>
<h3>ILO's best activities (policy advice, training, TC, other) <br /></h3>
<p><em>with succinct statement of reason why<br /></em></p>
<h3>Examples of recognition by constituents of ILO contribution</h3>
<p>&nbsp;</p>
<h3>Cooperation with other ministries</h3>
<p>&nbsp;</p>
<h3>International labour standards</h3>
<p>&nbsp;</p>
<h3>Social Dialogue and Tripartism</h3>
<p>&nbsp;</p>
<h3>
Short paragraph - assessment of how Tripartism is working</h3>
<p>&nbsp;</p>
<h3>Key figures on Employers' and Workers' organizations<br /></h3>
<p>&nbsp;</p>
'''

cooperation_default = '''
<h3>Relations with Resident Coordinator and UNDP representatives<br /></h3>
<p>&nbsp;</p>
<h3>Does the UNDAF reflect Decent Work Priorities and directions of
UNDAF?</h3>
<p>&nbsp;</p>
'''

further_resources_default = '''
<h3>Cooperation documents</h3>
<p>&nbsp;</p>
<h3>Key stakeholder contacts and information</h3>
<p>&nbsp;</p>
<h3>Sources for country information and data</h3>
<p>&nbsp;</p>
'''

##/code-section module-header

copied_fields = {}
copied_fields['title'] = BaseSchema['title'].copy()
copied_fields['title'].widget.label = "Country"
copied_fields['description'] = BaseSchema['description'].copy()
schema = Schema((

    copied_fields['title'],

    StringField(
        name='ecosoc_membership',
        widget=SelectionWidget(
            label="ECOSOC Membership",
            label_msgid='ILOIntranetTypes_label_ecosoc_membership',
            i18n_domain='ILOIntranetTypes',
        ),
        vocabulary=['Yes','No'],
    ),
    ArrayField(
        GCMember(
            name='governing_body_membership',
            widget=GCMember._properties['widget'](
                label="Member",
                label_msgid='ILOIntranetTypes_label_governing_body_membership',
                i18n_domain='ILOIntranetTypes',
            ),
        ),

        widget=EnhancedArrayWidget(
            label="Governing Body Membership",
            description="Click on the + button to add additional members and - to reduce.",
            label_msgid='ILOIntranetTypes_label_array:governing_body_membership',
            description_msgid='ILOIntranetTypes_help_array:governing_body_membership',
            i18n_domain='ILOIntranetTypes',
        ),
        size=1,
    ),
    IntegerField(
        name='rb_p',
        default=0,
        widget=IntegerWidget(
            label="No. of RB P Staff",
            label_msgid='ILOIntranetTypes_label_rb_p',
            i18n_domain='ILOIntranetTypes',
        ),
    ),
    IntegerField(
        name='rb_no',
        default=0,
        widget=IntegerWidget(
            label="No. of RB NO Staff",
            label_msgid='ILOIntranetTypes_label_rb_no',
            i18n_domain='ILOIntranetTypes',
        ),
    ),
    IntegerField(
        name='rb_gs',
        default=0,
        widget=IntegerWidget(
            label="No. of RB GS Staff",
            label_msgid='ILOIntranetTypes_label_rb_gs',
            i18n_domain='ILOIntranetTypes',
        ),
    ),
    IntegerField(
        name='tc_no',
        default=0,
        widget=IntegerWidget(
            label="No. of TC NO Staff",
            label_msgid='ILOIntranetTypes_label_tc_no',
            i18n_domain='ILOIntranetTypes',
        ),
    ),
    IntegerField(
        name='tc_p',
        default=0,
        widget=IntegerWidget(
            label="No. of TC P Staff",
            label_msgid='ILOIntranetTypes_label_tc_p',
            i18n_domain='ILOIntranetTypes',
        ),
    ),
    IntegerField(
        name='tc_gs',
        default=0,
        widget=IntegerWidget(
            label="No. of TC GS Staff",
            label_msgid='ILOIntranetTypes_label_tc_gs',
            i18n_domain='ILOIntranetTypes',
        ),
    ),
    StringField(
        name='labour_minister',
        widget=StringField._properties['widget'](
            label="Name of Labour Minister",
            label_msgid='ILOIntranetTypes_label_labour_minister',
            i18n_domain='ILOIntranetTypes',
        ),
    ),
    DateTimeField(
        name='labour_minister_start',
        widget=DateTimeField._properties['widget'](
            show_hm=False,
            label="Labour Minister's Date of Appointment",
            label_msgid='ILOIntranetTypes_label_labour_minister_start',
            i18n_domain='ILOIntranetTypes',
        ),
    ),
    FileField(
        name='labour_minister_cv',
        widget=FileField._properties['widget'](
            label="Attach CV if available",
            label_msgid='ILOIntranetTypes_label_labour_minister_cv',
            i18n_domain='ILOIntranetTypes',
        ),
        storage=AttributeStorage(),
    ),
    TextField(
        name='labour_minister_connection',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        default=connection_default,
        widget=RichWidget(
            label="Connecting with the Labour Minister (Confidential)",
            label_msgid='ILOIntranetTypes_label_labour_minister_connection',
            i18n_domain='ILOIntranetTypes',
        ),
        default_output_type='text/html',
    ),
    StringField(
        name='president_name',
        widget=StringField._properties['widget'](
            label="Name of President",
            visible={'edit':'invisible'},
            label_msgid='ILOIntranetTypes_label_president_name',
            i18n_domain='ILOIntranetTypes',
        ),
    ),
    TextField(
        name='labour_minister_last_meeting',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label="Last meeting with the Labour Minister",
            description="CABINET to complete",
            label_msgid='ILOIntranetTypes_label_labour_minister_last_meeting',
            description_msgid='ILOIntranetTypes_help_labour_minister_last_meeting',
            i18n_domain='ILOIntranetTypes',
        ),
        default_output_type='text/html',
    ),
    DateTimeField(
        name='president_start',
        widget=DateTimeField._properties['widget'](
            label="President's Date of Appointment",
            show_hm=False,
            visible={'edit':'invisible'},
            label_msgid='ILOIntranetTypes_label_president_start',
            i18n_domain='ILOIntranetTypes',
        ),
    ),
    DateTimeField(
        name='president_election',
        widget=DateTimeField._properties['widget'](
            label="Date of President's next election",
            show_hm=False,
            visible={'edit':'invisible'},
            label_msgid='ILOIntranetTypes_label_president_election',
            i18n_domain='ILOIntranetTypes',
        ),
    ),
    FileField(
        name='president_cv',
        widget=FileField._properties['widget'](
            label="Attach CV if available",
            visible={'edit':'invisible'},
            label_msgid='ILOIntranetTypes_label_president_cv',
            i18n_domain='ILOIntranetTypes',
        ),
        storage=AttributeStorage(),
    ),
    TextField(
        name='president_politics',
        widget=TextAreaWidget(
            label="Political Inclination",
            description="Political Inclination  of President's party or coalition and government",
            visible={'edit':'invisible'},
            label_msgid='ILOIntranetTypes_label_president_politics',
            description_msgid='ILOIntranetTypes_help_president_politics',
            i18n_domain='ILOIntranetTypes',
        ),
    ),
    StringField(
        name='pm_name',
        widget=StringField._properties['widget'](
            label="Name of Prime Minister",
            visible={'edit':'invisible'},
            label_msgid='ILOIntranetTypes_label_pm_name',
            i18n_domain='ILOIntranetTypes',
        ),
    ),
    DateTimeField(
        name='pm_start',
        widget=DateTimeField._properties['widget'](
            label="Prime Minister's Date of Appointment",
            show_hm=False,
            visible={'edit':'invisible'},
            label_msgid='ILOIntranetTypes_label_pm_start',
            i18n_domain='ILOIntranetTypes',
        ),
    ),
    DateTimeField(
        name='pm_election',
        widget=DateTimeField._properties['widget'](
            label="Date of Prime Minister's next election",
            show_hm=False,
            visible={'edit':'invisible'},
            label_msgid='ILOIntranetTypes_label_pm_election',
            i18n_domain='ILOIntranetTypes',
        ),
    ),
    FileField(
        name='pm_cv',
        widget=FileField._properties['widget'](
            label="Attach CV if available",
            visible={'edit':'invisible'},
            label_msgid='ILOIntranetTypes_label_pm_cv',
            i18n_domain='ILOIntranetTypes',
        ),
        storage=AttributeStorage(),
    ),
    TextField(
        name='pm_politics',
        widget=TextAreaWidget(
            label="Political Inclination",
            description="Political Inclination of Prime Minister's party or coalition and government",
            visible={'edit':'invisible'},
            label_msgid='ILOIntranetTypes_label_pm_politics',
            description_msgid='ILOIntranetTypes_help_pm_politics',
            i18n_domain='ILOIntranetTypes',
        ),
    ),
    StringField(
        name='head_gov_name',
        widget=StringField._properties['widget'](
            label="Name of Head of Government",
            label_msgid='ILOIntranetTypes_label_head_gov_name',
            i18n_domain='ILOIntranetTypes',
        ),
    ),
    DateTimeField(
        name='head_gov_start',
        widget=DateTimeField._properties['widget'](
            label="Head of Government's date of appointment",
            label_msgid='ILOIntranetTypes_label_head_gov_start',
            i18n_domain='ILOIntranetTypes',
        ),
    ),
    DateTimeField(
        name='head_gov_election',
        widget=DateTimeField._properties['widget'](
            label="Date of next election",
            label_msgid='ILOIntranetTypes_label_head_gov_election',
            i18n_domain='ILOIntranetTypes',
        ),
    ),
    FileField(
        name='head_gov_cv',
        widget=FileField._properties['widget'](
            label="Attach CV if available",
            label_msgid='ILOIntranetTypes_label_head_gov_cv',
            i18n_domain='ILOIntranetTypes',
        ),
        storage=AttributeStorage(),
    ),
    TextField(
        name='head_gov_politics',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label="Political inclination (Confidential)",
            description="Political inclination of Head of Government's party or coalition and government",
            label_msgid='ILOIntranetTypes_label_head_gov_politics',
            description_msgid='ILOIntranetTypes_help_head_gov_politics',
            i18n_domain='ILOIntranetTypes',
        ),
        default_output_type='text/html',
    ),
    TextField(
        name='impact',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        default=impact_default,
        widget=RichWidget(
            label="The impact and strategic significance of the ILO in the country",
            description="Focus on results, outcomes, impact - not detailed description of ILO activities and programes",
            label_msgid='ILOIntranetTypes_label_impact',
            description_msgid='ILOIntranetTypes_help_impact',
            i18n_domain='ILOIntranetTypes',
        ),
        default_output_type='text/html',
    ),
    TextField(
        name='overall_situation',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        default=overall_situation_default,
        widget=RichWidget(
            label="Overall Situation (descriptive)",
            label_msgid='ILOIntranetTypes_label_overall_situation',
            i18n_domain='ILOIntranetTypes',
        ),
        default_output_type='text/html',
    ),
    TextField(
        name='overall_situation_analytical',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label="Overall Situation - Analytical (Confidential)",
            description="Positive / negative key issues (e.g. country’s response to the Global Jobs Pact",
            label_msgid='ILOIntranetTypes_label_overall_situation_analytical',
            description_msgid='ILOIntranetTypes_help_overall_situation_analytical',
            i18n_domain='ILOIntranetTypes',
        ),
        default_output_type='text/html',
    ),
    TextField(
        name='office_view',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label="View of the Regional Office (Confidential)",
            label_msgid='ILOIntranetTypes_label_office_view',
            i18n_domain='ILOIntranetTypes',
        ),
        default_output_type='text/html',
    ),
    TextField(
        name='cooperation',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        default=cooperation_default,
        widget=RichWidget(
            label="Cooperation with the UN Family (Confidential)",
            label_msgid='ILOIntranetTypes_label_cooperation',
            i18n_domain='ILOIntranetTypes',
        ),
        default_output_type='text/html',
    ),
    TextField(
        name='cooperation_organizations',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label="Relationship with other multilateral and bilateral organizations",
            label_msgid='ILOIntranetTypes_label_cooperation_organizations',
            i18n_domain='ILOIntranetTypes',
        ),
        default_output_type='text/html',
    ),
    TextField(
        name='socio_economic_context',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label="Socio Economic Context",
            description="Brief Key Points - One point per line",
            label_msgid='ILOIntranetTypes_label_socio_economic_context',
            description_msgid='ILOIntranetTypes_help_socio_economic_context',
            i18n_domain='ILOIntranetTypes',
        ),
        default_output_type='text/html',
    ),
    copied_fields['description'],

    TextField(
        name='chronology',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label="Chronology of relevant past and prospective activities",
            label_msgid='ILOIntranetTypes_label_chronology',
            i18n_domain='ILOIntranetTypes',
        ),
        default_output_type='text/html',
    ),
    TextField(
        name='further_resources',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        default=further_resources_default,
        widget=RichWidget(
            label="Further Resources",
            label_msgid='ILOIntranetTypes_label_further_resources',
            i18n_domain='ILOIntranetTypes',
        ),
        default_output_type='text/html',
    ),
    FileField(
        name='attachment1',
        widget=FileField._properties['widget'](
            label="File attachment 1",
            description="Additional files to be attached to this note.",
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
            description="Additional files to be attached to this note.",
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
            description="Additional files to be attached to this note.",
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
            description="Additional files to be attached to this note.",
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
            description="Additional files to be attached to this note.",
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

InternalCountryBrief_schema = BaseSchema.copy() + \
    getattr(ATCTContent, 'schema', Schema(())).copy() + \
    getattr(HistoryAwareMixin, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class InternalCountryBrief(BaseContent, ATCTContent, HistoryAwareMixin, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IInternalCountryBrief)

    meta_type = 'InternalCountryBrief'
    _at_rename_after_creation = True

    schema = InternalCountryBrief_schema

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



registerType(InternalCountryBrief, PROJECTNAME)
# end of class InternalCountryBrief

##code-section module-footer #fill in your manual code here
##/code-section module-footer

