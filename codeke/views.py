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
        pdf = render_to_pdf("index.html",context)
        return HttpResponse(pdf,content_type='application/pdf')

        

# import pandas as pd


# Create your views here.
# def index(request):
#     return render(request, 'index.html')


# def statement(request):
#     df = pd.read_csv('/Users/komu/projects/codeke/MP312_consumers_master_20220622_010001.csv')

#     print(df.to_string())
#     return render(request, 'index.html')

