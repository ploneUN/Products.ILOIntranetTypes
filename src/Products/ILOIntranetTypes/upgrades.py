from plone.app.upgrade.utils import loadMigrationProfile
from Products.CMFCore.utils import getToolByName

def to4100(context, logger=None):
    loadMigrationProfile(context, 'profile-Products.ILOIntranetTypes:to4100')
    catalog = getToolByName(context, 'portal_catalog')
    for brain in catalog({'portal_type': 'ILOEvent'}):
        obj = brain.getObject()
        obj.reindexObject(idxs=['to_remind'])
    return
