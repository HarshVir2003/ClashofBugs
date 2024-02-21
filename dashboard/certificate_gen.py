import os
import shutil
import tempfile
from tournaments.models import CertificateUser
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


class CertificateGen:

    def __init__(self):
        self.pdf_canvas = None
        self.temp_file = None
        path = os.path.join(os.getcwd(), "certificate", "certificate.pdf")
        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as temp_pdf:
            shutil.copy(path, temp_pdf.name)
            self.temp_file = temp_pdf
            self.pdf_canvas = canvas.Canvas(temp_pdf.name, pagesize=letter)

    def get_certificates_of_user(self, user):
        all_certificates = CertificateUser.objects.filter(user=user, Attained=True)  # get uid of certificate
        certificates = []  # certificate topic and title
        for i in range(len(all_certificates)):
            certificates.append(all_certificates[i].certificate)

        return certificates, all_certificates

    def generate_pdf(self, certificate, User):
        username = User.first_name
        Title = certificate.Title
        topic = certificate.topic
        uid = CertificateUser.objects.get(certificate=certificate, user=User)
        self.pdf_canvas.setFont("", 12)
        self.pdf_canvas.setFillColorRGB(0, 0, 0)
        self.pdf_canvas.drawString(100, 100, username)
        self.pdf_canvas.setFont("", 12)
        self.pdf_canvas.setFillColorRGB(0, 0, 0)
        self.pdf_canvas.drawString(100, 100, topic)
        self.pdf_canvas.setFont("", 12)
        self.pdf_canvas.setFillColorRGB(0, 0, 0)
        self.pdf_canvas.drawString(100, 100, Title)
        self.pdf_canvas.setFont("", 12)
        self.pdf_canvas.setFillColorRGB(0, 0, 0)
        self.pdf_canvas.drawString(100, 100, uid)
        self.pdf_canvas.save()
        self.send_mail(User)

        # remove

    def send_mail(self, user):
        sender_email = "clashofbugs.com@gmail.com"
        app_password = "luse txfp qqxl sjnt"
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = user.email
        msg["Subject"] = "subject"
        msg.attach(MIMEText("body", "plain"))
        filepath = self.temp_file.name
        with open(filepath, "rb") as attachment:
            part = MIMEApplication(attachment.read(), "pdf")
            part.add_header("Content-Disposition", f"attachment; filename={filepath}")
        msg.attach(part)
        smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
        smtp_server.starttls()

        smtp_server.login(sender_email, app_password)
        smtp_server.sendmail(sender_email, user.email, msg.as_string())
        smtp_server.quit()
        os.remove(self.temp_file.name)
