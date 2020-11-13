from tkinter import *
import pymysql
from tkinter import messagebox
import tkinter.ttk as ttk
from time import sleep
import random
import time
from datetime import datetime

connection = pymysql.connect(host='localhost', user='root', password='root', db='BD_testing_app', port=3306)
cursor = connection.cursor()
role = ''
cur_question = 0
cor_value = None
max_questions = None
test_answers = []
cur_user = None

class Table(Frame):
    def __init__(self, parent=None, headings=tuple(), rows=tuple()):
        super().__init__(parent)

        table = ttk.Treeview(self, show="headings", selectmode="browse")
        table["columns"] = headings
        table["displaycolumns"] = headings

        for head in headings:
            table.heading(head, text=head, anchor=CENTER)
            table.column(head, anchor=CENTER)

        for row in rows:
            table.insert('', END, values=tuple(row))

        scrolltable = Scrollbar(self, command=table.yview)
        table.configure(yscrollcommand=scrolltable.set)
        scrolltable.pack(side=RIGHT, fill=Y)
        table.pack(expand=YES, fill=BOTH)



class UserForm(Toplevel):
    def __init__(self):
        global cur_question, cor_value, max_questions, r_var, test_answers
        x = 0.1
        y = 0.2
        start_time = time.time()

        def sbm_answer():
            global cur_user
            try:
                r_var.get()
            except Exception:
                messagebox.showinfo('Ошибка', 'Ввыберите вариант ответа')
                return
            if cur_question < max_questions - 1:
                next['state'] = 'normal'
            else:
                if r_var.get() == cor_value:
                    print('success')
                    test_answers[cur_question] = 1
                else:
                    print('unsuccess')

                next['state'] = 'disabled'
                self.destroy()
                EndForm = Toplevel(root)
                EndForm.title('Форма пользователя')
                EndForm.resizable(False, False)
                EndForm.geometry('600x300')
                EndForm.grab_set()
                EndForm.focus_set()

                c = 0
                for el in test_answers:
                    if el == 1:
                        c += 1
                ans_percent = float(c / max_questions)
                ans_percent *= 100
                ans_percent = '%.2f' % ans_percent
                ans_percent = str(ans_percent) + '%'
                print(ans_percent)
                res = Label(EndForm, text=f'Вы ответили правильно на {c} вопросов из {max_questions}', font='Tahoma 18')
                res.place(relx=0.1, rely=0.4)

                temp = time.time() - start_time
                temp = '%.2f' % temp
                vremya = Label(EndForm, text=f'Время прохождения теста {temp} секунд', font='Tahoma 18')
                vremya.place(relx=0.1, rely=0.5)
                vals = (cur_user, ans_percent, temp)
                cursor.execute('INSERT INTO users_info VALUES(%s,%s,%s);', vals)
                connection.commit()
                return
            if cur_question > 0:
                prev['state'] = 'normal'
            else:
                prev['state'] = 'disabled'
            if r_var.get() == cor_value:
                print('success')
                test_answers[cur_question] = 1
            else:
                print('unsuccess')
            submit['state'] = 'disabled'

        def next_question():
            x = 0.1
            y = 0.2

            global cur_question, cor_value, max_questions, r_var
            cur_question += 1
            submit['state'] = 'normal'
            if cur_question < max_questions - 1:
                next['state'] = 'normal'
            else:
                next['state'] = 'disabled'
            if cur_question > 0:
                prev['state'] = 'normal'
            else:
                prev['state'] = 'disabled'
            question['text'] = questions[cur_question][1]

            temp_text = questions[cur_question][1]
            vals = (temp_text,)
            cursor.execute('SELECT question_id FROM test_question WHERE question = %s;', vals)
            temp_id = cursor.fetchall()

            vals = (temp_id[0][0],)
            cursor.execute('SELECT * FROM `test_answers` WHERE `question_id` = %s;', vals)
            answers = cursor.fetchall()
            buttons = []
            for i in range(len(answers)):
                if answers[i][2] == 1:
                    cor_value = i
                buttons.append(
                    Radiobutton(self, text=answers[i][1], variable=r_var, value=i, indicatoron=0, height=2, width=5))
            random.shuffle(buttons)
            difference = 7 - len(answers)
            for i in range(difference):
                buttons.append(
                    Radiobutton(self, text='-', variable=r_var, value=1000, indicatoron=0, height=2, width=5))
            for button in buttons:
                button.place(relx=x, rely=y)
                y += 0.05

            r_var.set(None)

        def prev_question():
            x = 0.1
            y = 0.2

            global cur_question, cor_value, max_questions, r_var
            cur_question -= 1
            submit['state'] = 'normal'
            if cur_question < max_questions - 1:
                next['state'] = 'normal'
            else:
                next['state'] = 'disabled'
            if cur_question > 0:
                prev['state'] = 'normal'
            else:
                prev['state'] = 'disabled'
            question['text'] = questions[cur_question][1]
            vals = (cur_question + 1,)
            cursor.execute('SELECT * FROM `test_answers` WHERE `question_id` = %s;', vals)
            answers = cursor.fetchall()
            buttons = []
            for i in range(len(answers)):
                if answers[i][2] == 1:
                    cor_value = i
                buttons.append(
                    Radiobutton(self, text=answers[i][1], variable=r_var, value=i, indicatoron=0, height=2, width=5))
            random.shuffle(buttons)
            difference = 7 - len(answers)
            for i in range(difference):
                buttons.append(
                    Radiobutton(self, text='-', variable=r_var, value=1000, indicatoron=0, height=2, width=5))
            for button in buttons:
                button.place(relx=x, rely=y)
                y += 0.05
            r_var.set(None)

        super().__init__()
        self.title('Форма пользователя')
        self.resizable(False, False)
        self.geometry('1024x860')
        self.grab_set()
        self.focus_set()
        Form1.withdraw()

        question = Label(self, text='...', font='Tahoma 24')
        question.place(relx=0.1, rely=0.1)

        submit = Button(self, text='Подтвердить', font='Tahoma 24', width=15, command=sbm_answer)
        submit.place(relx=0.15, rely=0.6)

        next = Button(self, text='Следующий', font='Tahoma 24', width=15, command=next_question)
        next.place(relx=0.3, rely=0.7)

        prev = Button(self, text='Предыдущий', font='Tahoma 24', width=15, command=prev_question)
        prev.place(relx=0.02, rely=0.7)
        prev['state'] = 'disabled'

        cursor.execute('SELECT * FROM `test_question`;')
        questions = cursor.fetchall()
        max_questions = len(questions)
        question['text'] = questions[cur_question][1]
        vals = (cur_question + 1,)
        cursor.execute('SELECT * FROM `test_answers` WHERE `question_id` = %s;', vals)
        answers = cursor.fetchall()
        for _ in questions:
            test_answers.append(0)

        r_var.set(None)

        buttons = []
        for i in range(len(answers)):
            if answers[i][2] == 1:
                cor_value = i
            buttons.append(
                Radiobutton(self, text=answers[i][1], variable=r_var, value=i, indicatoron=0, height=2, width=5))
        random.shuffle(buttons)
        difference = 7 - len(answers)
        for i in range(difference):
            buttons.append(
                Radiobutton(self, text='-', variable=r_var, value=1000, indicatoron=0, height=2, width=5))
        for button in buttons:
            button.place(relx=x, rely=y)
            y += 0.05
        r_var.set(None)

        # cur_question += 1  # менять в функциях (или нет)


