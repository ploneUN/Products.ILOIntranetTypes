# -*- coding: utf-8 -*-
#
# File: ILOIntranetBase.py
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

##code-section module-header #fill in your manual code here
from Acquisition import aq_parent
from Products.CMFCore.utils import getToolByName

##/code-section module-header

schema = Schema((

    LinesField(
        name='mission_location',
        widget=MultiSelectionWidget(
            label="Location",
            description="Please select the country (or countries) for this mission. Hold down CTRL to select multiple countries.",
            label_msgid='ILOIntranetTypes_label_mission_location',
            description_msgid='ILOIntranetTypes_help_mission_location',
            i18n_domain='ILOIntranetTypes',
        ),
        searchable=1,
        vocabulary=['Afghanistan','Australia','Bangladesh', 'Bhutan','Brunei','Cambodia', 'China', 'Cook Islands', 'Democratic People\'s Republic of Korea', 'Federated States of Micronesia', 'Fiji', 'India', 'Indonesia', 'Iran', 'Japan', 'Kiribati', 'Lao PDR', 'Malaysia', 'Maldives', 'Marshall Islands', 'Mongolia', 'Myanmar', 'Nauru', 'Nepal','New Zealand', 'Niue', 'Pakistan', 'Palau', 'Papua New Guinea', 'Philippines', 'Republic of Korea', 'Samoa','Singapore', 'Solomon Islands', 'Sri Lanka', 'Thailand', 'Timor-Leste', 'Tokelau', 'Tonga', 'Tuvalu', 'Vanuatu','Viet Nam','HQ','ITC Turin','Other'],
        multiValued=1,
    ),
    LinesField(
        name='theme',
        widget=MultiSelectionWidget(
            label="ILO Themes",
            description="Select the related themes. Hold CTRL to make multiple selections.",
            label_msgid='ILOIntranetTypes_label_theme',
            description_msgid='ILOIntranetTypes_help_theme',
            i18n_domain='ILOIntranetTypes',
            size = 18,
        ),
        vocabulary='theme_vocab',
        multiValued=1,
    ),
    LinesField(
        name='country',
        widget=MultiSelectionWidget(
            label="Country",
            label_msgid='ILOIntranetTypes_label_country',
            i18n_domain='ILOIntranetTypes',
        ),
        searchable=1,
        vocabulary=['Afghanistan','Australia','Bangladesh', 'Bhutan','Brunei','Cambodia', 'China', 'Cook Islands', 'Democratic People\'s Republic of Korea', 'Federated States of Micronesia', 'Fiji', 'India', 'Indonesia', 'Iran', 'Kiribati', 'Lao PDR', 'Malaysia', 'Maldives', 'Marshall Islands', 'Mongolia', 'Myanmar', 'Nauru', 'Nepal','New Zealand', 'Niue', 'Pakistan', 'Palau', 'Papua New Guinea', 'Philippines', 'Republic of Korea', 'Samoa','Singapore', 'Solomon Islands', 'Sri Lanka', 'Thailand', 'Timor-Leste', 'Tokelau', 'Tonga', 'Tuvalu', 'Vanuatu','Viet Nam','Regional'],
        multiValued=1,
    ),
    StringField(
        name='mission_event_location',
        widget=SelectionWidget(
            label='Mission_event_location',
            label_msgid='ILOIntranetTypes_label_mission_event_location',
            i18n_domain='ILOIntranetTypes',
        ),
        vocabulary=['Afghanistan','Australia','Bangladesh', 'Bhutan','Brunei','Cambodia', 'China', 'Cook Islands', 'Democratic People\'s Republic of Korea', 'Federated States of Micronesia', 'Fiji', 'India', 'Indonesia', 'Iran', 'Japan', 'Kiribati', 'Lao PDR', 'Malaysia', 'Maldives', 'Marshall Islands', 'Mongolia', 'Myanmar', 'Nauru', 'Nepal','New Zealand','Niue', 'Pakistan', 'Palau', 'Papua New Guinea', 'Philippines', 'Republic of Korea','Singapore', 'Samoa', 'Solomon Islands', 'Sri Lanka', 'Thailand', 'Timor-Leste', 'Tokelau', 'Tonga', 'Tuvalu', 'Vanuatu','Viet Nam','HQ','ITC Turin','Other'],
        searchable=1,
    ),
    LinesField(
        name='office',
        widget=MultiSelectionWidget(
            label="ILO Office",
            description="Please select office you belong to. Hold down CTRL to select multiple offices.",
            label_msgid='ILOIntranetTypes_label_office',
            description_msgid='ILOIntranetTypes_help_office',
            i18n_domain='ILOIntranetTypes',
        ),
        searchable=1,
        vocabulary='office_vocab',
        multiValued=1,
    ),
    LinesField(
        name='iib_countries',
        widget=MultiSelectionWidget(
            label="Country Covered",
            description="Countries covered by this report. Hold down CTRL to select multiple countries.",
            label_msgid='ILOIntranetTypes_label_iib_countries',
            description_msgid='ILOIntranetTypes_help_iib_countries',
            i18n_domain='ILOIntranetTypes',
        ),
        vocabulary=['Afghanistan','Bangladesh', 'Bhutan', 'Cambodia', 'China', 'Cook Islands', 'Democratic People\'s Republic of Korea', 'Federated States of Micronesia', 'Fiji', 'India', 'Indonesia', 'Iran','Japan', 'Kiribati', 'Lao PDR', 'Malaysia', 'Maldives', 'Marshall Islands', 'Mongolia', 'Myanmar', 'Nauru', 'Nepal', 'Niue', 'Pakistan', 'Palau', 'Papua New Guinea', 'Philippines', 'Republic of Korea','Singapore', 'Samoa', 'Solomon Islands', 'Sri Lanka', 'Thailand', 'Timor-Leste', 'Tokelau', 'Tonga', 'Tuvalu', 'Vanuatu','Viet Nam','HQ','ITC Turin','Other'],
        multiValued=1,
    ),
    LinesField(
        name='members',
        widget=LinesField._properties['widget'](
            label="Mission Members",
            description="List of Mission Members. One name per line with principal member first.",
            label_msgid='ILOIntranetTypes_label_members',
            description_msgid='ILOIntranetTypes_help_members',
            i18n_domain='ILOIntranetTypes',
        ),
        searchable=1,
        required=1,
    ),
    StringField(
        name='domestic',
        widget=SelectionWidget(
            label="Mission Type",
            description="Please select whether this was a domestic or international mission",
            label_msgid='ILOIntranetTypes_label_domestic',
            description_msgid='ILOIntranetTypes_help_domestic',
            i18n_domain='ILOIntranetTypes',
        ),
        vocabulary=['Domestic','International'],
        required=1,
    ),
    LinesField(
        name='administrative_unit',
        widget=MultiSelectionWidget(
            label="Administrative Unit",
            description="Select Administrative Unit(s). Hold down CTRL to select multiple entries.",
            label_msgid='ILOIntranetTypes_label_administrative_unit',
            description_msgid='ILOIntranetTypes_help_administrative_unit',
            i18n_domain='ILOIntranetTypes',
        ),
        multiValued=1,
        searchable=True,
        vocabulary=['RO - Asia and the Pacific','CO- Bangkok','CO - Beijing','CO - Colombo','CO - Dhaka','CO - Hanoi','CO - Islamabad','CO - Jakarta','CO - Kathmandu','CO - Manila','CO - Suva','DWT/CO - New Delhi','DWT - Bangkok','ILO - Kabul','ILO - Phnom Penh','ILO - Yangon','HQ','ITC-ILO','ACT/EMP', 'ACTRAV', 'CABINET', 'CODEV', 'DCOMM', 'DECLARATION', 'DGREPORTS', 'DIALOGUE', 'EDMAS', 'EIIP', 'EMP/ANALYSIS', 'EMP/CEPOL', 'EMP/COOP', 'EMP/ELM', 'EMP/ENTERPRISE', 'EMP/MULTI', 'EMP/POLICY', 'EMP/SEED', 'EMP/SKILLS', 'EMP/TRENDS', 'ETHICS', 'EVAL', 'FINANCE', 'GENDER', 'HRD', 'IAO', 'ILO/AIDS', 'ILO/CRISIS', 'INST', 'INTEGRATION', 'INTER', 'IPEC', 'ITCOM', 'JUR', 'LAB/ADMIN', 'MIGRANT', 'NORMES', 'PARDEV', 'PROGRAM', 'PROTECTION', 'PROTRAV', 'Procurement', 'REGIONS', 'SECSOC', 'SECTOR', 'STANDARDS', 'STAT', 'STEP', 'SafeWork', 'TRAVAIL',],
    ),
    LinesField(
        name='technical_unit',
        widget=MultiSelectionWidget(
            label="Technical Unit",
            description="Select Technical Unit(s). Hold down CTRL to select multiple entries.",
            label_msgid='ILOIntranetTypes_label_technical_unit',
            description_msgid='ILOIntranetTypes_help_technical_unit',
            i18n_domain='ILOIntranetTypes',
        ),
        multiValued=1,
        searchable=True,
        vocabulary=['RO - Asia and the Pacific','CO- Bangkok','CO - Beijing','CO - Colombo','CO - Dhaka','CO - Hanoi','CO - Islamabad','CO - Jakarta','CO - Kathmandu','CO - Manila','CO - Suva','DWT/CO - New Delhi','DWT - Bangkok','ILO - Kabul','ILO - Phnom Penh','ILO - Yangon','HQ','ITC-ILO','ACT/EMP', 'ACTRAV', 'CABINET', 'CODEV', 'DCOMM', 'DECLARATION', 'DGREPORTS', 'DIALOGUE', 'EDMAS', 'EIIP', 'EMP/ANALYSIS', 'EMP/CEPOL', 'EMP/COOP', 'EMP/ELM', 'EMP/ENTERPRISE', 'EMP/MULTI', 'EMP/POLICY', 'EMP/SEED', 'EMP/SKILLS', 'EMP/TRENDS', 'ETHICS', 'EVAL', 'FINANCE', 'GENDER', 'HRD', 'IAO', 'ILO/AIDS', 'ILO/CRISIS', 'INST', 'INTEGRATION', 'INTER', 'IPEC', 'ITCOM', 'JUR', 'LAB/ADMIN', 'MIGRANT', 'NORMES', 'PARDEV', 'PROGRAM', 'PROTECTION', 'PROTRAV', 'Procurement', 'REGIONS', 'SECSOC', 'SECTOR', 'STANDARDS', 'STAT', 'STEP', 'SafeWork', 'TRAVAIL',],
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

ILOIntranetBase_schema = schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class ILOIntranetBase(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IILOIntranetBase)

    _at_rename_after_creation = True

    schema = ILOIntranetBase_schema

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


# end of class ILOIntranetBase

##code-section module-footer #fill in your manual code here
##/code-section module-footer

