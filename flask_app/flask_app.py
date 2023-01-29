from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

from openai_request_script import send_request
from twilio_script import twii

app = Flask(__name__)

@app.route('/')
def index():
    # Create a twilio class
    twi = twii()

    question = "what is 1+2"
    # response = send_request(question)
    response = "OpenAI currently off"

    # send msg to phone
    # twi.send_msg(response)

    return response

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    resp = MessagingResponse()

    # Add a message
    resp.message("We plan to support voice to text in the future!")

    return str(resp)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our TwiML response
    # resp = MessagingResponse()
    twi = twii()

    # Determine the right reply for this message
    # if body == 'hello':
    #     resp.message("Hi!")
    # elif body == 'bye':
    #     resp.message("Goodbye")
    twi.send_msg("sup ass")

    return str(twi)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81, debug=True)