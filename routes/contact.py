from flask import Blueprint, request, jsonify
import os
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

contact_bp = Blueprint("contact", __name__)


@contact_bp.route("/send-message", methods=["POST"])
def send_message():

    try:

        form_type = request.form.get("form_type")

        name = request.form.get("name")

        email = request.form.get("email")

        category = request.form.get("category")

        message = request.form.get("message")

        send_email(
            form_type,
            name,
            email,
            category,
            message
        )

        return jsonify({
            "success": True,
            "message": "Thank you! Your message has been sent successfully."
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


def send_email(form_type, name, email, category, message):

    sender = os.getenv("EMAIL_USER")

    password = os.getenv("EMAIL_PASS")

    receiver = sender

    # -----------------------------------

    if form_type == "feedback":

        subject = f"📝 New Feedback | {category}"

        heading = "New Feedback Received"

        color = "#ff9800"

    else:

        subject = f"📩 New Contact Message | {category}"

        heading = "New Contact Message"

        color = "#1565C0"

    # -----------------------------------

    html = f"""
<!DOCTYPE html>

<html>

<body style="margin:0;background:#f4f6f9;font-family:Arial,sans-serif;">

<table width="100%" cellpadding="0" cellspacing="0">

<tr>

<td align="center">

<table width="650"
style="background:white;
margin:30px auto;
border-radius:10px;
overflow:hidden;
box-shadow:0 0 15px rgba(0,0,0,.15);">

<tr>

<td style="background:{color};
padding:25px;
text-align:center;
color:white;">

<h1 style="margin:0;">
RefineX AI
</h1>

<p style="margin-top:8px;">
Smart Refinery Intelligence Platform
</p>

</td>

</tr>

<tr>

<td style="padding:30px;">

<h2 style="color:{color};">

{heading}

</h2>

<table
width="100%"
cellpadding="10"
style="border-collapse:collapse;">

<tr>

<td
style="font-weight:bold;
background:#f2f2f2;
width:180px;">

Form Type

</td>

<td>

{form_type.title()}

</td>

</tr>

<tr>

<td
style="font-weight:bold;
background:#f2f2f2;">

Name

</td>

<td>

{name}

</td>

</tr>

<tr>

<td
style="font-weight:bold;
background:#f2f2f2;">

Email

</td>

<td>

{email}

</td>

</tr>

<tr>

<td
style="font-weight:bold;
background:#f2f2f2;">

Category

</td>

<td>

{category}

</td>

</tr>

<tr>

<td
style="font-weight:bold;
background:#f2f2f2;">

Message

</td>

<td>

{message}

</td>

</tr>

</table>

<br>

<hr>

<p
style="color:#777;
font-size:13px;">

This email was automatically generated from the
<b>RefineX Smart Refinery Platform</b>.

</p>

</td>

</tr>

<tr>

<td
style="background:#1d2433;
color:#ddd;
padding:18px;
text-align:center;
font-size:12px;">

© 2026 RefineX AI

<br>

Indian Oil Corporation Ltd.

<br>

Guwahati Refinery

</td>

</tr>

</table>

</td>

</tr>

</table>

</body>

</html>
"""

    msg = MIMEMultipart("alternative")

    msg["Subject"] = subject

    msg["From"] = sender

    msg["To"] = receiver

    msg.attach(MIMEText(html, "html"))

    server = smtplib.SMTP("smtp.gmail.com", 587)

    server.starttls()

    server.login(sender, password)

    server.sendmail(
        sender,
        receiver,
        msg.as_string()
    )

    server.quit()