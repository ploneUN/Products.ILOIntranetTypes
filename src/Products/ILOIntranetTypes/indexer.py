from plone.indexer.decorator import indexer
from Products.ILOIntranetTypes.interfaces import IILOEvent
from DateTime import DateTime

@indexer(IILOEvent)
def to_remind(obj):
    if obj.reminder_sent:
        return False
    if getattr(obj, 'attendees', []) or getattr(obj, 'invited_users', []):
        startDate = obj.Schema()['startDate'].get(obj)
        if startDate and startDate > DateTime():
            return True
    return False
