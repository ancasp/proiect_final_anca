# Aplicație de Automatizare a Sarcinilor: Dezvoltă o aplicație care să automatizeze sarcini repetitive, precum
# gestionarea fișierelor, extragerea de date din pagini web sau trimiterea de e-mailuri automate.
# Pentru a dezvolta o astfel de aplicație, va trebui să aveți instalate Python și câteva biblioteci Python utile.
# Puteți instala aceste biblioteci utilizând pip: pip install selenium, requests, smtplib - nu merge, cica il are python

from selenium import webdriver
import requests
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configurarea Selenium pentru browser
browser = webdriver.Chrome()
browser.get('https://www.zf.ro/')  # Schimbați URL-ul cu site-ul dvs. de interes

# Extragere titluri de știri de pe site
titles = browser.find_element('xpath', "news-title")
news_titles = [title.text for title in titles]



# Închidere browser Selenium
browser.quit()
# Configurare detalii pentru e-mail
email_address = 'ancaa.spirea@gmail.com'  # Adresa de e-mail de la care veți trimite
email_password = 'Parola1@'  # Parola pentru adresa de e-mail
recipient_email = 'anca.spirea@yahoo.com'  # Adresa destinatarului
subject = 'Știri zilnice'

# Creare și trimitere e-mail
msg = MIMEMultipart()
msg['From'] = email_address
msg['To'] = recipient_email
msg['Subject'] = subject

body = "\n".join(news_titles)
msg.attach(MIMEText(body, 'plain'))
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_address, email_password)
    server.sendmail(email_address, recipient_email, msg.as_string())
    server.quit()
    print("E-mail trimis cu succes!")
except Exception as e:
    print("Eroare la trimiterea e-mailului:", str(e))