class PrepodForm(Toplevel):
    def __init__(self):
        super().__init__()

        self.title('Форма преподавателя')
        self.resizable(False, False)
        self.geometry('1024x860')
        self.grab_set()
        self.focus_set()
        Form1.withdraw()

        cursor.execute('SELECT * FROM `users`;')
        data = (row for row in cursor.fetchall())
        tb1 = Table(self, headings=('Логин', 'Пароль', 'ФИО', 'Роль'),
                    rows=data)
        tb1.pack(expand=YES, fill=BOTH)

        cursor.execute('SELECT * FROM `users_dates`;')
        data = (row for row in cursor.fetchall())
        tb2 = Table(self, headings=('Логин', 'Дата входа'), rows=data)
        tb2.pack(expand=YES, fill=BOTH)

        cursor.execute('SELECT * FROM `users_info`;')
        data = (row for row in cursor.fetchall())
        tb2 = Table(self, headings=('Логин', 'Процент праввильных ответов', 'время прохождения'), rows=data)
        tb2.pack(expand=YES, fill=BOTH)




class AdminForm(Toplevel):
    def __init__(self):
        def add():
            AdminAdd()

        def delete():
            AdminDelete()
        super().__init__()

        self.title('Форма админа')
        self.resizable(False, False)
        self.geometry('400x400')
        self.grab_set()
        self.focus_set()
        Form1.withdraw()

        add_btn = Button(self, text='Добавление', font='Tahoma 24', width=15, command=add)
        add_btn.place(relx=0.15, rely=0.3)

        del_btn = Button(self, text='Удаление', font='Tahoma 24', width=15, command=delete)
        del_btn.place(relx=0.15, rely=0.6)


