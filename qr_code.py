import qrcode
img = qrcode.make('mailto:yann24@gmail.com')
img.save('qrcode.png')
