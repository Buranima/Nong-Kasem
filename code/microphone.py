import speech_recognition as sr

class microphoneMain :
    def microphoneName() :
        #ตรวจสอบรายชื่อและหมายเลขไมโครโฟนในเครื่องคอมพิวเตอร์
        for index, name in enumerate(sr.Microphone.list_microphone_names()):
            print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
    #เลือกไมโครโฟน ****สำคัญมาก****
    microphoneNum = 2

if __name__ == "__main__" :
    microphoneMain.microphoneName()