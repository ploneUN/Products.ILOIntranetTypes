from Products.Five import BrowserView
from Products.ILOIntranetTypes.migration import migrate

class Migrate(BrowserView):

    def render(self):
        return migrate(self.context)
