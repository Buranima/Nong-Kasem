import speech_recognition as sr
from microphone import *

class recognitionMain :
    def recognition() :

        #เลือกภาษาที่ต้องการแปลง ****สำคัญมาก****
        languageRecognition = "th-TH"

        #สร้างตัวแปรการรู้จำเสียง
        recognizer = sr.Recognizer()
        #เปิดใช้งานไมโครโฟน
        with sr.Microphone(microphoneMain.microphoneNum) as source:
            print("พูดว่า 'หวัดดีน้องเกษม'")
            #เปิดการตัดเสียงรบกวน
            recognizer.adjust_for_ambient_noise(source)
            #บันทึกเสียงพูด
            audio = recognizer.listen(source)
            #เริ่มแปลงเสียง
            try:
                #แปลงเสียง
                textRecognition = recognizer.recognize_google(audio, language = languageRecognition)
                print("ข้อความที่อ่านได้คือ : ", textRecognition)
                return textRecognition
            #ไม่สามารถรับเสียงได้หรืออาจจะไม่ได้ยินเสียง
            except sr.UnknownValueError:
                print("ไม่สามารถรับรู้เสียง")
                return "ว่าง"
            #เกิดข้อผิดพลาดหรือไม่สามารถเชื่อมต่อบริการได้
            except sr.RequestError as e:
                print(f"เกิดข้อผิดพลาดในการร้องขอ: {e}")
                return "ว่าง"

if __name__ == "__main__" :
    while True:
        recognitionMain.recognition()