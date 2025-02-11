import cgi
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Holen der Formulardaten
form = cgi.FieldStorage()
name = form.getvalue('name')
email = form.getvalue('email')
message = form.getvalue('message')

# E-Mail-Details
sender_email = "erik.spinnler84@gmail.com"  # Deine E-Mail
receiver_email = "erik.spinnler12@icloud.com"  # Ziel-E-Mail
password = "Erik_spinnler12"  # Dein E-Mail Passwort

# Erstellen der Nachricht
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = "Neue Nachricht vom Kontaktformular"

body = f"Name: {name}\nE-Mail: {email}\nNachricht: {message}"
msg.attach(MIMEText(body, 'plain'))

# E-Mail senden
try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
    print("Content-type: text/html\n")
    print("<h2>Die Nachricht wurde erfolgreich gesendet!</h2>")
except Exception as e:
    print("Content-type: text/html\n")
    print(f"<h2>Fehler: {str(e)}</h2>")

