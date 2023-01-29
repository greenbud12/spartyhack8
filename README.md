# spartyhack8
gcloud auth login

gcloud builds submit --tag gcr.io/spartyhack8/spartyhack
gcloud run deploy --image gcr.io/spartyhack8/spartyhack --platform managed