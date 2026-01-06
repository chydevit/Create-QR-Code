import qrcode
#this for add url or text
data = 'hi'

# this function create qr code
img = qrcode.make(data)

#this for add name photo
img.save('po.jpg')