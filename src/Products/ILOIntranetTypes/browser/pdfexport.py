from StringIO import StringIO
from xhtml2pdf.pisa import CreatePDF
from zope.interface import Interface
from five import grok

class PDFExport(grok.View):
    grok.name('pdf_export')
    grok.require('zope2.View')
    grok.context(Interface)

    def render(self):
        layout = self.request.get('layout', None)
        if layout:
            html = self.context.restrictedTraverse(layout)()
        else:
            html = self.context()
        out = StringIO()

        try:
            pdf = CreatePDF(html, out)
        except Exception, e:
            return 'Unable to convert layout to PDF : %s' % str(e)
        result = out.getvalue()
        self.request.response.setHeader('Content-Type','application/pdf')
        self.request.response.setHeader('Content-Length',len(result))
        self.request.response.setHeader('Content-Disposition',
                'inline;filename=%s.pdf' % self.context.__name__)
        return result
