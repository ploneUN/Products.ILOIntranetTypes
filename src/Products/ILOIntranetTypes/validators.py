from Products.validation import validation
from Products.validation.interfaces.IValidator import IValidator
from zope.interface import implements

import rfc822

import re

NAME_ADDR_PATTERN=re.compile('(.*?)<(.*?)>')
GROUP_PATTERN=re.compile('Group:.*')

class EmailListValidator(object):
    implements(IValidator)

    def __init__(self, name):
        self.name = name

    def __call__(self, value, *args, **kwargs):
        mailhost = kwargs['instance'].MailHost

        errmsg = "One or more email addresses are invalid"
        for v in value:
            if GROUP_PATTERN.match(v):
                continue

            if NAME_ADDR_PATTERN.match(v):
                name, addr = rfc822.parseaddr(v)
                if not mailhost.validateSingleEmailAddress(addr):
                    return errmsg
            else:
                if not mailhost.validateSingleEmailAddress(v):
                    return errmsg

validation.register(EmailListValidator('isEmailList'))


class ITRequestValidator(object):
    implements(IValidator)

    def __init__(self, name):
        self.name = name

    def __call__(self, value, *args, **kwargs):
        instance = kwargs.get('instance', None)

        errmsg = 'You requested IT services - please provide details of your request in the comments.'

        if isinstance(value, str):
            value = value.lower() == 'true'

        if value:
            if not instance.REQUEST.get('description', '').strip():
                return errmsg

validation.register(ITRequestValidator('isRequireITCommentFilled'))
