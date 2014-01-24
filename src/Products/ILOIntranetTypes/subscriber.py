from five import grok
from zope.lifecycleevent import IObjectModifiedEvent
from Products.ILOIntranetTypes.interfaces import IMissionReport
from plone import api
import re

@grok.subscribe(IMissionReport, IObjectModifiedEvent)
def expand_group(obj, event):
    values = []
    pattern = re.compile('Group:.*')
    for entry in (obj.distribution or []):
        if pattern.match(entry):
            groupid = entry.split(':', 1)[1]
            users = api.user.get_users(groupname=groupid)
            for user in users:
                values.append('%s <%s>' % (
                    user.getProperty('fullname'),
                    user.getProperty('email')
                ))
    distribution = [i for i in (obj.distribution or []) if not (
        pattern.match(entry))] + values

    obj.distribution = list(set(distribution))
