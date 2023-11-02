from gradio_client import Client

def inferConvertBatch(index, filePath, base64_audio_data):
    client = Client("http://localhost:7865/")
    result = client.predict(                    
                    0,	# int | float (numeric value between 0 and 2333) in '화자/가수 ID를 선택해주세요.' Slider component
                    filePath,	# str  in '처리할 오디오 폴더의 경로를 입력하세요 (파일 매니저의 주소 표시줄에서 복사하세요):' Textbox component
                    "C:/Users/Hyug/Documents",	# str  in '출력 폴더 지정:' Textbox component
                    # {"name" : "test123.wav", "data" : f"data:@file/octet-stream;base64,{base64_audio_data}"},	# List[str] (List of filepath(s) or URL(s) to files) in '오디오 파일을 일괄적으로 입력할 수도 있습니다. 두 가지 옵션 중 하나를 선택하십시오. 폴더에서 읽기가 우선합니다.' File component
                    ["D:/RVC/Retrieval-based-Voice-Conversion-WebUI/opt/vocal4/t/test123.wav"],
                    0,	# int | float  in '음조 변경 (정수, 반음 수, 옥타브 상승: 12, 옥타브 내림: -12)' Number component
                    "rmvpe",	# str  in '选择音高提取算法,输入歌声可用pm提速,harvest低音好但巨慢无比,crepe效果好但吃GPU,rmvpe效果最好且微吃GPU' Radio component
                    "",	# str  in '특징 검색 라이브러리 파일 경로입니다. 공란으로 둘 경우 드롭다운에서 선택한 결과를 사용합니다.' Textbox component
                    index,	# str (Option from: ['logs\\joonhyug/added_IVF986_Flat_nprobe_1_joonhyug_v2.index', 'logs\\joonhyug2/added_IVF1429_Flat_nprobe_1_joonhyug2_v2.index', 'logs\\joonhyug_rmvpe/added_IVF1429_Flat_nprobe_1_joonhyug_rmvpe_v2.index', 'logs\\joonhyug_rmvpe_10min/added_IVF579_Flat_nprobe_1_joonhyug_rmvpe_10min_v2.index', 'logs\\joonhyug_rmvpe_story/added_IVF1427_Flat_nprobe_1_joonhyug_rmvpe_story_v2.index', 'logs\\joonhyug_rmvpe_story2/added_IVF1427_Flat_nprobe_1_joonhyug_rmvpe_story_v2.index', 'logs\\test1/added_IVF579_Flat_nprobe_1_test1_v2.index', 'logs\\tngud2/added_IVF1129_Flat_nprobe_1_tngud2_v2.index']) in '인덱스 경로를 자동으로 감지하고 드롭다운에서 선택하세요:' Dropdown component
                    0.75,	# int | float (numeric value between 0 and 1) in '검색 특성 비율:' Slider component
                    3,	# int | float (numeric value between 0 and 7) in '만약 3 이상이면, 수확된 음높이 결과에 중앙값 필터링을 적용합니다. 값은 필터 반경을 나타내며 숨소리를 줄일 수 있습니다.' Slider component
                    0,	# int | float (numeric value between 0 and 48000) in '후 처리에서 출력 오디오를 최종 샘플 속도로 재샘플링합니다. 재샘플링하지 않으려면 0으로 설정하세요.' Slider component
                    0.25,	# int | float (numeric value between 0 and 1) in '입력 음량 엔벨로프를 출력 음량 엔벨로프로 대체하거나 혼합하는 데 사용하세요. 비율이 1에 가까울수록 출력 엔벨로프가 더 많이 사용됩니다.' Slider component
                    0.33,	# int | float (numeric value between 0 and 0.5) in '전자 음악에서 찢겨지는 등의 아티팩트를 방지하기 위해 무성음자음과 숨소리를 보호하세요. 비활성화하려면 0.5로 설정하세요. 보호 강도를 높이기 위해 값을 낮추면 색인 정확도가 감소할 수 있습니다.' Slider component
                    "wav",	# str  in '내보내는 파일 형식' Radio component
                    api_name="/infer_convert_batch"
    )
    print(result)
    
