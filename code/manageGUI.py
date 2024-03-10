from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image,ImageTk
from maria import *
from restore import *

def maimManageGUI() :
    global font1, font2, font3

    def saveQuestionT1(event = None) :
        questionDataT1 = e1T1.get()
        answerDataT1 = e2T1.get()
        e1T1.focus()
        connectToDB()
        if len(questionDataT1) > 0 and len(answerDataT1) > 0 :
            resultT1 = browseSQL("SELECT question FROM question_table WHERE question = '" + str(questionDataT1) + "'")
            if len(resultT1) > 0 :
                e2T1.delete(0, "end")
                messagebox.showwarning("แจ้งเตือน", "คำถามนี้มีในฐานข้อมูลแล้ว")
            else :
                resultT1 = browseSQL("SELECT id_answer FROM answer_table WHERE answer = '" + str(answerDataT1) + "'")
                if len(resultT1) > 0:
                    dataT1 = str(resultT1)
                    dataT1 = dataT1.replace("'", "")
                    dataT1 = dataT1.replace(",", "")
                    dataT1 = dataT1.replace("(", "")
                    dataT1 = dataT1.replace(")", "")
                    dataT1 = dataT1.replace("[", "")
                    dataT1 = dataT1.replace("]", "")
                    increaseSQL("INSERT INTO question_table (question, answer_fk) VALUES ('" + str(questionDataT1) + "', " + str(dataT1) + ")")
                else :
                    increaseSQL("INSERT INTO answer_table (answer) VALUES ('" + str(answerDataT1) + "')")
                    resultT1 = browseSQL("SELECT id_answer FROM answer_table WHERE answer = '" + str(answerDataT1) + "'")
                    dataT1 = str(resultT1)
                    dataT1 = dataT1.replace("'", "")
                    dataT1 = dataT1.replace(",", "")
                    dataT1 = dataT1.replace("(", "")
                    dataT1 = dataT1.replace(")", "")
                    dataT1 = dataT1.replace("[", "")
                    dataT1 = dataT1.replace("]", "")
                    increaseSQL("INSERT INTO question_table (question, answer_fk) VALUES ('" + str(questionDataT1) + "', " + str(dataT1) + ")")
                print("คำถาม -> {}".format(questionDataT1))
                print("คำตอบ -> {}".format(answerDataT1))
                e1T1.delete(0, "end")
                e2T1.delete(0, "end")
                messagebox.showinfo("แจ้งเตือน", "การบันทึกสำเร็จ")
        else :
            messagebox.showerror("เกิดข้อผิดพลาด", "กรุณากรอกข้อมูลให้ครบถ้วน")
    
    def setEntryT1(event = None) :
        e2T1.focus()

    def deletlLogT2(event = None) :
        connectToDB()
        dropSQL("DROP TABLE log_table")
        createSQL("CREATE TABLE log_table(id_log INT(50) NOT NULL AUTO_INCREMENT, question_log VARCHAR(100) NOT NULL , PRIMARY KEY(id_log))")
        reloadLogT2()

    def reloadLogT2(event = None) :
        global resultLogT2
        connectToDB()
        resultLogT2 = browseSQL("SELECT question_log FROM log_table")
        tableLogT2.delete(*tableLogT2.get_children())
        if len(resultLogT2) > 0 :
            for l in resultLogT2 :
                tableLogT2.insert("", "end", value=l)
    
    def increaseQT2N(event = None) :
        global font1, font2, font3
        
        def increaseQLog(event = None) :
            questionDataT2N = e1T2N.get()
            answerDataT2N = e2T2N.get()
            print(len(questionDataT2N), len(answerDataT2N))
            connectToDB()
            if len(questionDataT2N) > 0 and len(answerDataT2N) > 0 :
                resultT2N = browseSQL("SELECT question FROM question_table WHERE question = '" + str(questionDataT2N) + "'")
                if len(resultT2N) > 0 :
                    e2T2N.delete(0, "end")
                    messagebox.showwarning("แจ้งเตือน", "คำถามนี้มีในฐานข้อมูลแล้ว")
                else :
                    resultT2N = browseSQL("SELECT id_answer FROM answer_table WHERE answer = '" + str(answerDataT2N) + "'")
                    if len(resultT2N) > 0:
                        dataT2N = str(resultT2N)
                        dataT2N = dataT2N.replace("'", "")
                        dataT2N = dataT2N.replace(",", "")
                        dataT2N = dataT2N.replace("(", "")
                        dataT2N = dataT2N.replace(")", "")
                        dataT2N = dataT2N.replace("[", "")
                        dataT2N = dataT2N.replace("]", "")
                        increaseSQL("INSERT INTO question_table (question, answer_fk) VALUES ('" + str(questionDataT2N) + "', " + str(dataT2N) + ")")
                    else :
                        increaseSQL("INSERT INTO answer_table (answer) VALUES ('" + str(answerDataT2N) + "')")
                        resultT2N = browseSQL("SELECT id_answer FROM answer_table WHERE answer = '" + str(answerDataT2N) + "'")
                        dataT2N = str(resultT2N)
                        dataT2N = dataT2N.replace("'", "")
                        dataT2N = dataT2N.replace(",", "")
                        dataT2N = dataT2N.replace("(", "")
                        dataT2N = dataT2N.replace(")", "")
                        dataT2N = dataT2N.replace("[", "")
                        dataT2N = dataT2N.replace("]", "")
                        increaseSQL("INSERT INTO question_table (question, answer_fk) VALUES ('" + str(questionDataT2N) + "', " + str(dataT2N) + ")")
                    print("คำถาม -> {}".format(questionDataT2N))
                    print("คำตอบ -> {}".format(answerDataT2N))
                    resultT2N = browseSQL("SELECT id_log FROM log_table WHERE question_log = " + questionDataT2N)
                    dataT2N = str(resultT2N)
                    dataT2N = dataT2N.replace("'", "")
                    dataT2N = dataT2N.replace(",", "")
                    dataT2N = dataT2N.replace("(", "")
                    dataT2N = dataT2N.replace(")", "")
                    dataT2N = dataT2N.replace("[", "")
                    dataT2N = dataT2N.replace("]", "")
                    deleteSQL("DELETE FROM log_table WHERE  id_log = " + dataT2N)
                    reloadLogT2()
                    messagebox.showinfo("แจ้งเตือน", "การบันทึกสำเร็จ")
                newWindownT2N.destroy()
            else :
                messagebox.showerror("เกิดข้อผิดพลาด", "กรุณากรอกข้อมูลให้ครบถ้วน")
                newWindownT2N.destroy()

        def setEntryT2N(event = None) :
            e2T2N.focus()

        newWindownT2N = Tk()
        windowWidthT2N = 640
        windowHeightT2N = 384
        screenWidthT2N = ManageGUI.winfo_screenwidth()
        screenHeightT2N = ManageGUI.winfo_screenheight()
        xPositionT2N = (screenWidthT2N - windowWidthT2N) // 2
        yPositionT2N = (screenHeightT2N - windowHeightT2N) // 2
        newWindownT2N.geometry(f"{windowWidthT2N}x{windowHeightT2N}+{xPositionT2N}+{yPositionT2N}")
        newWindownT2N.title("เพิ่มคำถามไปยังฐานข้อมูล")

        itemT2N = tableLogT2.selection()[0]
        valuesT2N = tableLogT2.item(itemT2N, "values")
        dataT2N = str(valuesT2N)
        dataT2N = dataT2N.replace("'", "")
        dataT2N = dataT2N.replace(",", "")
        dataT2N = dataT2N.replace("(", "")
        dataT2N = dataT2N.replace(")", "")
        dataT2N = dataT2N.replace("[", "")
        dataT2N = dataT2N.replace("]", "")

        l1T2N = ttk.Label(newWindownT2N, text="คำถาม", font=font2)
        l1T2N.pack()

        e1T2N = ttk.Entry(newWindownT2N, font=font3, width=50)
        e1T2N.bind("<Return>", setEntryT2N)
        e1T2N.pack()
        e1T2N.insert(0, dataT2N)

        l2T2N = ttk.Label(newWindownT2N, text="คำตอบ", font=font2)
        l2T2N.pack()

        e2T2N = ttk.Entry(newWindownT2N, font=font3, width=50)
        e2T2N.bind("<Return>", increaseQLog)
        e2T2N.pack()

        b1T2N = ttk.Button(newWindownT2N, text="บันทึก", command=increaseQLog)
        b1T2N.pack(ipadx=40, ipady=20 ,pady=30)

        newWindownT2N.mainloop()

    def restoreDataBaseT4() :
        resultT4 = messagebox.askyesno("แจ้งเตือน", "การคืนค่าฐานข้อมูลจะลบข้อมูลทั้งหมดออกจากฐานข้อมูล คุณแน่ใจแล้วใช่หรือไม่")
        if resultT4 :
            restoreDB()
            messagebox.showinfo("แจ้งเตือน", "คืนค่าสำเร็จ")
        else :
            pass

    def restoreConfigT4() :
        resultT4 = messagebox.askyesno("แจ้งเตือน", "การคืนค่าการตั้งค่าจะทำให้การตั้งค่ากลับคืนสู่ค่าเริ่มต้น คุณแน่ใจแล้วใช่หรือไม่")
        if resultT4 :
            restoreJson()
            messagebox.showinfo("แจ้งเตือน", "คืนค่าสำเร็จ")
        else :
            pass
    
    def restoreAllT4() :
        resultT4 = messagebox.askyesno("แจ้งเตือน", "การคืนค่าการตั้งค่าจะทำให้การตั้งค่าทั้งหมดกลับคืนสู่ค่าเริ่มต้น คุณแน่ใจแล้วใช่หรือไม่")
        if resultT4 :
            restoreJson()
            restoreDB()
            messagebox.showinfo("แจ้งเตือน", "คืนค่าสำเร็จ")
        else :
            pass

    def editeAllQT3N(event = None) :
        global font1, font2, font3
        
        def editeQT3N(event = None) :
            questionDataT3N = e1T3N.get()
            answerDataT3N = e2T3N.get()
            print(len(questionDataT3N), len(answerDataT3N))
            connectToDB()
            if len(questionDataT3N) > 0 and len(answerDataT3N) > 0 :
                resultT3N = browseSQL("SELECT question FROM question_table WHERE question = '" + str(questionDataT3N) + "'")
                if len(resultT3N) > 0 :
                    e2T3N.delete(0, "end")
                    messagebox.showwarning("แจ้งเตือน", "คำถามนี้มีในฐานข้อมูลแล้ว")
                else :
                    resultT3N = browseSQL("SELECT id_answer FROM answer_table WHERE answer = '" + str(answerDataT3N) + "'")
                    if len(resultT3N) > 0:
                        dataT3N = str(resultT3N)
                        dataT3N = dataT3N.replace("'", "")
                        dataT3N = dataT3N.replace(",", "")
                        dataT3N = dataT3N.replace("(", "")
                        dataT3N = dataT3N.replace(")", "")
                        dataT3N = dataT3N.replace("[", "")
                        dataT3N = dataT3N.replace("]", "")
                        increaseSQL("INSERT INTO question_table (question, answer_fk) VALUES ('" + str(questionDataT3N) + "', " + str(dataT3N) + ")")
                    else :
                        increaseSQL("INSERT INTO answer_table (answer) VALUES ('" + str(answerDataT3N) + "')")
                        resultT3N = browseSQL("SELECT id_answer FROM answer_table WHERE answer = '" + str(answerDataT3N) + "'")
                        dataT3N = str(resultT3N)
                        dataT3N = dataT3N.replace("'", "")
                        dataT3N = dataT3N.replace(",", "")
                        dataT3N = dataT3N.replace("(", "")
                        dataT3N = dataT3N.replace(")", "")
                        dataT3N = dataT3N.replace("[", "")
                        dataT3N = dataT3N.replace("]", "")
                        increaseSQL("INSERT INTO question_table (question, answer_fk) VALUES ('" + str(questionDataT3N) + "', " + str(dataT3N) + ")")
                    print("คำถาม -> {}".format(questionDataT3N))
                    print("คำตอบ -> {}".format(answerDataT3N))
                    resultT3N = browseSQL("SELECT id_log FROM log_table WHERE question_log = " + questionDataT3N)
                    dataT3N = str(resultT3N)
                    dataT3N = dataT3N.replace("'", "")
                    dataT3N = dataT3N.replace(",", "")
                    dataT3N = dataT3N.replace("(", "")
                    dataT3N = dataT3N.replace(")", "")
                    dataT3N = dataT3N.replace("[", "")
                    dataT3N = dataT3N.replace("]", "")
                    deleteSQL("DELETE FROM log_table WHERE  id_log = " + dataT3N)
                    reloadAllT3()
                    messagebox.showinfo("แจ้งเตือน", "การบันทึกสำเร็จ")
                newWindownT3N.destroy()
            else :
                messagebox.showerror("เกิดข้อผิดพลาด", "กรุณากรอกข้อมูลให้ครบถ้วน")
                newWindownT3N.destroy()

        def setEntryT3N(event = None) :
            e2T3N.focus()

        newWindownT3N = Tk()
        windowWidthT3N = 640
        windowHeightT3N = 384
        screenWidthT3N = ManageGUI.winfo_screenwidth()
        screenHeightT3N = ManageGUI.winfo_screenheight()
        xPositionT3N = (screenWidthT3N - windowWidthT3N) // 2
        yPositionT3N = (screenHeightT3N - windowHeightT3N) // 2
        newWindownT3N.geometry(f"{windowWidthT3N}x{windowHeightT3N}+{xPositionT3N}+{yPositionT3N}")
        newWindownT3N.title("แก้ไขคำถามและคำตอบในฐานข้อมูล")

        itemT3N = tableLogT3.selection()[0]
        valuesT3N = tableLogT3.item(itemT3N, "values")

        l1T3N = ttk.Label(newWindownT3N, text="คำถาม", font=font2)
        l1T3N.pack()

        e1T3N = ttk.Entry(newWindownT3N, font=font3, width=50)
        e1T3N.bind("<Return>", setEntryT3N)
        e1T3N.pack()
        e1T3N.insert(0, valuesT3N[0])

        l2T3N = ttk.Label(newWindownT3N, text="คำตอบ", font=font2)
        l2T3N.pack()

        e2T3N = ttk.Entry(newWindownT3N, font=font3, width=50)
        e2T3N.bind("<Return>", editeQT3N)
        e2T3N.pack()
        e2T3N.insert(0, valuesT3N[1])

        b1T3N = ttk.Button(newWindownT3N, text="บันทึก", command=editeQT3N)
        b1T3N.pack(ipadx=30, ipady=10 ,pady=10)

        b2T3N = ttk.Button(newWindownT3N, text="ลบ", command=editeQT3N)
        b2T3N.pack(ipadx=30, ipady=10 ,pady=10)

        newWindownT3N.mainloop()

    def reloadAllT3(event = None) :
        global resultLogT3
        connectToDB()
        resultLogT3 = browseSQL("SELECT question_log FROM log_table")
        tableLogT3.delete(*tableLogT3.get_children())
        if len(resultLogT3) > 0 :
            for l in resultLogT3 :
                tableLogT3.insert("", "end", value=l)

