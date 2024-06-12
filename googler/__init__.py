from .manager import MakeGoogleConnection
from ..logger import Logger
from ..configloader import Configuration
log = Logger("googler.main")
cfg = Configuration()

log.info(f"Google kapcsolatok ellenörzése folyamatban!")

try:
    sckk_usr = [cfg.getCFG("sckk_usr", "sheet_id"), cfg.getCFG("sckk_usr", "page_name")]
    apms_usr = [cfg.getCFG("apms_usr", "sheet_id"), cfg.getCFG("apms_usr", "page_name")]
    tow_usr = [cfg.getCFG("tow_usr", "sheet_id"), cfg.getCFG("tow_usr", "page_name")]
    log.info("Adatok betöltése a konfigurációs állományból sikeres!")
except Exception as e:
    log.error(f"Hiba az adatok betöltése során! ({str(e)})")

log.info("Kapcsolódás")
for i in [sckk_usr, apms_usr, tow_usr]:
    MakeGoogleConnection(i[0], i[1], monitor=True)