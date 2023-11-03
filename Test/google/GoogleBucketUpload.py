import uuid
from google.cloud import storage

import os
os.environ ["GOOGLE_APPLICATION_CREDENTIALS"] = "rd-ssafy-project-ebd0eea46d3e.json"
print('Credendtials from environ: {}'.format(os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')))


def upload_blob(bucket_name, source_file_name, destination_blob_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    generation_match_precondition = 0

    blob.upload_from_filename(source_file_name, if_generation_match=generation_match_precondition)

    print(
        f"File {source_file_name} uploaded to {destination_blob_name}."
    )

file = "./test123.wav.wav"
uuidResult = uuid.uuid3(uuid.NAMESPACE_URL, file)
print(uuidResult)
upload_blob('ssafy-last-project', file, str(uuidResult))