#######################################################################################################
    ManageGUI = Tk()
    windowWidth = 800
    windowHeight = 480
    screenWidth = ManageGUI.winfo_screenwidth()
    screenHeight = ManageGUI.winfo_screenheight()
    xPosition = (screenWidth - windowWidth) // 2
    yPosition = (screenHeight - windowHeight) // 2
    ManageGUI.geometry(f"{windowWidth}x{windowHeight}+{xPosition}+{yPosition}")
    ManageGUI.title("NONG KASEM Q&A Settings")
    tab = ttk.Notebook(ManageGUI)
    t1 = Frame(tab)
    t2 = Frame(tab)
    t3 = Frame(tab)
    t4 = Frame(tab)
    tab.pack(fill=BOTH, expand=1)
    tab.add(t1, text="เพิ่มคำถามใหม่")
    tab.add(t2, text="ประวัติ")
    tab.add(t3, text="ฐานข้อมูลคำถาม")
    tab.add(t4, text="คืนค่าการตั้งค่า")
#######################################################################################################

#######################################################################################################
    l1T1 = ttk.Label(t1, text="คำถาม", font=font1)
    l1T1.pack()

    e1T1 = ttk.Entry(t1, font=font2, width=60)
    e1T1.bind("<Return>", setEntryT1)
    e1T1.pack()
    e1T1.focus()

    l2T1 = ttk.Label(t1, text="คำตอบ", font=font1)
    l2T1.pack()

    e2T1 = ttk.Entry(t1, font=font2, width=60)
    e2T1.bind("<Return>", saveQuestionT1)
    e2T1.pack()

    b1T1 = ttk.Button(t1, text="บันทึก", command=saveQuestionT1)
    b1T1.pack(ipadx=60, ipady=30 ,pady=30)
