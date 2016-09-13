#! /usr/bin/env python

import smtplib


myem = "projectjarvis76@gmail.com"
pasw = "Garfield76"
to = raw_input('number')
msg = raw_input('message')


for i in range(10):
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(myem, pasw)
    server.sendmail(myem, to, msg)
server.quit()
