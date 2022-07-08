import qrcode
#import image
qr=qrcode.QRCode(
  version=15,#version of qr code, high the number more image will be complexed and big
  box_size=10,#size of box in which qr code will be displayed
  border=5) #white part of image
data="FIRST INSTALL IMAGE AND QRCODE USING (pip install qrcode --user) and (pip install image --user). NOW USE VISUAL STUDIO CODE TO RUN THIS FILE AND WE CAN GIVE ANY PATH IN THE URL AS WE WANT. I HAVE PROVIED QR CODE FOR AN TEXT."

qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color="white")
img.save("deletetest.png")