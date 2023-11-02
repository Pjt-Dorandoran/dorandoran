import uvicorn
from fastapi import FastAPI
app = FastAPI()

from Publicher import message
from Consumer import on_message

exchange = "test.exchange"

@app.get("/")
def 이름():
    return "보낼 값"

@app.get("/test")
def 야옹():
    return {'고양이' : '야옹'}

@app.post("/send")
def send_message():
    queue_name = "test.req"
    message(queue_name, "테스트")
    return {"message" : "Message sent"}

@app.get("/receive")
async def receive_message():
    queue_name = "test.req"
    try:
        temp = await on_message(queue_name)
    except Exception as e:
        print(e)
    print("temp : ", temp)
    print(type(temp))
    return {"message" : "Message Received", "temp" : temp.get()}

@app.get("/receive2")
async def receive2_message():
    queue_name = "test.res"
    try:
        temp = await on_message(queue_name)
    except Exception as e:
        print(e)
    print("temp : ", temp)
    print(type(temp))
    return {"message" : "Message Received", "temp" : temp.get()}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)