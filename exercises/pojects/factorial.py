import qrcode

a = qrcode.make('https://www.youtube.com/watch?v=41Nck7hRrEA&t=3s')
a.save('qrcode.png')