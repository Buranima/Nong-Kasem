from recognition import *

class verifyMain :
    def alarm(textRecognition) :
        #ตรวจสอบการเรียก
        if "สวัสดีน้องเกษม" in textRecognition or "หวัดดีน้องเกษม" in textRecognition :
            #สร้างคำพูดแรกเมื่อถูกเรียก
            textSpeech = "สวัสดีค่ะ มีอะไรให้หนูช่วยไหมคะ"
            print("สวัสดีค่ะ มีอะไรให้หนูช่วยไหมคะ")
            return textSpeech
        else :
            return "ว่าง"

if __name__ == "__main__" :
    while True:
        verifyMain.alarm(recognitionMain.recognition())