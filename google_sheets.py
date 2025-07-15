
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def get_gsheet_client(json_keyfile):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(json_keyfile, scope)
    client = gspread.authorize(creds)
    return client

def log_progress_to_sheet(sheet, username, module, score):
    sheet.append_row([username, module, score])
