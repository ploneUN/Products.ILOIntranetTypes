from archetypes.schemaextender.interfaces import (ISchemaExtender,
                          IOrderableSchemaExtender,
                          IBrowserLayerAwareExtender)

from zope.component import adapts
from zope.interface import implements

from Products.Archetypes.public import BooleanField, AttributeStorage
from archetypes.schemaextender.field import ExtensionField
from Products.PloneBooking.content.schemata import BookingSchema

BookingSchema['description'].schemata = 'default'
BookingSchema['description'].widget.label='Meeting Requirements'
BookingSchema['description'].widget.label_msgid=''
BookingSchema['description'].widget.i18n_domain=''
BookingSchema['description'].widget.description=''
BookingSchema['description'].widget.description_msgid=''


class ExtenderBooleanField(ExtensionField, BooleanField):
    pass

class RequireITCheckboxExtender(object):

    implements(
        IOrderableSchemaExtender,
    )

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return [
            ExtenderBooleanField(
                'require_it',
                storage = AttributeStorage(),
                default=False,
                widget = BooleanField._properties['widget'](
                    label='Require IT services/equipment',
                    description=('Enable to notify Helpdesk about your IT' +
                    ' requirements, otherwise availability of '+
                    'equipment/services will not be guaranteed. Provide '+
                    'details in the comments below (e.g. laptop, projector, '+
                    'videoconferencing, etc.).'+
                    ' Note that this is a tentative request, the actual'+
                    ' availability will be confirmed by a return email from'+
                    'Helpdesk.'
                    )
                ),
                validators=('isRequireITCommentFilled',)
            )
        ]


    def getOrder(self, original):
        original['default'].remove('require_it')
        descindex = original['default'].index('description')
        original['default'].insert(descindex, 'require_it')
        return original
