from requests_toolbelt import MultipartEncoder
import requests

fileName = "img/image (2).png"
def addBook(url, field, accessToken):
    try:
        m = MultipartEncoder(fields=field)
        headers = {'Content-Type' : m.content_type, 'AccessToken' : accessToken}
        response = requests.post(url+"/book", headers=headers, data=m)
        response.raise_for_status()
        # print(response.json())
        if response.status_code == 200:
            print("책 등록 성공")
        return response.json()['data']
    except Exception as e:
        print(e)

def addPage(url, field, accessToken, bookId):
    try:
        m = MultipartEncoder(fields=field)
        headers = {'Content-Type' : m.content_type, 'AccessToken' : accessToken}
        response = requests.post(url+"/page/"+str(bookId), headers=headers, data=m)
        response.raise_for_status()
        # print(response.json())
        if response.status_code == 200:
            print("페이지 등록 성공")
    except Exception as e:
        print(e)

def addContent(url, field, accessToken, bookId):
    try:
        headers = {'AccessToken' : accessToken}
        response = requests.post(url+"/content/"+str(bookId), headers=headers, json=field)
        response.raise_for_status()
        # print(response.json())
        if response.status_code == 200:
            print("내용 등록 성공")
    except Exception as e:
        print(e)

url = "https://dorandoran.site/api"

def insertBook(accessToken, imgPath, field):
    bookField = {
        'title' : '',
        'multipartFile' : '',
        'author' : '',
        'publisher' : ''
        }
    bookField["title"] = field["title"]
    bookField["author"] = field["author"]
    bookField["publisher"] = field["publisher"]
    bookField["multipartFile"] = (imgPath, open(imgPath, 'rb'), 'image/png')
    bookId = addBook(url, bookField, accessToken)
    if bookId is None:
        raise ValueError("bookId의 값이 올바르지 않습니다.")
    return bookId

def insertPage(accessToken, imgPath, bookId, idx):
    pageField = {
    'multipartFile' : '',
    'idx' : ''
    }
    pageField["multipartFile"] = (imgPath, open(imgPath, 'rb'), 'image/png')
    pageField["idx"] = str(idx)
    addPage(url, pageField, accessToken, bookId)

def insertContent(accessToken, bookId, idx, script):
    contentField = {
    'idx' : '',
    'script' : ''
    }
    contentField["idx"] = str(idx)
    contentField["script"] = script
    addContent(url, contentField, accessToken, bookId)
