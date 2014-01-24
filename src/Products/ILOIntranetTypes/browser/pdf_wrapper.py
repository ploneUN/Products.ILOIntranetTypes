from five import grok
from Products.ILOIntranetTypes.interfaces import (
    IMissionReport, IMission,
    IILOEvent, IInternalCountryBrief
)

grok.templatedir('templates')

class MissionReportPDFView(grok.View):
    grok.template('mission_report_pdf')
    grok.name('xhtml2pdf_view')
    grok.context(IMissionReport)

class MissionPDFView(grok.View):
    grok.template('mission_pdf')
    grok.name('xhtml2pdf_view')
    grok.context(IMission)

class ILOEventPDFView(grok.View):
    grok.template('iloevent_pdf')
    grok.name('xhtml2pdf_view')
    grok.context(IILOEvent)

class InternalCountryBriefPDFView(grok.View):
    grok.template('cbn_pdf')
    grok.name('xhtml2pdf_view')
    grok.context(IInternalCountryBrief)
