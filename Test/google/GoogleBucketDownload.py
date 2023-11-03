import os
os.environ ["GOOGLE_APPLICATION_CREDENTIALS"] = "rd-ssafy-project-ebd0eea46d3e.json"
print('Credendtials from environ: {}'.format(os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')))

from google.cloud import storage

client = storage.Client()

bucket = client.bucket('ssafy-last-project')

# blob = bucket.blob('00cbff5b-b5a5-4ac8-bdb6-ddcb6f63b7fe')

# blob.download_to_filename('00cbff5b-b5a5-4ac8-bdb6-ddcb6f63b7fe.png')

blob = bucket.blob('8404c976-872d-345b-a495-7eab36fc9906')

blob.download_to_filename('8404c976-872d-345b-a495-7eab36fc9906.wav')