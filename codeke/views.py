from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .utils import render_to_pdf
from django.template.loader import get_template

# Create your views here.
# def index(request):
#     return render(request,'index.html')

class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('index.html')
        context = {
            "invoice_id": 123,
            "customer_name": "John Cooper",
            "amount": 1399.99,
            "today": "Today",
        }
        html = template.render(context)
        return HttpResponse(html)

        