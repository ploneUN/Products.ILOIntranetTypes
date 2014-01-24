# -*- coding: utf-8 -*-
#
# File: StaffKnowledgeTransfer.py
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

from Products.ILOIntranetTypes.config import *

# additional imports from tagged value 'import'
from Products.ILOIntranetTypes.ILOIntranetBase import ILOIntranetBase
from Products.ATContentTypes.content.event import ATEvent
from Products.ATContentTypes.content.event import ATEventSchema
from Products.ILOIntranetTypes.MissionReport import MissionReport
from Products.CMFCore.utils import getToolByName

##code-section module-header #fill in your manual code here
##/code-section module-header

copied_fields = {}
copied_fields['title'] = BaseSchema['title'].copy()
copied_fields['title'].widget.label = "Name of Staff"
copied_fields['office'] = ILOIntranetBase.schema['office'].copy()
copied_fields['office'].required = 1
copied_fields['office'].widget.label = "ILO Office of last assignment"
copied_fields['office'].widget.description = "Please select office you last worked in."
copied_fields['office'].widget.type = "SelectionWidget"
copied_fields['startDate'] = ATEventSchema['startDate'].copy()
copied_fields['startDate'].widget.label = "Start Date"
copied_fields['startDate'].widget.show_hm = False
copied_fields['endDate'] = ATEventSchema['endDate'].copy()
copied_fields['endDate'].widget.label = "End Date"
copied_fields['endDate'].widget.show_hm = False
copied_fields['theme'] = ILOIntranetBase.schema['theme'].copy()
copied_fields['theme'].required = 1
copied_fields['theme'].widget.label = "Key area of work expertise during the assignment period"
copied_fields['theme'].widget.description = "Please select related areas of work. Hold CTRL to make multiple selections."
schema = Schema((

    copied_fields['title'],

    StringField(
        name='assignment_title',
        widget=StringField._properties['widget'](
            label="Assignment Title",
            label_msgid='ILOIntranetTypes_label_assignment_title',
            i18n_domain='ILOIntranetTypes',
        ),
        required=1,
        searchable=1,
    ),
    copied_fields['office'],

    copied_fields['startDate'],

    copied_fields['endDate'],

    copied_fields['theme'],

    StringField(
        name='contract_type',
        widget=SelectionWidget(
            label="Type of Contract",
            label_msgid='ILOIntranetTypes_label_contract_type',
            i18n_domain='ILOIntranetTypes',
        ),
        required=1,
        vocabulary=['Regular Budget','Technical Cooperation'],
    ),
    StringField(
        name='assignment_grade',
        widget=StringField._properties['widget'](
            label="Assignment Grade",
            description="Please indicate your salary grade and step e.g. P4 - 10.",
            label_msgid='ILOIntranetTypes_label_assignment_grade',
            description_msgid='ILOIntranetTypes_help_assignment_grade',
            i18n_domain='ILOIntranetTypes',
        ),
        required=1,
        searchable=1,
    ),
    TextField(
        name='key_contacts',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            description="Please list key professionals and/or organizations met / worked with during the assignment with details of why they are valuable to the work of your successor.",
            label="Key contacts established / maintained during assignment period",
            label_msgid='ILOIntranetTypes_label_key_contacts',
            description_msgid='ILOIntranetTypes_help_key_contacts',
            i18n_domain='ILOIntranetTypes',
        ),
        default_output_type='text/html',
        searchable=1,
    ),
    TextField(
        name='key_resources',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            description="Please list key resource mobilization opportunities / contacts that you are pursuing.",
            label="Key resource mobilization opportunities being pursued",
            label_msgid='ILOIntranetTypes_label_key_resources',
            description_msgid='ILOIntranetTypes_help_key_resources',
            i18n_domain='ILOIntranetTypes',
        ),
        default_output_type='text/html',
        searchable=1,
    ),
    TextField(
        name='outstanding_issues',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            description="Please list pending issue or follow-up action needed by your successor.",
            label="Pending issues that need follow-up or action by your successor",
            label_msgid='ILOIntranetTypes_label_outstanding_issues',
            description_msgid='ILOIntranetTypes_help_outstanding_issues',
            i18n_domain='ILOIntranetTypes',
        ),
        default_output_type='text/html',
        searchable=1,
    ),
    TextField(
        name='lessons_learned',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            description="Please briefly describe key policy lessons releated to your area of work that a successor should take note of in order to be able to work effectively during his/her assignment.",
            label="Top 5 lessons learned during the assignment period",
            label_msgid='ILOIntranetTypes_label_lessons_learned',
            description_msgid='ILOIntranetTypes_help_lessons_learned',
            i18n_domain='ILOIntranetTypes',
        ),
        default_output_type='text/html',
        searchable=1,
    ),
    TextField(
        name='advice',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label="Top 5 things you would advice your successor to do",
            description="Please briefly describe key tips or insight a successor should do in order to be able to work effectively during his/her assignment.",
            label_msgid='ILOIntranetTypes_label_advice',
            description_msgid='ILOIntranetTypes_help_advice',
            i18n_domain='ILOIntranetTypes',
        ),
        default_output_type='text/html',
        searchable=1,
    ),
    TextField(
        name='advice_not',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            description="Please briefly describe tips or insights a successor should not do in order to be able to work effectively during his/her assignment.",
            label="Top 5 things you would advice your successor not to do",
            label_msgid='ILOIntranetTypes_label_advice_not',
            description_msgid='ILOIntranetTypes_help_advice_not',
            i18n_domain='ILOIntranetTypes',
        ),
        default_output_type='text/html',
        searchable=1,
    ),
    FileField(
        name='file1',
        widget=FileField._properties['widget'](
            label="Resource 1",
            label_msgid='ILOIntranetTypes_label_file1',
            i18n_domain='ILOIntranetTypes',
        ),
        storage=AttributeStorage(),
        searchable=1,
    ),
    FileField(
        name='file2',
        widget=FileField._properties['widget'](
            label="Resource 2",
            label_msgid='ILOIntranetTypes_label_file2',
            i18n_domain='ILOIntranetTypes',
        ),
        storage=AttributeStorage(),
        searchable=1,
    ),
    FileField(
        name='file3',
        widget=FileField._properties['widget'](
            label="Resource 3",
            label_msgid='ILOIntranetTypes_label_file3',
            i18n_domain='ILOIntranetTypes',
        ),
        storage=AttributeStorage(),
        searchable=1,
    ),
    FileField(
        name='file4',
        widget=FileField._properties['widget'](
            label="Resource 4",
            label_msgid='ILOIntranetTypes_label_file4',
            i18n_domain='ILOIntranetTypes',
        ),
        storage=AttributeStorage(),
        searchable=1,
    ),
    FileField(
        name='file5',
        widget=FileField._properties['widget'](
            label="Resource 5",
            label_msgid='ILOIntranetTypes_label_file5',
            i18n_domain='ILOIntranetTypes',
        ),
        storage=AttributeStorage(),
        searchable=1,
    ),
    FileField(
        name='file6',
        widget=FileField._properties['widget'](
            label="Resource 6",
            label_msgid='ILOIntranetTypes_label_file6',
            i18n_domain='ILOIntranetTypes',
        ),
        storage=AttributeStorage(),
        searchable=1,
    ),
    FileField(
        name='file7',
        widget=FileField._properties['widget'](
            label="Resource 7",
            label_msgid='ILOIntranetTypes_label_file7',
            i18n_domain='ILOIntranetTypes',
        ),
        storage=AttributeStorage(),
        searchable=1,
    ),
    FileField(
        name='file8',
        widget=FileField._properties['widget'](
            label="Resource 8",
            label_msgid='ILOIntranetTypes_label_file8',
            i18n_domain='ILOIntranetTypes',
        ),
        storage=AttributeStorage(),
        searchable=1,
    ),
    FileField(
        name='file9',
        widget=FileField._properties['widget'](
            label="Resource 9",
            label_msgid='ILOIntranetTypes_label_file9',
            i18n_domain='ILOIntranetTypes',
        ),
        storage=AttributeStorage(),
        searchable=1,
    ),
    FileField(
        name='file10',
        widget=FileField._properties['widget'](
            label="Resource 10",
            label_msgid='ILOIntranetTypes_label_file10',
            i18n_domain='ILOIntranetTypes',
        ),
        storage=AttributeStorage(),
        searchable=1,
    ),

),
)

##code-section after-local-schema #fill in your manual code here

schema._fields['office'].widget = SelectionWidget(
                            label = "ILO office of last assignment",
                            description = "Please select office you last worked in.")

##/code-section after-local-schema

StaffKnowledgeTransfer_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class StaffKnowledgeTransfer(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IStaffKnowledgeTransfer)

    meta_type = 'StaffKnowledgeTransfer'
    _at_rename_after_creation = True

    schema = StaffKnowledgeTransfer_schema

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



registerType(StaffKnowledgeTransfer, PROJECTNAME)
# end of class StaffKnowledgeTransfer

##code-section module-footer #fill in your manual code here
##/code-section module-footer

