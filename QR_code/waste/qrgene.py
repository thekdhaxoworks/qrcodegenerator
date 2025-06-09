import qrcode
qr=qrcode.make("visit our official website through the below link")
data="https://tkrec.ac.in"
qr=qrcode.make(data)
qr.save("docupy.png")
qr.show()