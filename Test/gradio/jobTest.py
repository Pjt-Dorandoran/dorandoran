import time
from gradio_client import Client
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
                    5,	# int | float (numeric value between 1 and 50) in '모델 저장 주기(save_every_epoch):' Slider component
                    5,	# int | float (numeric value between 2 and 1000) in '전체 학습 에포크 수 (total_epoch):' Slider component
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
    print("Result : ", job.result())
    return job

user = "user5"

trainPath = "D:/RVC/Retrieval-based-Voice-Conversion-WebUI/data/t"
job = testGradio2(user, trainPath)
# print(job)
# print(type(job))
# print(job.outputs())
# while not job.done():
#     time.sleep(60)
# print("Outputs : ", job.outputs())