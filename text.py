import qrcode

text_qrcode = qrcode.make('https://www.linkedin.com/in/richardsantosss/')

print(type(text_qrcode))
print(text_qrcode)
text_qrcode.save('text.png')