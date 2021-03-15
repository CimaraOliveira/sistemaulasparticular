
from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.template.loader import get_template
from django.views.generic import View

from sistemaulas.utils import render_to_pdf
from disciplina.models import Usuario


class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        usuarioDisc = Usuario.objects.order_by('username').filter(username=self.request.user)
        data = {'usuarioDiscs': usuarioDisc}

        pdf = render_to_pdf('relatorio/invoice.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('relatorio/invoice.html')

        context = {
            "invoice_id": 123,
            "customer_name": "John Cooper",
            "amount": 1399.99,
            "today": "Today",
        }
        html = template.render(context)
        pdf = render_to_pdf('relatorio/invoice.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" % ("12341231")
            content = "inline; filename='%s'" % (filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" % (filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")


def write_pdf_view(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="mypdf.pdf"'

    buffer = BytesIO()
    p = canvas.Canvas(buffer)

    # Start writing the PDF here
    p.drawString(100, 100, 'Hello world.')
    # End writing

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response