#######################################################################################################

#######################################################################################################
    headerT2 = ["คำถาม"]
    headerSizeT2 = [780]
    tableLogT2 = ttk.Treeview(t2, columns=headerT2, show="headings", height=16)
    tableLogT2.pack()
    for hT2, sT2 in zip(headerT2, headerSizeT2) :
        tableLogT2.heading(hT2, text=hT2)
        tableLogT2.column(hT2, width=sT2)
    connectToDB()
    resultLogT2 = browseSQL("SELECT question_log FROM log_table")
    if len(resultLogT2) > 0 :
        for l in resultLogT2 :
            tableLogT2.insert("", "end", value=l)
    tableLogT2.bind("<Double-1>", increaseQT2N)

    b1T2 = ttk.Button(t2, text="โหลดใหม่", command=reloadLogT2)
    b1T2.pack(ipadx=20, ipady=10 ,pady=4)

    b2T2 = ttk.Button(t2, text="ลบประวัติ", command=deletlLogT2)
    b2T2.pack(ipadx=20, ipady=10 ,pady=4)
#######################################################################################################

#######################################################################################################
    headerT3 = ["คำถาม", "คำตอบ"]
    headerSizeT3 = [390, 390]
    tableLogT3 = ttk.Treeview(t3, columns=headerT3, show="headings", height=16)
    tableLogT3.pack()
    for hT3, sT3 in zip(headerT3, headerSizeT3) :
        tableLogT3.heading(hT3, text=hT3)
        tableLogT3.column(hT3, width=sT3)
    connectToDB()
    resultLogT3 = browseSQL("SELECT question, answer FROM question_table, answer_table WHERE answer_fk = id_answer")
    if len(resultLogT3) > 0 :
        for l in resultLogT3 :
            tableLogT3.insert("", "end", value=l)
    tableLogT3.bind("<Double-1>", editeAllQT3N)

    b1T3 = ttk.Button(t3, text="โหลดใหม่", command=reloadAllT3)
    b1T3.pack(ipadx=20, ipady=10 ,pady=30)
#######################################################################################################

#######################################################################################################
    b1T4 = ttk.Button(t4, text="คืนค่าการตั้งค่า", command=restoreConfigT4)
    b1T4.pack(ipadx=20, ipady=10 ,pady=4)
    b2T4 = ttk.Button(t4, text="คืนค่าฐานข้อมูล", command=restoreDataBaseT4)
    b2T4.pack(ipadx=20, ipady=10 ,pady=4)
    b3T4 = ttk.Button(t4, text="คืนค่าทั้งหมด", command=restoreAllT4)
    b3T4.pack(ipadx=20, ipady=10 ,pady=4)
#######################################################################################################

#######################################################################################################
    ManageGUI.mainloop()
#######################################################################################################

if __name__ == "__main__" :
    maimManageGUI()