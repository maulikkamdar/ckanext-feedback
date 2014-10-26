import smtplib
import os
import ckan.plugins as p
import pylons.config as config

from ckan.common import request
from ckan.lib.base import BaseController
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders

class FeedbackController(BaseController):
  def feedback(self):
    return p.toolkit.render('feedbackForm.html')

  def feedbackProv(self):
   # assert type(['maulik.kamdar@insight-centre.org'])==list
    requestHandler = config.get('ckan.feedback.request_email', "maulik.kamdar@insight-centre.org") # this should read from config file or send email to default
    senderEmail = config.get('ckan.feedback.sender_email', "admin@system.com") # this should read from config file or send email from default
    msg = MIMEMultipart()
    msg['From'] = senderEmail
    msg['To'] = requestHandler
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = "Dataset Request for " + request.params['datasetName']
    
    dataRequest = "User Name: " + request.params['name'] + "\nUser Email: " + request.params['email'] + "\nOrganization Name: " + request.params['organization'] + "\nDataset Name: " + request.params['datasetName'] + "\nDataset Description: " + request.params['description']
    msg.attach( MIMEText(dataRequest) )
    smtp = smtplib.SMTP('localhost',25)
    smtp.sendmail(senderEmail, requestHandler, msg.as_string() )
    smtp.close()
    return p.toolkit.render('feedbackProv.html')