class AdminAdd(Toplevel):
    def __init__(self):
        ans = []
        def add_question():
            vals = (equestion.get(),)
            cursor.execute('INSERT INTO `test_question` (`question`) VALUES (%s);', vals)
            connection.commit()
            cursor.execute('SELECT `question_id` FROM test_question WHERE `question` = %s;', vals)
            question_id = cursor.fetchall()
            for i in range(7):
                if eanswers[i].get() != '':
                    ans.append(eanswers[i].get())
            print(question_id)
            for i in range(len(ans)):
                if i == 0:
                    vals = (int(question_id[0][0]), ans[i], 1)
                    cursor.execute('INSERT INTO test_answers VALUES(%s,%s,%s);', vals)
                    connection.commit()
                else:
                    vals = (int(question_id[0][0]), ans[i], 0)
                    cursor.execute('INSERT INTO test_answers VALUES(%s,%s,%s);', vals)
                    connection.commit()



        y = 0.37
        y2 = 0.37
        super().__init__()

        self.title('Форма добавления')
        self.resizable(False, False)
        self.geometry('400x600')
        self.grab_set()
        self.focus_set()

        lquestion = Label(self, text='Введите вопрос')
        lquestion.place(relx=0.1, rely=0.2)

        equestion = Entry(self)
        equestion.place(relx=0.4, rely=0.2)

        lanswers = []

        for i in range(7):
            lanswers.append(Label(self, text='Введите ответ'))
            lanswers[i].place(relx=0.1, rely=y)
            y += 0.07

        eanswers = []

        for i in range(7):
            eanswers.append(Entry(self))
            eanswers[i].place(relx=0.4, rely=y2)
            y2 += 0.07

        correct = Label(self, text='- правильный')
        correct.place(relx=0.73, rely=0.37)

        add = Button(self, text='Добавить', font='Tahoma 24', width=15, command=add_question)
        add.place(relx=0.15, rely=0.87)


class AdminDelete(Toplevel):
    def __init__(self):
        def delete_question():
            try:
                vals = (int(edelete.get()),)
                cursor.execute('DELETE FROM `test_question` WHERE `question_id` = %s;', vals)
                connection.commit()
                cursor.execute('DELETE FROM `test_answers` WHERE `question_id` = %s;', vals)
                connection.commit()
            except Exception:
                messagebox.showinfo('Ошибка', 'Неверное значение айди')
        super().__init__()
        self.title('Форма удаления')
        self.resizable(False, False)
        self.geometry('400x400')
        self.grab_set()
        self.focus_set()

        ldelete = Label(self,text='Введите id теста для удаления')
        ldelete.place(relx=0.1, rely=0.2)

        edelete = Entry(self)
        edelete.place(relx=0.6, rely=0.2)

        del_button = Button(self, text='Удалить', font='Tahoma 24', width=15, command=delete_question)
        del_button.place(relx=0.15, rely=0.6)


class Remember(Toplevel):
    def __init__(self, master):
        def change():
            if elogin.get() != '' and epassword.get() != '' and enewpassword.get() != '':
                cursor.execute('SELECT * FROM `users`;')
                users = cursor.fetchall()
                for user in users:
                    if elogin.get() == user[0] and epassword.get() == user[1]:
                        if user[3] == 'Пользователь':
                            vals = (enewpassword.get(), elogin.get())
                            cursor.execute('UPDATE users SET password = %s WHERE login = %s;', vals)
                            connection.commit()
                            messagebox.showinfo('Успех', 'Инфорация изменена')
                            sleep(0.3)
                            self.destroy()
            else:
                messagebox.showinfo('Провал', 'Что-то не так')
        super().__init__()

        self.master = master
        self.title('Восстановить пароль')
        self.resizable(False, False)
        self.geometry('320x600')
        self.grab_set()
        self.focus_set()

        login = Label(self, text='Логин', font='Tahoma 24')
        login.place(x=20, y=90)

        password = Label(self, text='Пароль', font='Tahoma 24')
        password.place(x=15, y=150)

        new_password = Label(self, text='Новый', font='Tahoma 24')
        new_password.place(x=20, y=210)

        elogin = Entry(self, justify=CENTER)
        elogin.place(x=135, y=106)

        epassword = Entry(self, show='*', justify=CENTER)
        epassword.place(x=135, y=166)

        enewpassword = Entry(self, show='*', justify=CENTER)
        enewpassword.place(x=135, y=226)

        enter = Button(self, text='Изменить', font='Tahoma 24', width=15, command=change)
        enter.place(x=20, y=400)


