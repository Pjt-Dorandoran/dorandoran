import chardet
filePath = "text/개구리 왕자.txt"

def split_text(filePath):
    # 파일 인코딩 자동 감지
    with open(filePath, 'rb') as file:
        result = chardet.detect(file.read())

    # 감지된 인코딩으로 파일 열기
    with open(filePath, 'r', encoding=result['encoding']) as file:
        lines = file.readlines()

    lineList = []
    for line in lines:
        # print(line.strip("\n"))
        lineList.append(line.strip("\n"))
    return lineList