import  smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

mesaj = MIMEMultipart()

mesaj["From"] =  "furkancets@gmail.com"

mesaj["To"] = "furkancets@gmail.com"

mesaj["Subject"] = "Smtp Mail Gönderme"

yazi = """
Smtp ile mail gönderiyorum

Furkan Cetukkaya
"""

mesaj_gövdesi = MIMEText(yazi, "plain")

mesaj.attach(mesaj_gövdesi)

#try:
mail = smtplib.SMTP("smyp.gmail.com", 587)

mail.ehlo()

mail.starttls()

mail.login("","")

mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())

print("Mail başarıyla gönderildi.")

mail.close()

#except:

#    sys.stderr.write("Bir sorun oluştu!")
#    sys.stderr.flush()
