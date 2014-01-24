from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName
import logging 
logger = logging.getLogger('missionreport-migrate')



def migrate(site):
    catalog = getToolByName(site, 'portal_catalog')
    missionreports = catalog({'portal_type':'MissionReport'})
    for mr in missionreports:
        obj = mr.getObject()
        logger.info('Migrating %s' % '/'.join(obj.getPhysicalPath()))
        schema = obj.Schema()
 
        field = schema['SummaryAchievements']
        val = field.get(obj)
        val = val.replace('\n', '<br/>')
        field.set(obj, val)
 
 
        # followup
        field = schema['followup']
        fieldstorage = field.getStorage()
        val = fieldstorage.get('followup', obj)
        if hasattr(val, '__iter__'):
            val = ['<ul>'] + ['<li>%s</li>' % i for i in val] + ['</ul>']
            val = '\n'.join(val)
        fieldstorage.set('followup', obj, '')
        field.set(obj, val)
        obj.reindexObject()
    return "DONE"
