from gtts import gTTS
from mutagen.mp3 import MP3
import os
import time
from recognition import *
from verify import *

class soundMain :
    def saveSound(textSpeech) :
        #เลือกภาษาที่ต้องการพูด ****สำคัญมาก****
        langSpeech = "th"

        #แปลงเป็นคำพูด
        if textSpeech == "ว่าง" :
            pass
        else :
            #แปลงข้อความเป็นคำพูด
            tts = gTTS(textSpeech, lang = langSpeech)
            #บันทึกไฟล์เสียง
            tts.save("voice.wav")
            #เรียกใช้การเล่นเสียง
            soundMain.openSound()

    def openSound() :
        #เล่นเสียง
        os.system("voice.wav")
        #ระบุไฟล์ MP3
        audioMp3 = MP3("voice.wav")
        #วัดความยาวเสียง
        audioDuration = audioMp3.info.length
        #หยุดการทำงานตามเวลาเล่นเสียง
        time.sleep(audioDuration+1)

if __name__ == "__main__" :
    while True:
        soundMain.saveSound(verifyMain.alarm(recognitionMain.recognition()))