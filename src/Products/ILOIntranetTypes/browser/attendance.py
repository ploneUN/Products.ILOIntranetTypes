from five import grok
from plone.app.layout.viewlets.interfaces import IAboveContentBody
from Products.ILOIntranetTypes.interfaces import IILOEvent
from Products.CMFCore.interfaces import ISiteRoot
from email import message_from_string
from zope.component.hooks import getSite
from DateTime import DateTime
import json
from five import grok
from plone.directives import form
from iloksp.caching.utils import purge
import logging 
log = logging.getLogger("ilo.eventreminder")
grok.templatedir('templates')

class AttendanceViewlet(grok.Viewlet):
    grok.name('ilointranettypes.attendanceviewlet')
    grok.context(IILOEvent)
    grok.require('zope2.View')
    grok.viewletmanager(IAboveContentBody)
    grok.template('attendanceviewlet')

    def update(self):
        pass

    def attending(self):
        user = self.context.portal_membership.getAuthenticatedMember().getId()
        if user in self.context.getField('attendees').get(self.context):
            return True
        if user in self.context.getField('invited_users').get(self.context):
            return False
        return None
            

class UpdateAttendance(grok.View):
    grok.context(IILOEvent)
    grok.name('update_attendance')
    grok.require('zope2.View')
    
    def render(self):
        if self.request.get('attending') and self.request.method == 'POST':
            self.attending()
        elif self.request.get('notattending') and self.request.method == 'POST':
            self.notattending()
        purge(self.context)
        self.request.response.redirect(self.context.absolute_url())

    def attending(self):
        user = self.context.portal_membership.getAuthenticatedMember().getId()
        field = self.context.getField('attendees')
        vals = list(field.get(self.context))
        if user not in vals:
            vals.append(user)
            field.set(self.context, vals)

    def notattending(self):
        user = self.context.portal_membership.getAuthenticatedMember().getId()
        field = self.context.getField('attendees')
        vals = list(field.get(self.context))
        if user in vals:
            vals.remove(user)
            field.set(self.context, vals)

class TickReminder(grok.View):
    grok.context(ISiteRoot)
    grok.name('attendancereminder_tick_and_remind')
    grok.require('cmf.ManagePortal')

    def render(self):
        brains = self.context.portal_catalog({
            'object_provides': IILOEvent.__identifier__,
            'to_remind': True
        })

        sent_obj = 0
        sent_users = 0
        today = DateTime().asdatetime()
        for brain in brains:
            obj = brain.getObject()

            if obj.getField('reminder_sent').get(obj):
                continue

            startDate = obj.getField('startDate').get(obj)
            if not startDate:
                continue

            startDate = startDate.asdatetime()
            if (startDate - today).days >= 7:
                continue

            # remind owner
            creator = obj.Creator()
            self.send_owner_reminder(obj, creator)

            # remind attendees
            attendees = obj.getField('attendees').get(obj)
            for user in set(attendees):
                self.send_reminder(obj, user)
                sent_users += 1
            obj.getField('reminder_sent').set(obj, True)
            obj.reindexObject(idxs=['to_remind'])
            sent_obj += 1

        return 'Sent reminders of %s objects. %s emails sent in total' %  (
                                                            sent_obj,
                                                            sent_users)

    def send_reminder(self, obj, user):
        mt = self.context.portal_membership
        member = mt.getMemberById(user)
        if member is None:
            log.info("User %s does not exist" % user)
            return

        site = getSite()

        encoding = site.getProperty('email_charset', 'utf-8')
        data = self.extract_memberdata(member)
        attendcount = len(obj.attendees)
        mail_text = obj.event_attendance_reminder(
            user=data,
            portal=site,
            content=self.context,
            charset=encoding,
            member=member,
            attendcount=attendcount
        )

        message_obj = message_from_string(mail_text)
        mTo = message_obj['To']
        mFrom = message_obj['From']
        subject = message_obj['Subject']

        site.MailHost.send(mail_text, mTo, mFrom, subject=subject,
                        charset=encoding)

    def send_owner_reminder(self, obj, user):
        mt = self.context.portal_membership
        member = mt.getMemberById(user)
        if member is None:
            log.info("User %s does not exist" % user)
            return

        site = getSite()

        encoding = site.getProperty('email_charset', 'utf-8')
        data = self.extract_memberdata(member)
        attendcount = len(obj.attendees)
        mail_text = obj.event_owner_reminder(
            user=data,
            portal=site,
            content=self.context,
            charset=encoding,
            member=member,
            attendcount=attendcount
        )

        message_obj = message_from_string(mail_text)
        mTo = message_obj['To']
        mFrom = message_obj['From']
        subject = message_obj['Subject']

        site.MailHost.send(mail_text, mTo, mFrom, subject=subject,
                        charset=encoding)

    def extract_memberdata(self, member):
        return {
            'email': member.getProperty('email'),
            'fullname': member.getProperty('fullname'),
            'id': member.getId()
        }


