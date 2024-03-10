from recognition import *
from maria import *
from gtts import gTTS
from mutagen.mp3 import MP3
import os
import time
from config import *

def saveSound(textSpeech) :
    langSpeech = "th"

    if textSpeech == "ว่าง" :
        pass
    else :
        tts = gTTS(textSpeech, lang = langSpeech)
        tts.save("voice.wav")
        openSound("voice.wav")

def openSound(nameVoice) :
    os.system(nameVoice)
    audioMp3 = MP3(nameVoice)
    audioDuration = audioMp3.info.length
    time.sleep(audioDuration)

def alarm() :
    textRecognition = recognition()
    if "สวัสดี" + nameBot in textRecognition or "หวัดดี" + nameBot in textRecognition :
        textSpeech = "สวัสดีค่ะ มีอะไรให้หนูช่วยไหมคะ"
        print("สวัสดีค่ะ มีอะไรให้หนูช่วยไหมคะ")
        saveSound(str(textSpeech))
        verifTextSpeech()
    else :
        saveSound("ว่าง")
    
def verifTextSpeech() :
    textRecognition = recognition()
    if "ไม่มี" in textRecognition :
        textSpeech = "หากมีอะไรที่หนูช่วยได้สามารถบอกหนูได้เลยนะคะ"
        saveSound(str(textSpeech))
    else :
        connectToDB()
        result = browseSQL("SELECT answer FROM answer_table, question_table WHERE question LIKE '%"+str(textRecognition)+"%' AND answer_fk = id_answer")
        if len(result) == 1 :
            textSpeech = str(result)
            saveSound(str(textSpeech) + "ค่ะ")
        else :
            if "ว่าง" in textRecognition :
                pass
            else :
                increaseSQL("INSERT INTO log_table (question_log) VALUES ('" + str(textRecognition) +"')")
                textSpeech = "หนูไม่เข้าใจคำถามค่ะ"
                saveSound(str(textSpeech))

if __name__ == "__main__" :
    while True:
        alarm()