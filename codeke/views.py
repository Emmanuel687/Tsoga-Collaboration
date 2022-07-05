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
            "office_hours":"Mon to Thursday 7:30 to 16:30 Friday 07:30 to 13:30",
            "payment_hours":"Mon to Thursday 7:30 to 16:30 Friday  07:30 to 12:30",
            "kwaguqa":"Tel:(013) 698-0262 Fax:(013)690-6207",
            "oggies":"(013) 643-1027 Fax:(013)690-2039",
            
           
            "account_number":"00040239",
            "consumer_name": "THOMAS NTHABISENG MOKONENI",
            "postal_address":"KWA-GUQA EXT 7 ERF NO 4114 WITBANK",
            "postal_code":1038,
            "interest_pin":353579124,
           

            "account_date":" 22 Jan 2022",
            "tax_invoice": "0004002393022201",
            "vat_registration":0,
            "erf_description":"51007 000004114 0000 0000 0000",
            "market_value":"390,000.00",
            "street_Id":"KWA EXT 7,4114",
            "land_area":300.000,
            "deposit_amount":0.00,

            "meter_no":"0000001024",
            "meter_type":"PRE-PAID" ,
            "old_reading":.000,
            "new_reading": ".000 N",
            "consumptions": .000,
            "levied_amount":0.0, 
            "reading_dates":"-",

            "date":"",
            "code":"",
            "description":"OPENING BALANCE",
            "units":"",
            "tariff":"",
            "value":"110,223.60", 

            "date_1":"23/01/2022",
            "code_1":"00S023",
            "description_1":"SEWERAGE",
            "units_1":1.000,
            "tariff_1":"",
            "value_1":219.47, 

            "date_2":"23/01/2022",
            "code_2":"00w008",
            "description_2":"WATER",
            "units_2":1.000,
            "tariff_2":"",
            "value_2":516.76, 

            "date_3":"23/01/2022",
            "code_3":"00S023",
            "description_3":"RATES",
            "units_3":1.000,
            "tariff_3":"",
            "value_3":362.09, 

            "date_4":"23/01/2022",
            "code_4":"00R007",
            "description_4":"REFUSE",
            "units_4":"",
            "tariff_4":"",
            "value_4":164.00, 


            "date_5":"",
            "code_5":"00S023",
            "description_5":"VAT",
            "units_5":"",
            "tariff_5":"",
            "value_5":135.03, 

            "date_6":"",
            "code_6":"009008",
            "description_6":"INTEREST",
            "units_6":"",
            "tariff_6":"",
            "value_6":493.53, 
             

            "days_1":"104,595.12",
            "days_2":"1,868.79",
            "days_3":"1,876.16",
            "days_4":"1,883.53",
            "days_5":"1,890.88",
            "days_6":"112,114.48",

            "account_name":"004002393",
            "consumer_name":"THOMAS NTHABISENG MOKONENI",
            "total_due":"112 114.48",
            "total_due_before":"07/02/2022",

            "bank_name":"ABSA",
            "account_name":"Emalahleni Local Municipality",
            "branch_code":509-750,
            "reference":"0004002393"


            








            
            
              


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

