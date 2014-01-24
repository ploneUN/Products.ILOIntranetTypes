from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

class UpdateBooking(BrowserView):
    def render(self):
        request = self.request
        ptool = getToolByName(self.context, 'portal_properties')
        charset = ptool.site_properties.default_charset
        request.response.setHeader(
            'Content-type', 'text/plain; charset=%s' % charset
        )
        kwargs = request.form

        errorMessages = ''

        fieldsToValidate = ['fullName', 'phone', 'email', 'require_it']
        for fieldName in fieldsToValidate:
            if kwargs.has_key(fieldName):
                field = self.context.getField(fieldName)
                result = field.validate(kwargs[fieldName], self.context, errors={})
                if result:
                    errorMessages += '\n' + result

        if errorMessages:
            btool = getToolByName(self.context, 'portal_booking')
            return "%s:%s%s" % (
                btool.zdt2ts(self.context.getStartDate()),
                btool.zdt2ts(self.context.getEndDate()),
                errorMessages
            )

        if kwargs.has_key('require_it'):
            if kwargs.get('require_it').lower() == 'true':
                kwargs['require_it'] = True
            else:
                kwargs['require_it'] = False

        result = self.context.updateBooking(request)

        return result
