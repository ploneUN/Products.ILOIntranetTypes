from five import grok
from Solgema.fullcalendar.interfaces import ISolgemaFullcalendarMarker
from Products.ATContentTypes.interfaces.topic import IATTopic
from Products.CMFCore.utils import getToolByName
import calendar
from Products.AdvancedQuery import Or, Between
from datetime import datetime
from StringIO import StringIO
from xhtml2pdf.pisa import CreatePDF

grok.templatedir('templates')


def extract_days(start, end, year, month):
    if start.month() == month and end.month() == month:
        return range(start.day(), end.day() + 1)
    elif start.month() == month:
        final = calendar.monthrange(year, month)[1]
        return range(start.day(), final+1)
    elif end.month() == month:
        return range(1, end.day() +1 )
    else:
        raise AssertionError

class MissionTravelBaseView(grok.View):
    grok.baseclass()
    grok.context(IATTopic)

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

    def locations(self):
        now = datetime.now()
        month = int(self.request.get('month', now.month))
        year = int(self.request.get('year', now.year))
        finalday = calendar.monthrange(year, month)[1]
        catalog = getToolByName(self.context, 'portal_catalog')
        query = catalog.makeAdvancedQuery(self.context.buildQuery())
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

        data = {}
        for brain in brains:
            obj = brain.getObject()
            data.setdefault(obj.mission_event_location, {})
            days = extract_days(obj.startDate, obj.endDate, year, month)
            days = [(day, obj) for day in days]
            for member in obj.members:
                member = member.strip()
                if member.lower() in [
                        'none', 'n/a', '-- none --', '--'
                    ]:
                    continue
                data[obj.mission_event_location].setdefault(member, {})
                data[obj.mission_event_location][member].setdefault('days', [])
                data[obj.mission_event_location][member]['days'] += days
                data[obj.mission_event_location][member]['days'] = list(
                    set(data[obj.mission_event_location][member]['days'])
                )

        result = []
        for location, people in sorted(data.items(), key=lambda x:x[0]):
            if not location.strip():
                continue
            peopleresult = []
            for person, info in sorted(people.items(), key=lambda x:x[0]):
                o = {'name': person}
                o.update(info)
                peopleresult.append(o)

            result.append({
                'name': location,
                'people': peopleresult
            })

        return result

    def days(self):
        now = datetime.now()
        month = int(self.request.get('month', now.month))
        year = int(self.request.get('year', now.year))
        finalday = calendar.monthrange(year, month)[1]
        return range(1, finalday + 1)


class MissionTravelView(MissionTravelBaseView):
    grok.name('mission_travel_view')
    grok.template('missiontravel')

class MissionTravelPrintView(MissionTravelBaseView):
    grok.name('mission_travel_view_print')
    grok.require('zope2.View')

    def render(self):
        html = self.context.missiontravel_print(view=self)
        out = StringIO()
        pdf = CreatePDF(html, out, link_callback=self.link_callback)
        result = out.getvalue()
        self.request.response.setHeader('Content-Type','application/pdf')
        self.request.response.setHeader('Content-Length',len(result))
        self.request.response.setHeader('Content-Disposition',
                'inline;filename=%s.pdf' % self.monthText())
        return result

    def link_callback(self, url, rel):
        return url
    
