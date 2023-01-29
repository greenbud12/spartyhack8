from flask import current_app as app
from flask import Flask, request, redirect

from twilio.twiml.messaging_response import MessagingResponse
from . openai_request_script import send_request
from . twilio_script import twii


@app.route('/')
def index():
    return f"""<html>
	           <h1 style="text-align: center; color: Black;">
               Welcome to TextGPT</h1>
	           <p style="text-align: center; color: Black;">
               Simply text (269)399-4156</p>
	           </html>
	        """

@app.route("/sms/call", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    resp = MessagingResponse()

    # Add a message
    resp.message("The Robots are coming! Head for the hills!")

    return str(resp)

@app.route("/sms/msg", methods=['GET', 'POST'])
def incoming_sms():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    resp = MessagingResponse()

    # MSG to send back
    msg = "A test"

    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)
    b2 = body.lower().strip()

    # # Determine the right reply for this message
    if b2 == 'hello':
        resp.message("Hi!")
    elif b2 == 'bye':
        resp.message("Goodbye")
    elif b2 == 'help' or b2 == 'h':
        resp.message("I am a chatbot that can answer any of your questions.\
 You could ask about the weather, color of an apple, or how to plant\
 a tomato seedling. Your creativity is the limit.")
    else:
        # Add a message
        msg = resp.message(send_request(body))

        # Add a picture message
        msg.media(
            "https://farm8.staticflickr.com/7090/6941316406_80b4d6d50e_z_d.jpg"
        )

    return str(resp)