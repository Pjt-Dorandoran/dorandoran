from splitText import split_text
from login import login
import book
import os

#텍스트 파일 경로
fileInput = input("파일을 text폴더에 넣고, 파일명을 입력해주세요(.txt 포함) : ")
filePath = "text/"+fileInput
texts = split_text(filePath)

# title : 제목
# author : 작가
# publisher : 출판사
parts = filePath.split("/")[-1].split(".")[0].split("_")
field = {
    'title' : parts[0],
    'author' : parts[1],
    'publisher' : parts[2]
}

# Book의 표지 이미지 경로
coverPath = "img/"+parts[0]+"/"+parts[0]+"_cover.png"

idx = 1
for text in texts:
    print(str(idx)+" : "+text)
    idx += 1
print("총 문장 : "+str(len(texts)))
print("책 등록을 진행하려면 엔터키를 누르세요. \n 종료를 원하면 e키를 누르세요.")
key = input()
if key == 'e':
    print("프로그램을 종료합니다.")
    raise
else:
    #관리자 로그인
    accessToken = login()

    try:
        # Page, Content의 index 번호
        idx = 1
        # 책 등록
        bookId = book.insertBook(accessToken, coverPath, field)
        for text in texts:
            # 나중에 페이지 하나에 들어 갈 사진경로
            imgPath = "img/"+parts[0]+"/"+parts[0]+"_"+str(idx)+".png"
            # imgPath = "img/image (2).png"
            # Page 등록
            book.insertPage(accessToken, imgPath, bookId, idx)
            if '#' in text:
                temp = text.split("#")
                for t in temp:
                    # Content 등록
                    book.insertContent(accessToken, bookId, idx, t)
                    print(t)
            else:
                # Content 등록
                book.insertContent(accessToken, bookId, idx, text)
                print(text)
            idx += 1
        os.system("pause")
    except Exception as e:
        print(e)