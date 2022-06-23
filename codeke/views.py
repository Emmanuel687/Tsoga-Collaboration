from django.shortcuts import render
import pandas as pd


# Create your views here.
def index(request):
    return render(request, 'index.html')


def statement(request):
    df = pd.read_csv('/Users/komu/projects/codeke/MP312_consumers_master_20220622_010001.csv')

    print(df.to_string())
    return render(request, 'index.html')
