from five import grok
from Products.ATContentTypes.interfaces.topic import IATTopic
import json
from plone.memoize import ram
from time import time
from Products.CMFCore.utils import getToolByName
import calendar
from Products.AdvancedQuery import Or, Between
from datetime import datetime
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
import urllib
grok.templatedir('templates')

class MapView(grok.View):
    grok.context(IATTopic)
    grok.name('map_view')
    grok.template('map_view')

    def months(self):
        thismonth = datetime.now().month
        month = int(self.request.get('month', thismonth))
        return [{'value': i, 'name': n,
            'selected': i == month} for i, n in enumerate(
            calendar.month_name) if i
        ]

    def monthText(self):
        month = self.month()
        return calendar.month_name[month].upper()

    def month(self):
        thismonth = datetime.now().month
        return int(self.request.get('month', thismonth))

    def themes(self):
        themes = getUtility(IVocabularyFactory, name='ilo.vocabulary.themes')(self.context)
        theme = self.request.get('theme', 'All')
        result = [{
            'value': i.value,
            'name': i.value,
            'selected': i.value == theme} for i in themes
        ]
        result.insert(0, {'value': 'All', 'name': 'All', 'selected': theme == 'All'})
        return result

    def offices(self):
        offices = getUtility(IVocabularyFactory, name='ilo.vocabulary.offices')(self.context)
        office = self.request.get('office', 'All')
        result = [{
            'value': i.value,
            'name': i.value,
            'selected': i.value == office} for i in offices
        ]
        result.insert(0, {'value': 'All', 'name': 'All', 'selected': office == 'All'})
        return result

    def map_embed_url(self):
        now = datetime.now()
        month = int(self.request.get('month', now.month))
        year = int(self.request.get('year', now.year))
        office = self.request.get('office', None)
        theme = self.request.get('theme', None)
        data = {'month': month, 'year': year}
        if office and office != 'All':
            data['office'] = office
        if theme and theme != 'All':
            data['theme'] = theme
        return '%s/map_embed?%s' % (self.context.absolute_url(), urllib.urlencode(data))

class MapEmbed(grok.View):
    grok.context(IATTopic)
    grok.name('map_embed')
    grok.template('map_embed')

    def js(self):
        now = datetime.now()
        month = int(self.request.get('month', now.month))
        year = int(self.request.get('year', now.year))
        office = self.request.get('office', None)
        theme = self.request.get('theme', None)
        data = {'month': month, 'year': year}
        if office and office != 'All':
            data['office'] = office
        if theme and theme != 'All':
            data['theme'] = theme

        return '''
            $(function () {
                config = {
                    icons: ["http://maps.google.com/mapfiles/ms/icons/red-dot.png",
                    "http://maps.google.com/mapfiles/ms/icons/green-dot.png",
                    "http://maps.google.com/mapfiles/ms/icons/blue-dot.png",
                    "http://maps.google.com/mapfiles/ms/icons/orange-dot.png",
                    "http://maps.google.com/mapfiles/ms/icons/purple-dot.png",
                    "http://maps.google.com/mapfiles/ms/icons/pink-dot.png",
                    "http://maps.google.com/mapfiles/ms/icons/yellow-dot.png"],
                    skip_keywords: ['Other Regions']
                };
            
                initializeMap("map", '%(jsonurl)s?%(query)s', config);
            });
        ''' % {
            'jsonurl': '%s/mapdata.json' % self.context.absolute_url(),
            'query': urllib.urlencode(data)
        }

class MapJsonView(grok.View):
    grok.context(IATTopic)
    grok.name('mapdata.json')

    def render(self):
        now = datetime.now()
        month = int(self.request.get('month', now.month))
        year = int(self.request.get('year', now.year))
        theme = self.request.get('theme', None)
        office = self.request.get('office', None)
        return self._get_json(month, year, office, theme)

    def _get_json(self, month, year, office=None, theme=None):
        self.request.response.setHeader('Content-type', 'application/json')
        catalog = getToolByName(self.context, 'portal_catalog')
        finalday = calendar.monthrange(year, month)[1]
        q = self.context.buildQuery()
        if office and office != 'All':
            q['office'] = office
        if theme and theme != 'All':
            q['theme'] = theme
        query = catalog.makeAdvancedQuery(q)
        query &= Or(
            Between('start',
                datetime(year, month, 1),
                datetime(year, month, finalday)
            ),
            Between('end',
                datetime(year, month, 1),
                datetime(year, month, finalday)
            )
        )

        brains = catalog.evalAdvancedQuery(query)
        
        result = []

        for brain in brains:
            b = brain.getObject()
            if not b.mission_event_location:
                continue
            country = b.mission_event_location
            if country == 'HQ':
                country = 'Switzerland'
            item = {
                'title': b.Title(),
                'description': b.Description(),
                'members': b.members,
                'startDate': b.startDate.strftime("%d %b %Y"),
                'endDate': b.endDate.strftime("%d %b %Y"),
                'office': b.office,
                'theme': b.theme,
                'url': b.absolute_url(),
                'country': country,
                'city': b.city,
                'latlng': ''
            }
            result.append(item)

        return json.dumps(result[:20])