class Registration(Toplevel):
    def __init__(self, master):
        def select_item(event):
            global role
            role = (listbox.get(listbox.curselection()))
            print(role)

        def create_user():
            if ereglog != '' and eregpass != '' and eregfio != '' and role != '':
                coincidence = False
                cursor.execute('SELECT * FROM `users`')
                users = cursor.fetchall()
                for user in users:
                    if ereglog.get() == user[0]:
                        coincidence = True
                        messagebox.showinfo('Ошибка', 'Такой логин занят')
                        break
                if not coincidence:
                    log = str(ereglog.get())
                    passw = str(eregpass.get())
                    fio = str(eregfio.get())
                    vals = (log, passw, fio, str(role))
                    cursor.execute('INSERT INTO `users` VALUES (%s, %s, %s, %s);', vals)
                    connection.commit()
                    messagebox.showinfo('Успех', 'Инфорация добавлена')
                    sleep(0.3)
                    self.destroy()

            else:
                messagebox.showinfo('Ошибка', 'Что то пошло не так')

        super().__init__()
        self.master = master
        self.title('Оболочка для тестирования')
        self.resizable(False, False)
        self.geometry('1024x860')
        self.grab_set()
        self.focus_set()

        reglog = Label(self, text='Логин', font='Tahoma 24')
        reglog.place(relx=0.3, rely=0.3)

        regpass = Label(self, text='Пароль', font='Tahoma 24')
        regpass.place(rely=0.37, relx=0.3)

        regfio = Label(self, text='ФИО', font='Tahoma 24')
        regfio.place(rely=0.44, relx=0.3)

        regrole = Label(self, text='Роль', font='Tahoma 24')
        regrole.place(rely=0.51, relx=0.3)

        ereglog = Entry(self, justify=CENTER)
        ereglog.place(relx=0.43, rely=0.32)

        eregpass = Entry(self, show='*', justify=CENTER)
        eregpass.place(relx=0.43, rely=0.39)

        eregfio = Entry(self, justify=CENTER)
        eregfio.place(relx=0.43, rely=0.46)

        listbox = Listbox(self, width=17, height=2, font=('Tahoma', 10))
        listbox.bind('<<ListboxSelect>>', select_item)
        listbox.place(relx=0.43, rely=0.53)

        data = ('Пользователь', 'Преподаватель')
        for row in data:
            listbox.insert(END, row)

        friendly = Label(self, text='Enter your login and password, please!', font='Tahoma 24')
        friendly.place(relx=0.15, rely=0.20)

        create = Button(self, text='Create', font='Tahoma 24', width=15, command=create_user)
        create.place(relx=0.3, rely=0.6)


class AuthenticationScreen(Toplevel):
    def __init__(self):
        def onclose():
            self.destroy()
            root.destroy()

        def register():
            Form2 = Registration(Form1)

        def enter():
            global cur_user
            if elogin.get() != '' and epassword.get() != '':
                cursor.execute('SELECT * FROM `users`;')
                users = cursor.fetchall()
                for user in users:
                    if elogin.get() == user[0] and epassword.get() == user[1]:
                        if user[3] == 'Пользователь':
                            cur_user = elogin.get()
                            cur_date = datetime.now()
                            date_time = cur_date.strftime("%m/%d/%Y")
                            vals = (elogin.get(), date_time)
                            cursor.execute('INSERT INTO users_dates VALUES(%s,%s);', vals)
                            connection.commit()
                            Form3 = UserForm()
                        elif user[3] == 'Преподаватель':
                            Form5 = PrepodForm()
                if elogin.get() == 'admin' and epassword.get() == 'admin':
                    Form4 = AdminForm()

        def remember():
            Remember(Form1)

        super().__init__()

        self.title('Оболочка для тестирования')
        self.resizable(False, False)
        self.geometry('320x600')
        self.protocol("WM_DELETE_WINDOW", onclose)

        login = Label(self, text='Логин', font='Tahoma 24')
        login.place(x=20, y=90)

        password = Label(self, text='Пароль', font='Tahoma 24')
        password.place(x=15, y=150)

        # fio = Label(self, text='ФИО', font='Tahoma 24')
        # fio.place(x=30, y=210)

        elogin = Entry(self, justify=CENTER)
        elogin.place(x=135, y=106)

        epassword = Entry(self, show='*', justify=CENTER)
        epassword.place(x=135, y=166)

        # efio = Entry(self, justify=CENTER)
        # efio.place(x=135, y=226)

        enter = Button(self, text='Войти', font='Tahoma 24', width=15, command=enter)
        enter.place(x=20, y=400)

        register = Button(self, text='Регистрация', font='Tahoma 24', width=15, command=register)
        register.place(x=20, y=500)

        bremember = Button(self, text='Восстановить', font='Tahoma 24', width=15, command=remember)
        bremember.place(x=20, y=300)


if __name__ == '__main__':
    root = Tk()
    r_var = IntVar()
    root.withdraw()
    Form1 = AuthenticationScreen()

    root.mainloop()

    connection.close()
