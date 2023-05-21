from importlib.resources import path
import transformers
import tkinter as tk
from tkinter import messagebox as tkMessageBox
from tkinter import ttk
from tkinter import font
from tkinter.font import BOLD
from tkinter.messagebox import QUESTION
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from datetime import datetime as DateFunctions



context = ("Doctor: Hello! What is your name? Patient: Hi, my name is Paul Walker. Doctor: Well, Can you tell me your age? Patient: I'm 32. Doktor: Okey. What can I do for you? Patient: Doctor I feel weak, vomiting and don't feel like eating. Doctor: Come and sit here. Open your mouth. Since how long are you not feeling well? Patient: Since yesterday. Doctor: No problem. Did you have motions yesterday? Patient: No Doctor. Not so freely. Doctor: Do you drink a lot of water? Patient: No Doctor, I don’t have water too much. Doctor: Did you took any medicine? Patient: Yes Doctor, I took a Crocin. Doctor: who asked you to take it? Patient: No one Doctor. I took it myself. Doctor: why did you take it? Patient: Because I felt a headache. Doctor: Nothing to be worried at. Do you need quick relief? Patient: No Doctor. It is enough you give me medicines for now. Doktor: According to my diagnosis, I only see fatigue. I'm giving you Nemis and Parol drugs. Nemis muscle relaxant and Parol to relieve pain. If you feel bad again, please stop by again. Patient: Thank you.")

questions = [ "What is the patient's first name?",  
             "What is the patient's age?", 
             "What are the patient's feelings?",
             "What is the doctor's diagnosis?",
             "What drugs did the doctor give the patient?"]


from transformers import BertForQuestionAnswering

model = BertForQuestionAnswering.from_pretrained('deepset/bert-base-cased-squad2')

from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained('deepset/bert-base-cased-squad2')

tokenizer.encode(questions[0], truncation=True, padding=True)

from transformers import pipeline

nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)

sonuc0 = nlp({
    'question' : questions[0],
    'context' : context
})

sonuc1 = nlp({
    'question' : questions[1],
     'context' : context
})

sonuc2 = nlp({
    'question' : questions[2],
     'context' : context
})

sonuc3 = nlp({
    'question' : questions[3],
     'context' : context
})

sonuc4 = nlp({
    'question' : questions[4],
     'context' : context
})

#########################################


    



#windows

win = tk.Tk()
win.geometry("700x450+0+0")
win.title("Medical Report")


tittle_label = tk.Label(win, text="Hasta Muayene Raporu", fon=("Arial", 30, BOLD), border=12, relief=tk.GROOVE)
tittle_label.pack(side=tk.TOP, fill=tk.X)

detail_frame = tk.LabelFrame(win, text="Alınan Bilgiler", font=("Arial",20), bg="lightgray", fg="white",bd=12, relief=tk.GROOVE)
detail_frame.place(x=20, y=90, width=600, height=400)


#===== ENTRY ======#

hasta_adi = tk.Label(detail_frame, text="Adı: ", font=("Arial", 15))
hasta_adi.grid(row=0, column=0, padx=2, pady=2)

hasta_adi_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 15))
hasta_adi_ent.insert(0,context[sonuc0['start']:sonuc0['end']])
hasta_adi_ent.grid(row=0, column=1, padx=2, pady=2)


#-----------------------------------------------------#

yas = tk.Label(detail_frame, text="Yaş: ", font=("Arial", 15))
yas.grid(row=2, column=0, padx=2, pady=2)

yas_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 15))
yas_ent.insert(0,context[sonuc1['start']:sonuc1['end']])
yas_ent.grid(row=2, column=1, padx=2, pady=2)

#----------------------------------------------------#

hasta_belirtileri = tk.Label(detail_frame, text="Belirtiler: ", font=("Arial", 15))
hasta_belirtileri.grid(row=3, column=0, padx=2, pady=2)

hasta_belirtileri_ent = tk.Entry(detail_frame,  bd=7, font=("Arial", 15))
hasta_belirtileri_ent.insert(0,context[sonuc2['start']:sonuc2['end']])
hasta_belirtileri_ent.grid(row=3, column=1, padx=2, pady=2)

#---------------------------------------------------#

teshis = tk.Label(detail_frame, text="Teşhis: ", font=("Arial", 15))
teshis.grid(row=4, column=0, padx=2, pady=2)

teshis_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 15))
teshis_ent.insert(0,context[sonuc3['start']:sonuc3['end']])
teshis_ent.grid(row=4, column=1, padx=2, pady=2)

#----------------------------------------------------#

ilac = tk.Label(detail_frame, text="Verilen İlaç: ", font=("Arial", 15))
ilac.grid(row=5, column=0, padx=2, pady=2)

ilac_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 15))
ilac_ent.insert(0,context[sonuc4['start']:sonuc4['end']])
ilac_ent.grid(row=5, column=1, padx=2, pady=2)

#----------------------------------------------------#



def createPdf():
    now = DateFunctions.now()
    my_canvas = canvas.Canvas(hasta_adi_ent.get()+'_muayene_raporu_'+now.strftime("%d_%m_%Y")+'.pdf', pagesize=letter)
    my_canvas.setLineWidth(.3)
    my_canvas.setFont('Helvetica', 12)
    my_canvas.drawString(30, 750, 'PATIENT EXAMINATION REPORT')
    my_canvas.drawString(30, 735, 'XX HOSPITAL')
    my_canvas.drawString(481, 750, now.strftime("%d/%m/%Y - %H:%M"))
    my_canvas.line(480, 747, 580, 747)
    my_canvas.drawString(30, 650, 'PATIENT NAME:')
    my_canvas.drawString(123, 650, hasta_adi_ent.get())
    my_canvas.line(120, 645, 580, 645)
    my_canvas.drawString(30, 597, 'PATIENT AGE:')
    my_canvas.drawString(123, 597, yas_ent.get())
    my_canvas.line(115, 593, 300, 593)
    my_canvas.drawString(30, 544, 'PATIENT SYMPTOMS:')
    my_canvas.drawString(160, 544, hasta_belirtileri_ent.get())
    my_canvas.line(157, 540, 500, 540)
    my_canvas.drawString(30, 491, 'DIAGNOSIS:')
    my_canvas.drawString(103, 491, teshis_ent.get())
    my_canvas.line(101, 486, 500, 486)
    my_canvas.drawString(30, 438, 'MEDICINE:')
    my_canvas.drawString(95, 438, ilac_ent.get())
    my_canvas.line(95, 433, 500, 433)

    my_canvas.drawString(450, 200, 'DOKTOR NAME')
    my_canvas.line(545, 180, 445, 180)
    my_canvas.drawString(460, 150, 'SIGNATURE')
    my_canvas.line(545, 130, 445, 130)

    my_canvas.save()
    tkMessageBox.showinfo("Durum", "Pdf Başarıyla oluşturuldu.")


###########################

#BUTTON#

btn_frame = tk.Frame(detail_frame, bg="lightgrey", bd=10, relief=tk.GROOVE)
btn_frame.place(x=22, y=250, width=250, height=70)

update_btn = tk.Button(btn_frame, bg="lightgrey", text="Yükle", bd=7, font=("Arial", 13), width=23,command=createPdf)
update_btn.grid(row=0, column=1, padx=3, pady=2)

update_btn.pack

win.mainloop()

