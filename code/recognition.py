import speech_recognition as sr
from config import *

def microphoneName() :
    #ตรวจสอบรายชื่อและหมายเลขไมโครโฟนในเครื่องคอมพิวเตอร์
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

def setMicrophoneName() :
    #เลือกไมโครโฟน ****สำคัญมาก****
    microphoneNum = 2
    return microphoneNum

def recognition() :
    global nameBot
    languageRecognition = "th-TH"

    recognizer = sr.Recognizer()

    with sr.Microphone(setMicrophoneName()) as source:
        print("พูดว่า 'หวัดดี" + nameBot + "'")

        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source)

        try:
            textRecognition = recognizer.recognize_google(audio, language = languageRecognition)
            removedWord1 = "ครับ"
            textRecognition = textRecognition.replace(removedWord1, "")
            removedWord2 = "ค่ะ"
            textRecognition = textRecognition.replace(removedWord2, "")
            removedWord3 = "คะ"
            textRecognition = textRecognition.replace(removedWord3, "")
            removedWord3 = " "
            textRecognition = textRecognition.replace(removedWord3, "")
            print("ข้อความที่อ่านได้คือ : ", textRecognition)
            return textRecognition
        
        except sr.UnknownValueError:
            print("ไม่สามารถรับรู้เสียง")
            return "ว่าง"

        except sr.RequestError as e:
            print(f"เกิดข้อผิดพลาดในการร้องขอ: {e}")
            return "ว่าง"

if __name__ == "__main__" :
    while True:
        recognition()