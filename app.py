from flask import Flask, request, jsonify
import smtplib
from email.message import EmailMessage

from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/send-email', methods=['POST'])
def send_email():
    try:
        # Parse request data
        data = request.get_json()
        user_email = data['user_email']
        message = data['message']

        # Set up SMTP connection
        smtp_server = 'smtp.gmail.com'
        port = 587
        sender_email = 'apptest2000118@gmail.com'
        password = 'idrs pzcp hghl jcyp'

        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(sender_email, password)

        # Create EmailMessage object
        email = EmailMessage()
        email.set_content(user_email+"   "+ message)
        email['Subject'] = 'Message from User'
        email['From'] = sender_email
        email['To'] = 'kumarapeliofficial@gmail.com'
        cc_emails=['damayantha20118@gmail.com','cyberkey.opensource@hotmail.com','cyberkey.feedback@outlook.com']
        if isinstance(cc_emails, list):
            cc_emails = ', '.join(cc_emails)  # Convert list to comma-separated string
        email['Cc'] = cc_emails

        # Send email
        server.send_message(email)

        # Close SMTP connection
        server.quit()

        return jsonify({'success': True, 'message': 'Email sent successfully'})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
