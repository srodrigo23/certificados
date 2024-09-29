
###
# 'http://www.dtic.umss.edu.bo/curso-de-ofimatica-con-microsoft-365-2o-version/'
###
from datetime import datetime as dt

def create_qr(url:str, code:str, date:str, path_to_save:str)->str:
  import segno, os
  qrcode = segno.make_qr(f"{url}/{code}")
  qrcode.save(
    os.path.join(path_to_save, f"{date}_{code}.png")
  )


create_qr(
  url='http://www.dtic.umss.edu.bo/curso-de-ofimatica-con-microsoft-365-2o-version',
  code='1123ADNC32122',
  date=f"{dt.now().year}-{dt.now().month}-{dt.now().day}",
  path_to_save='./reports'
)