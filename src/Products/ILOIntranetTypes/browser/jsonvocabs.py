from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from simplejson import dumps as jsondumps
from plone import api

class MultiSelectWithAutoComplete(BrowserView):
    def __call__(self):

        self.request.response.setHeader('Content-type', 'application/json')

        portal_catalog =  getToolByName(self.context, 'portal_catalog')
        portal_membership = getToolByName(self.context, 'portal_membership')

        #FIXME We probably want to return names as in Full Name <email>
        #but have to be careful that it's email header safe for
        #unicode values

        # Grab email addresses from Person content type from
        # collective.contacts
        member_address = [] 
        for member in portal_membership.listMembers():
            member_email = member.getProperty('email')
            member_fullname = member.getProperty('fullname')
            member_complete = '%s <%s>' %(member_fullname,member_email)
            member_address.append(member_complete)


        persons = [ i.getObject() for i in \
                   portal_catalog.searchResults(portal_type='Person') ]

        person_address = []
        for person in persons:

            if person.work_email != '' :
                person_email = person.work_email

                person_name = '%s %s' %(person.getFirstName(),person.getLastName())

                person_complete = '%s <%s>' %(person_name, person_email)
                person_address.append(person_complete)


        # Grab emails from portal members
        groups = ['Group:%s' % g.id for g in api.group.get_groups()]

        return jsondumps(person_address + member_address + groups)

# Placeholders for making other fields autocomplete.
# MisisonMembers will need an additional keyword index on
# field members. Authors will also need to have index added.
#

class MissionMembers(BrowserView):
    def __call__(self):
 
        catalog = getToolByName(self.context, 'portal_catalog')
        members =  catalog.uniqueValuesFor('getMembers')
        results = []
        for member in members:
            if member:
                for mem in member:
                    if mem not in results:
                        results.append(mem)
        
        return jsondumps(results)
# 
# class Authors(BrowserView):
#    def __call__(self):
# 
#        catalog = getToolByName(self.context, 'portal_catalog')
#        results = catalog.uniqueValuesFor('getAuthors')
#        return list(result.s)