class AttendeeList(grok.View):
    grok.context(IILOEvent)
    grok.name('attendee_list')
    grok.require('zope2.View')
    grok.template('attendee_list')
    

    def invited_users(self):
        mt = self.context.portal_membership
        result = []
        for mid in self.context.getField('invited_users').get(self.context):
            member = mt.getMemberById(mid)
            if member:
                result.append(self.extract_memberdata(member))
        return result

    def attendees(self):
        mt = self.context.portal_membership
        result = []
        for mid in self.context.getField('attendees').get(self.context):
            member = mt.getMemberById(mid)
            if member:
                result.append(self.extract_memberdata(member))
        return result


    def update(self):
        if self.request.method == 'POST':
            new_invites = [i for i in self.request.get('invited_users'
                            ).split(',') if i]
            field = self.context.getField('invited_users')
            invites = list(field.get(self.context))
            for new_invite in new_invites:
                if new_invite in invites:
                    continue
                invites.append(new_invite)
                self.send_invite_email(new_invite)
            field.set(self.context, invites)
            self.context.reindexObject()

    def send_invite_email(self, user):
        obj = self.context
        mt = self.context.portal_membership
        member = mt.getMemberById(user)
        if member is None:
            log.info("User %s does not exist" % user)
            return

        site = getSite()

        encoding = site.getProperty('email_charset', 'utf-8')
        data = self.extract_memberdata(member)
        mail_text = obj.event_invite_email(
            user=data,
            portal=site,
            content=self.context,
            charset=encoding,
            member=member,
        )

        message_obj = message_from_string(mail_text)
        mTo = message_obj['To']
        mFrom = message_obj['From']
        subject = message_obj['Subject']

        site.MailHost.send(mail_text, mTo, mFrom, subject=subject,
                        charset=encoding)

    def extract_memberdata(self, member):
        fullname = member.getProperty('fullname')
        if not fullname:
            fullname = member.getId()
        return {
            'email': member.getProperty('email'),
            'fullname': fullname,
            'jobtitle': member.getProperty('jobtitle'),
            'office': member.getProperty('office'),
            'id': member.getId()
        }


MAX_RESULTS=10
class AttendeeSource(grok.View):
    grok.context(IILOEvent)
    grok.name('attendee-source.json')
    grok.require('zope2.View')

    def _extract_data(self, user):
        return {
            'value': user['userid'],
            'name': '%s (%s)' % (user['title'], user['email'])
        }

    def render(self):
        search_view = self.context.restrictedTraverse('@@pas_search')
        query = self.request.get('q')
        users = search_view.searchUsers(fullname=query)[:MAX_RESULTS]
        return json.dumps([
            self._extract_data(user) for user in (users
            ) if (user['userid'] not in self.context.attendees and
                user['userid'] not in self.context.invited_users)])
