from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.preprocessing import image
import numpy as np
import asyncio
import websockets
from io import BytesIO
import urllib

with open('model_bike2.json', 'r') as json_file:
    loaded_model_json = json_file.read()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("model_bike2.h5")
loaded_model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

def downloadImage(URL):
    with urllib.request.urlopen(URL) as url:
        img = image.load_img(BytesIO(url.read()), target_size=(150, 150))
    return image.img_to_array(img)

async def hello():
    uri = "ws://localhost:8080"
    async with websockets.connect(uri) as websocket:
        while True:
            await websocket.send("get")
            while True:
                request = await websocket.recv()
                if request == "end":
                    break
                img_array = downloadImage(request)
                result = loaded_model.predict(np.array([img_array]))
                print(request, result)
                await websocket.send(str(np.argmax(result[0])))

asyncio.get_event_loop().run_until_complete(hello())


