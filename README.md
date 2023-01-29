TextGPT
Description
Provides sms the ability to communicate with the OpenAI engine text-davinci-002

Installation
# important ish
gcloud auth login
gcloud init

# use this to reupload
docker-compose -f docker-compose.yml -p spartyhack-container8 up
gcloud builds submit --tag gcr.io/spartyhack8/spartyhack
gcloud run deploy --image gcr.io/spartyhack8/spartyhack --platform managed

Usage
Text the number (269)399-4156.

Contribution
Information on how others can contribute to the project, including guidelines and code of conduct.

License
Information on the license under which the project is released, such as an open source license.

Acknowledgements
I would like to acknowledge Prof. MM Ghassemi for his teaching. Without learning what I have in his class I do not beleive I would have been able to finish.

Support
bakerso1@msu.edu