import segno


url = 'http://www.dtic.umss.edu.bo/curso-de-ofimatica-con-microsoft-365-2o-version/'
qrcode = segno.make_qr(url)
qrcode.save("code.png")


