import gspread
from oauth2client.service_account import ServiceAccountCredentials
from ..logger import Logger
log = Logger("googler.main")


class MakeGoogleConnection:
    def __init__(self, sheet_id, worksheet_name, monitor=False):
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        credentials_path = "/home/linux/SCMS/api_scms/api_scms/credentials.json"
        try:
            credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_path, scope)
            client = gspread.authorize(credentials)
            sheet = client.open_by_key(sheet_id)
            self.worksheet = sheet.worksheet(worksheet_name)
            if monitor:
                log.info(f"Kapcsoalt sikeresen lértejött! ({self.worksheet})")
        except Exception as e:
            log.error(f"Hiba a kapcsolódás során! ({str(e)})")
    def GetRanges(self, ranges):
        try:
            return self.worksheet.batch_get(ranges)
        except Exception as e:
            log.error(f"Hiba az adatok lekérdezése során! ({str(e)})")