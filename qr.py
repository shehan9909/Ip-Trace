import os
import qrcode
data = "https://github.com/shehan9909"
input_data = data
qr=qrcode.QRCode(version=1,box_size=10,border=5)
qr.add_data(input_data)
qr.make(fit=True)
img=qr.make_image(fill='black',back_color='white')
img.save('qrcode001.png')
# Created by pyminifier (https://github.com/liftoff/pyminifier)
os.system("termimage qrcode001.png")
