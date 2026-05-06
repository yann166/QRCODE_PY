import qrcode
img = qrcode.make('google.com')
img.save('qrcode.png')
