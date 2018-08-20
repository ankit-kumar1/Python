import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
import psycopg2
from sqlalchemy import create_engine
import pandas
from datetime import datetime, timedelta

now = datetime.now()
datepart = "%d%02d%02d"%(now.year,now.month,now.day)
engine = create_engine('postgres://user:pswd@localhost:1234/database')
data_frame = pandas.read_sql_query("select * from sales query;", engine)

data_frame.abs_period = data_frame.abs_period.apply('"{}"'.format)
print data_frame['abs_period']
print data_frame.dtypes


data_frame.to_csv("/Users/ankitkumar/Weekly_Sales - "+datepart+".csv")

fromaddr = "abc.xyz@gmail.com"
toaddr = ['ankit@plated.com', 'steven@facebook.com', 'absx@google.com']

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = ", ".join(toaddr)
msg['Subject'] = "Weekly Sales - "+datepart

body = "FYI,find attachment!"

msg.attach(MIMEText(body, 'plain'))


filename = "Weekly_Sales - "+datepart+".csv"
attachment = open("/Users/ankitkumar/"+filename, "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "apppassword")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
