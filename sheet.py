
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# Connect to Google Sheets
class createsheet:
        def __init__(self):
                
                self.scope = ['https://www.googleapis.com/auth/spreadsheets',
                        "https://www.googleapis.com/auth/drive"]

                self.credentials = ServiceAccountCredentials.from_json_keyfile_name('/home/neer/Desktop/testing/credentials1.json', self.scope)
                self.client = gspread.authorize(self.credentials)
                self.spreadsheet = self.client.create('testing')
        def sheets(self,email):
                with open('data.csv', 'r') as file_obj:
                        self.content = file_obj.read()
                        self.client.import_csv(self.spreadsheet.id, data=self.content)
                        self.spreadsheet.share(email,perm_type='user',role='reader')    

ob1=createsheet()  
ob1.sheets('neer.amrutia@gmail.com')      