def inferChangeVoice(pth):
    client = Client("http://localhost:7865/")
    result = client.predict(
                    pth,	# str (Option from: ['joonhyug.pth', 'joonhyug2.pth', 'joonhyug_rmvpe.pth', 'joonhyug_rmvpe_10min.pth', 'joonhyug_rmvpe_story.pth', 'joonhyug_rmvpe_story2.pth', 'test1.pth', 'tngud.pth', 'tngud2.pth']) in '음성 추론:' Dropdown component
                    0,	# int | float (numeric value between 0 and 0.5) in '전자 음악에서 찢겨지는 등의 아티팩트를 방지하기 위해 무성음자음과 숨소리를 보호하세요. 비활성화하려면 0.5로 설정하세요. 보호 강도를 높이기 위해 값을 낮추면 색인 정확도가 감소할 수 있습니다.' Slider component
                    0,	# int | float (numeric value between 0 and 0.5) in '전자 음악에서 찢겨지는 등의 아티팩트를 방지하기 위해 무성음자음과 숨소리를 보호하세요. 비활성화하려면 0.5로 설정하세요. 보호 강도를 높이기 위해 값을 낮추면 색인 정확도가 감소할 수 있습니다.' Slider component
                    api_name="/infer_change_voice"
    )
    print(result)
    
def trainStartAll(user, trainPath):
    client = Client("http://localhost:7865/")
    result = client.predict(
                    user,	# str  in '실험 이름을 입력하세요:' Textbox component
                    "40k",	# str  in '' Radio component
                    "true",	# str  in '모델이 음높이 지도를 제공하는지 여부 (노래에 필수, 말하기에는 선택 가능):' Radio component
                    trainPath,	# str  in '학습 폴더 경로를 입력하세요.' Textbox component
                    0,	# int | float (numeric value between 0 and 4) in '화자/가수의 ID를 지정해주세요.' Slider component
                    11,	# int | float (numeric value between 0 and 16) in '음높이 추출 및 데이터 처리에 사용되는 CPU 프로세스 수:' Slider component
                    "rmvpe_gpu",	# str  in '选择音高提取算法:输入歌声可用pm提速,高质量语音但CPU差可用dio提速,harvest质量更好但慢,rmvpe效果最好且微吃CPU/GPU' Radio component
                    10,	# int | float (numeric value between 1 and 50) in '모델 저장 주기(save_every_epoch):' Slider component
                    20,	# int | float (numeric value between 2 and 1000) in '전체 학습 에포크 수 (total_epoch):' Slider component
                    4,	# int | float (numeric value between 1 and 40) in '각 GPU의 배치 크기:' Slider component
                    "false",	# str  in '하드 디스크 공간을 절약하기 위해 최신 '.ckpt' 파일만 저장하시겠습니까?' Radio component
                    "assets/pretrained_v2/f0G40k.pth",	# str  in '미리 학습된 기본 모델 G 경로를 로드합니다.' Textbox component
                    "assets/pretrained_v2/f0D40k.pth",	# str  in '사전 학습된 기존 모델 D 경로를 불러오세요.' Textbox component
                    "0",	# str  in ''-'로 구분된 GPU 색인을 입력하세요. 예를 들면, 0-1-2를 입력하면 GPU 0, 1, 2를 사용합니다.'' Textbox component
                    "false",	# str  in 'GPU 메모리에 모든 학습 데이터 세트를 캐시할까요? 10분 미만의 작은 데이터 세트는 캐시하여 학습 속도를 높일 수 있지만, 대용량 데이터 세트를 캐시하면 GPU 메모리를 많이 소비하고 속도 향상이 크지 않을 수도 있습니다.' Radio component
                    "false",	# str  in '각 저장 지점마다 최종적인 작은 모델을 'weights' 폴더에 저장하시겠습니까?' Radio component
                    "v2",	# str  in '版本' Radio component
                    "0-0",	# str  in 'rmvpe卡号配置：以-分隔输入使用的不同进程卡号,例如0-0-1使用在卡0上跑2个进程并在卡1上跑1个进程' Textbox component
                    api_name="/train_start_all"
    )
    print(result)



def inferRefresh(user):
    
    data = {
        "pth" : "",
        "index" : ""
    }
    
    client = Client("http://localhost:7865/")
    result = client.predict(
                    api_name="/infer_refresh"
    )
    pths = result[0]['choices']
    for pth in pths:
        a = pth.split(".")[0]
        if user == a:
            # print("pht : ", pth)
            data['pth'] = pth
    indexs = result[1]['choices']
    for index in indexs:
        a = index.split("\\")[1]
        b = a.split("/")[0]
        # print(b)
        if user == b:
            # print("index : ", index)
            data['index'] = index
    return data

