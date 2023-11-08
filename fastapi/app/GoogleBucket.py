import uuid
import os
os.environ ["GOOGLE_APPLICATION_CREDENTIALS"] = "rd-ssafy-project-ebd0eea46d3e.json"

from google.cloud import storage

client = storage.Client()

bucket_name = 'ssafy-last-project'

def Download(userId, voiceUrl):
    fileName = voiceUrl.split("/")[-1]
    print(fileName)
    
    directory = os.path.join("/", "app", "data", str(userId))
    os.makedirs(directory, exist_ok=True)
    save_location = os.path.join(directory, fileName+".wav")

    if os.path.exists(save_location):
        print("aleady download")
        return

    bucket = client.bucket(bucket_name)
    blob = bucket.blob(fileName)
    blob.download_to_filename(save_location)

def Upload(userId, fileName):

    directory = os.path.join("/", "app", "opt", str(userId), fileName)

    destination_file_name = str(uuid.uuid3(uuid.NAMESPACE_URL, directory))

    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_file_name)
    generation_match_precondition = 0
    blob.upload_from_filename(directory, if_generation_match=generation_match_precondition)
    print(destination_file_name)

Download(1, "https://storage.googleapis.com/ssafy-last-project/eb7c380d-58b5-4425-a012-1617d5b16d25")