from django.core.management.base import BaseCommand, CommandError
import pandas as pd


class Command(BaseCommand):
    help = 'Generate statement'

    #Identify the html elements that need to be dynamic

    def add_arguments(self, parser):
        parser.add_argument('account_no', nargs='+', type=int)

    def handle(self, *args, **options):
        df = pd.read_csv('/Users/komu/projects/codeke/MP312_consumers_master_20220622_010001.csv')
        #get the unique account numbers f rom the pandas

        # for each unique account number render the html into a file
        #Convert the file into pdf
        print(df.head())
