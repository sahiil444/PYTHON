from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import API

class NLPApp:


    def __init__(self):
        self.dbo = Database()   
        self.apio = API()
        self.root = Tk()
        self.root.title('NLPApp')
        self.root.geometry('350x600')
        self.root.configure(bg='#34495E')
        # self.root.iconbitmap('resorces/favicon.ico')
        self.login_gui()
        self.root.mainloop()

    def login_gui(self):

        self.clean_gui()

        heading = Label(self.root,text='NLPApp',bg='#34495E',fg='white')
        heading.pack(pady=(20,20))
        heading.configure(font=('verdana',20,'bold'))

        label1 = Label(self.root,text='Enter Email',bg="#81A8CF",fg='white',width=15)
        label1.pack(pady=(5,5))
        label1.configure(font=('verdana',12))

        self.email_input = Entry(self.root,width=25)
        self.email_input.pack(pady=(4,5),ipady=1.5)

        label2 = Label(self.root,text='Enter Password ',bg="#81A8CF",fg='white',width=15)
        label2.pack(pady=(14,4))
        label2.configure(font=('verdana',12))

        self.pass_input = Entry(self.root,width=25,show='*')
        self.pass_input.pack(pady=(5,5),ipady=1.5)

        login_butn = Button(self.root,text='Login',width=21,height=1,command=self.perform_login)
        login_butn.pack(pady=(14,5))

        label2 = Label(self.root,text='Not a member? ',bg="#81A8CF",fg='white',width=15)
        label2.pack(pady=(14,4))
        label2.configure(font=('verdana',12))

        register_butn = Button(self.root,text='Register Now ',width=21,height=1,command=self.register_gui)
        register_butn.pack(pady=(14,5))

    def register_gui(self):

        self.clean_gui()

        heading = Label(self.root,text='NLPApp',bg='#34495E',fg='white')
        heading.pack(pady=(20,20))
        heading.configure(font=('verdana',20,'bold'))

        label0 = Label(self.root,text='Enter Name',bg="#81A8CF",fg='white',width=16)
        label0.pack(pady=(5,5))
        label0.configure(font=('verdana',12))

        self.name_input = Entry(self.root,width=27)
        self.name_input.pack(pady=(4,5),ipady=1.5)

        label1 = Label(self.root,text='Enter Email',bg="#81A8CF",fg='white',width=16)
        label1.pack(pady=(5,5))
        label1.configure(font=('verdana',12))

        self.email_input = Entry(self.root,width=27)
        self.email_input.pack(pady=(4,5),ipady=1.5)

        label2 = Label(self.root,text='Enter Password ',bg="#81A8CF",fg='white',width=16)
        label2.pack(pady=(14,4))
        label2.configure(font=('verdana',12))

        self.pass_input = Entry(self.root,width=27,show='*')
        self.pass_input.pack(pady=(5,5),ipady=1.5)

        register_butn = Button(self.root,text='Register',width=22,height=1,command=self.perform_registation)
        register_butn.pack(pady=(14,5))

        label3 = Label(self.root,text='Already a member? ',bg="#81A8CF",fg='white',width=16)
        label3.pack(pady=(14,4))
        label3.configure(font=('verdana',12))

        login_butn = Button(self.root,text='Login ',width=22,height=1,command=self.login_gui)
        login_butn.pack(pady=(14,5))


    def perform_registation(self):

        name = self.name_input.get()
        email = self.email_input.get()
        password = self.pass_input.get()

        response = self.dbo.add_data(name,email,password)
        if response:
            messagebox.showinfo('Success','Registation Successfull. You can login now')
        else:
            messagebox.showerror('Error','Email already exist')


    def perform_login(self):

        email = self.email_input.get()
        password = self.pass_input.get()

        response = self.dbo.search(email,password)
        if response:
            messagebox.showinfo('Success','Login Successfull')
            self.home_gui()
        else:
            messagebox.showerror('Error','Incorrect email/Password')


    def home_gui(self):

        self.clean_gui()

        heading = Label(self.root,text='NLPApp',bg='#34495E',fg='white')
        heading.pack(pady=(20,20))
        heading.configure(font=('verdana',20,'bold'))

        Sentiment_butn = Button(self.root,text='Sentiment Analysis ',width=30,height=4,command=self.sentiment_gui)
        Sentiment_butn.pack(pady=(14,5))

        ner_butn = Button(self.root,text='Name Entity Recognition ',width=30,height=4,command=self.ner_gui)
        ner_butn.pack(pady=(14,5))

        grammar_Correction_butn = Button(self.root,text='grammar_Correction',width=30,height=4,command=self.grammar_Correction_gui)
        grammar_Correction_butn.pack(pady=(14,5))

        logout_butn = Button(self.root,text='Logout',width=10,height=1,command=self.login_gui)
        logout_butn.pack(pady=(14,5))


    def sentiment_gui(self):

        self.clean_gui()

        heading = Label(self.root,text='NLPApp',bg='#34495E',fg='white')
        heading.pack(pady=(20,20))
        heading.configure(font=('verdana',20,'bold'))

        heading2 = Label(self.root,text='Sentiment Analysis',bg='#34495E',fg='white')
        heading2.pack(pady=(10,10))
        heading2.configure(font=('verdana',14,'bold','underline'))


        label1 = Label(self.root,text='Enter the text ',bg="#81A8CF",fg='white',width=15)
        label1.pack(pady=(10,10))
        label1.configure(font=('verdana',15))

        self.text = Entry(self.root,width=33)
        self.text.pack(pady=(10,10),ipady=5)

        sentiment_butn = Button(self.root,text='Analyze Sentiment',width=28,height=2,command=self.do_sentiment_analysis)
        sentiment_butn.pack(pady=(10,10))

        self.sentiment_result = Label(self.root,text='',bg='#34495E',fg='white')
        self.sentiment_result.pack(pady=(10,10))
        self.sentiment_result.configure(font=('verdana',15))

        goback_butn = Button(self.root,text='Go Back',width=28,height=2,command=self.home_gui)
        goback_butn.pack(pady=(10,10))


    def do_sentiment_analysis(self):
        para = self.text.get()
        response = self.apio.sentiment_analysis(para)
        txt = ''
        for i in response['scored_labels']:
            txt = '->' + i['label']

        self.sentiment_result['text'] = txt


    def ner_gui(self):
        self.clean_gui()

        heading = Label(self.root,text='NLPApp',bg='#34495E',fg='white')
        heading.pack(pady=(20,20))
        heading.configure(font=('verdana',20,'bold'))

        heading2 = Label(self.root,text='Name Entity Recogination',bg='#34495E',fg='white')
        heading2.pack(pady=(10,10))
        heading2.configure(font=('verdana',14,'bold','underline'))

        label1 = Label(self.root,text='Enter the text ',bg="#81A8CF",fg='white',width=15)
        label1.pack(pady=(10,10))
        label1.configure(font=('verdana',15))

        self.text = Entry(self.root,width=33)
        self.text.pack(pady=(10,10),ipady=5)

        ner_butn = Button(self.root,text='Analyze NER',width=28,height=2,command=self.do_ner_analysis)
        ner_butn.pack(pady=(10,10))

        self.ner_result = Label(self.root,text='',bg='#34495E',fg='white')
        self.ner_result.pack(pady=(10,10))
        self.ner_result.configure(font=('verdana',15))

        goback_butn = Button(self.root,text='Go Back',width=28,height=2,command=self.home_gui)
        goback_butn.pack(pady=(10,10))

    def do_ner_analysis(self):
        para = self.text.get()
        result = self.apio.ner_analysis(para)
        display_txt = ''
        for i in result['entities']:
            display_txt = display_txt + i['type'] + '->' + i['text'] + '\n'

        self.ner_result['text'] = display_txt



    def grammar_Correction_gui(self):

        self.clean_gui()

        heading = Label(self.root,text='NLPApp',bg='#34495E',fg='white')
        heading.pack(pady=(20,20))
        heading.configure(font=('verdana',20,'bold'))

        heading2 = Label(self.root,text='Grammar Correction',bg='#34495E',fg='white')
        heading2.pack(pady=(10,10))
        heading2.configure(font=('verdana',14,'bold','underline'))

        label1 = Label(self.root,text='Enter the text ',bg="#81A8CF",fg='white',width=15)
        label1.pack(pady=(10,10))
        label1.configure(font=('verdana',15))

        self.text = Entry(self.root,width=33)
        self.text.pack(pady=(10,10),ipady=5)

        grammar_Correction_butn = Button(self.root,text='Grammar Correction',width=28,height=2,command=self.do_grammar_Correction_analysis)
        grammar_Correction_butn.pack(pady=(10,10))

        self.grammar_Correction_result = Label(self.root,text='',bg='#34495E',fg='white')
        self.grammar_Correction_result.pack(pady=(10,10))
        self.grammar_Correction_result.configure(font=('verdana',15))

        goback_butn = Button(self.root,text='Go Back',width=28,height=2,command=self.home_gui)
        goback_butn.pack(pady=(10,10))    


    def do_grammar_Correction_analysis(self):
        para = self.text.get()
        result = self.apio.grammar_Correction_analysis(para)
        txt = result['correction']
        self.grammar_Correction_result['text'] = txt

    def clean_gui(self):
        for i in self.root.pack_slaves():
            i.destroy()

nlp = NLPApp()