def testGradio():
    client = Client("http://localhost:7865/")
    job = client.submit(
                    api_name="/infer_refresh"
    )
    print(job.status())
    print(job.result())

import time
def testGradio2(user, trainPath):
    client = Client("http://localhost:7865/")
    job = client.submit(
                    user,	# str  in '실험 이름을 입력하세요:' Textbox component
                    "40k",	# str  in '' Radio component
                    "true",	# str  in '모델이 음높이 지도를 제공하는지 여부 (노래에 필수, 말하기에는 선택 가능):' Radio component
                    trainPath,	# str  in '학습 폴더 경로를 입력하세요.' Textbox component
                    0,	# int | float (numeric value between 0 and 4) in '화자/가수의 ID를 지정해주세요.' Slider component
                    11,	# int | float (numeric value between 0 and 16) in '음높이 추출 및 데이터 처리에 사용되는 CPU 프로세스 수:' Slider component
                    "rmvpe_gpu",	# str  in '选择音高提取算法:输入歌声可用pm提速,高质量语音但CPU差可用dio提速,harvest质量更好但慢,rmvpe效果最好且微吃CPU/GPU' Radio component
                    10,	# int | float (numeric value between 1 and 50) in '모델 저장 주기(save_every_epoch):' Slider component
                    20,	# int | float (numeric value between 2 and 1000) in '전체 학습 에포크 수 (total_epoch):' Slider component
                    4,	# int | float (numeric value between 1 and 40) in '각 GPU의 배치 크기:' Slider component
                    "false",	# str  in '하드 디스크 공간을 절약하기 위해 최신 '.ckpt' 파일만 저장하시겠습니까?' Radio component
                    "assets/pretrained_v2/f0G40k.pth",	# str  in '미리 학습된 기본 모델 G 경로를 로드합니다.' Textbox component
                    "assets/pretrained_v2/f0D40k.pth",	# str  in '사전 학습된 기존 모델 D 경로를 불러오세요.' Textbox component
                    "0",	# str  in ''-'로 구분된 GPU 색인을 입력하세요. 예를 들면, 0-1-2를 입력하면 GPU 0, 1, 2를 사용합니다.'' Textbox component
                    "false",	# str  in 'GPU 메모리에 모든 학습 데이터 세트를 캐시할까요? 10분 미만의 작은 데이터 세트는 캐시하여 학습 속도를 높일 수 있지만, 대용량 데이터 세트를 캐시하면 GPU 메모리를 많이 소비하고 속도 향상이 크지 않을 수도 있습니다.' Radio component
                    "false",	# str  in '각 저장 지점마다 최종적인 작은 모델을 'weights' 폴더에 저장하시겠습니까?' Radio component
                    "v2",	# str  in '版本' Radio component
                    "0-0",	# str  in 'rmvpe卡号配置：以-分隔输入使用的不同进程卡号,例如0-0-1使用在卡0上跑2个进程并在卡1上跑1个进程' Textbox component
                    api_name="/train_start_all"
    )
    print("Status : ", job.status())
    print("Result : ", job.result(timeout=5))
    while not job.done():
        time.sleep(60)
    print("Outputs : ", job.outputs())
    print("Result2 : ", job.result(timeout=5))
   
import os     
def is_file_exists(filePath):
    return os.path.exists(filePath)

# user = "joonhyug_rmvpe_story2"
user = "user2"
# data = inferRefresh(user)
# print(data)
# filePath = "D:\RVC\Retrieval-based-Voice-Conversion-WebUI\opt\vocal4\instrument_한성현m4a.m4a.reformatted.wav_10.wav"
filePath = "D:/RVC/Retrieval-based-Voice-Conversion-WebUI/opt/vocal4/t"
# print(is_file_exists(filePath))
# inferChangeVoice(data['pth'])

# print(is_file_exists(filePath))

# import base64

# with open(filePath+"/test123.wav", "rb") as file:
#     audio_data = base64.b64encode(file.read()).decode('utf-8')
# output_folder = os.path.join("C:/Users/Hyug/Documents", "converted_audio")
# os.mkdir(output_folder, exist_ok=True)
# inferConvertBatch(data['index'], filePath, audio_data)
# inferConvert(data['index'], filePath+"/test123.wav", audio_data)

trainPath = "D:/RVC/Retrieval-based-Voice-Conversion-WebUI/data/t"
# trainStartAll("user1", trainPath)

testGradio()
testGradio2(user, trainPath)