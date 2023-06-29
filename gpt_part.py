import openai
import speech_recognition
from gtts import gTTS
import time
from playsound import playsound
import os
import random

def speak_completion():
    with open("completion.txt", "r") as f:
        text = f.read()
        print(text)

    language = "ru"

    obj = gTTS(text=text, lang=language, slow=False)

    name = "sound.mp3"
    print(name)
    obj.save(name)

    time.sleep(3)
    print(name)
    time.sleep(3)
    playsound("sound.mp3")

    time.sleep(3)

    os.remove(name)


    os.remove(name)
    os.remove(name)
    os.remove(name)
    os.remove(name)
    os.remove(name)
    os.remove(name)


# chatgpt search function

def record():
    record_and_recognize_audio()
def gpt_request():
    openai.api_key = "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"
    with open("voice.txt", "r") as f:
        request = f.read()
    model_engine = "text-davinci-003"
    prompt = request
    print("Спасибо за запрос, ожидайте, я думаю.")
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    with open("completion.txt", "w+") as f:
        f.write(completion.choices[0].text)
        f.close()

    print("Ответ сохранен в файл")
    speak_completion()




# speak function
def record_and_recognize_audio(*args: tuple):
    recognizer = speech_recognition.Recognizer()
    microphone = speech_recognition.Microphone()
    with microphone:
        recognized_data = ""

        recognizer.adjust_for_ambient_noise(microphone, duration=2)

        try:
            print("Слушаю вас... Просьба произносить слова чётко")
            audio = recognizer.listen(microphone, 10, 10)

        except speech_recognition.WaitTimeoutError:
            print("Пожалуйста, проверьте работоспособность вашего микрофона")
            return

        try:
            print("Распознаю вашу речь...")
            recognized_data = recognizer.recognize_google(audio, language="ru").lower()

        except speech_recognition.UnknownValueError:
            pass
            print("Error1")

        except speech_recognition.RequestError:
            print("Пожалуйста, проверьте подключения к интернету")
            print("Error2")
    print(recognized_data)
    print("Вы сказали: ", recognized_data)
    with open("voice.txt", "w+") as f:
        f.write(recognized_data)
        f.close()
        print(recognized_data)
    gpt_request()



# speaking function


