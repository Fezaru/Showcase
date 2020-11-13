import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pymysql, os, time, hashlib, webbrowser, random
import tkinter.ttk as ttk
from urllib.request import pathname2url

connection = pymysql.connect(host='localhost', user='root', password='root', db='math_app', port=3306)
cursor = connection.cursor()
webbrowser.register('Chrome', None,
                    webbrowser.BackgroundBrowser('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'))

# cursor.execute("INSERT INTO users(login,pass) VALUES(1,1);")
# connection.commit()
cor_answers = 0
temp_index = 0
question_counter = 1
tasks = set()
cur_user = ''
correct = 0


def is_digit(string):
    if string.isdigit():
        return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False


def app_onclose():
    app.destroy()
    root.destroy()


"""def test_passing(menu):
    def test_window_onclose():
        test_window.destroy()
        root.destroy()

    menu.destroy()
    test_window = Toplevel(root)
    test_window.title('ППС Решение систем нелинейных уравнений')
    test_window.geometry('1400x900')
    test_window.configure(background='#2A2B2B')
    test_window.resizable(False, False)                           
    test_window.protocol("WM_DELETE_WINDOW", test_window_onclose)"""


# выбор тестов или теории
def main_menu():
    def menu_onclose():
        menu.destroy()
        root.destroy()

    def open_theory():
        webbrowser.get('Chrome').open_new('file:///F:/PyCharmProject1/teoriya/teoriya_trpo.html')

    def choose_test():
        def test_draw():
            pass  # написать сюда отрисовку всех кнопок и лейблов

        def test_1():
            global temp_index
            global question_counter
            global tasks
            global cur_user
            global cor_answers
            question_counter = 1
            tasks.clear()
            temp_index = 0
            cor_answers = 0

            def test_window_onclose():
                test_window.destroy()
                root.destroy()

            def open_global_stats():

                def stats_on_close():
                    stats.destroy()
                    root.destroy()

                test_window.destroy()
                stats = Toplevel(root)
                stats.title('ППС Решение систем нелинейных уравнений')
                stats.geometry('1280x1024')
                stats.configure(background='WHITE')
                stats.resizable(False, False)
                stats.protocol("WM_DELETE_WINDOW", stats_on_close)
                tree = ttk.Treeview(stats)
                tree["columns"] = ("test", "mark")
                tree.column("#0", width=340, minwidth=340, stretch=tk.NO)
                tree.column("test", width=340, minwidth=340, stretch=tk.NO)
                tree.column("mark", width=340, minwidth=340, stretch=tk.NO)
                tree.heading("#0", text="Users", anchor=tk.W)
                tree.heading("test", text="Test", anchor=tk.W)
                tree.heading("mark", text="Mark", anchor=tk.W)

                cursor.execute('SELECT * FROM `test_rating`;')
                ratings = cursor.fetchall()
                for item in ratings:
                    tree.insert('', 'end', text=str(item[0]), values=(str(item[1]), str(item[2])))

                tree.pack(expand=tk.YES, fill=tk.BOTH)

            def return_menu():
                test_window.destroy()
                main_menu()

            def sign_value():
                check_x = x_entry.get()
                check_y = y_entry.get()
                if check_x != '' and check_y != '':
                    if is_digit(check_x) and is_digit(check_y):
                        global cor_answers
                        temp_x = float(x_entry.get())
                        temp_y = float(y_entry.get())
                        cor_x = float(test_answers[temp_index][2])
                        cor_y = float(test_answers[temp_index][3])
                        if temp_x == cor_x and temp_y == cor_y:
                            cor_answers += 1
                        sign.place_forget()
                        test_window.update()
                        time.sleep(0.15)
                        hint.place(relx=0.4, rely=0.75)
                        next['state'] = NORMAL
                    else:
                        messagebox.showinfo('Failure', 'insert correct value')
                else:
                    messagebox.showinfo('Failure', 'insert value')

            def show_correct():
                hint_x['text'] = 'x = ' + str(test_answers[temp_index][2])
                hint_y['text'] = 'y = ' + str(test_answers[temp_index][3])
                hint_x.place(relx=0.53, rely=0.595)
                hint_y.place(relx=0.53, rely=0.645)
                hint.place_forget()

            def next_question():  # почему то если проходить тест 2 раз на последнем вопросе (проверить) зависает
                global question_counter
                global temp_index
                global cor_answers
                global tasks
                global cur_user
                done = 0
                progress.step(10)
                hint.place_forget()
                next['state'] = DISABLED
                if question_counter == 9:
                    next['text'] = 'Finish'
                if question_counter != 10:
                    question_counter += 1
                    cur_ques['text'] = '{} of 10'.format(question_counter)
                    while temp_index in tasks:
                        temp_index = random.randint(0, 14)
                else:
                    next.place_forget()
                    tasks.clear()
                    question_counter = 1
                    urav1.place_forget()
                    urav2.place_forget()
                    x_entry.place_forget()
                    y_entry.place_forget()
                    x_equals.place_forget()
                    y_equals.place_forget()
                    cur_ques.place_forget()
                    progress.place_forget()
                    hint_x.place_forget()
                    hint_y.place_forget()
                    sign.place_forget()
                    done = 1

                    cursor.execute('SELECT * FROM `test_rating`;')
                    rating = cursor.fetchall()
                    coincidence = 0
                    best = int()
                    for temp in rating:
                        if str(cur_user) == str(temp[0]) and str(temp[1]) == '1':
                            coincidence = 1
                            best = temp[2]
                            if cor_answers > temp[2]:
                                best = cor_answers
                                upd = (cor_answers, cur_user)
                                cursor.execute('UPDATE `test_rating` SET `best_result`=%s WHERE `user`=%s,`test` = 1;',
                                               upd)
                                connection.commit()
                    if not coincidence:
                        ins = (cur_user, 1, float(cor_answers))
                        cursor.execute('INSERT INTO `test_rating` (`user`,`test`,`best_result`) VALUES (%s,%s,%s);',
                                       ins)
                        connection.commit()
                    cursor.execute('SELECT * FROM `test_rating` WHERE `test` = 1;')
                    rating = cursor.fetchall()
                    rating = list(rating)
                    marks = list()
                    for i in range(len(rating)):
                        marks.append(rating[i][2])

                    n = len(rating)
                    for i in range(n - 1):
                        for j in range(n - i - 1):
                            if marks[j] < marks[j + 1]:
                                marks[j], marks[j + 1] = marks[j + 1], marks[j]
                                rating[j], rating[j + 1] = rating[j + 1], rating[j]

                    user_index = int()
                    for temp in rating:
                        if cur_user == temp[0]:
                            user_index = rating.index(temp)

                    best = Label(test_window, text='Your best: {}'.format(int(best)), font='Tahoma 24',
                                 foreground='#DFDFDF', background='#2A2B2B')
                    best.place(relx=0.42, rely=0.27)
                    result = Label(test_window, text='Your mark: {}'.format(cor_answers), font='Tahoma 24',
                                   foreground='#DFDFDF', background='#2A2B2B')
                    result.place(relx=0.42, rely=0.33)
                    position = Label(test_window, text='Your place is: {}'.format(user_index + 1), font='Tahoma 24',
                                     foreground='#DFDFDF', background='#2A2B2B')
                    position.place(relx=0.41, rely=0.39)
                    test_stats = Button(test_window, text='View global stats', font='Tahoma 24', width=15,
                                        background='#454747',
                                        command=open_global_stats,
                                        activebackground='#5B5C5C', justify=CENTER)
                    test_stats.place(relx=0.39, rely=0.46)
                    back = Button(test_window, text='Return to menu', font='Tahoma 24', width=15,
                                  background='#454747',
                                  command=return_menu,
                                  activebackground='#5B5C5C')
                    back.place(relx=0.39, rely=0.55)

                    cor_answers = 0
                    # записать результат в базу, если он лучше предыдущего (или по другому)
                if question_counter != 11:
                    tasks.add(temp_index)
                    urav1['text'] = str(test_questions[temp_index][2])
                    urav2['text'] = str(test_questions[temp_index][3])
                    if not done:
                        sign.place(relx=0.4, rely=0.75)
                    hint_x.place_forget()
                    hint_y.place_forget()

            menu.destroy()
            test_window = Toplevel(root)
            test_window.title('ППС Решение систем нелинейных уравнений')
            test_window.geometry('1400x900')
            test_window.configure(background='#2A2B2B')
            test_window.resizable(False, False)
            test_window.protocol("WM_DELETE_WINDOW", test_window_onclose)  # ФУНКЦИИ ПРОТОКОЛЬНЫЕ ПИСАТЬ БЕЗ СКОБОЧЕК
            # добавить фигурную скобочку картинкой (не получилось)
            urav1 = Label(test_window, text='.......', font='Tahoma 24', foreground='#DFDFDF', background='#2A2B2B')
            urav1.place(relx=0.1, rely=0.1)
            urav2 = Label(test_window, text='.......', font='Tahoma 24', foreground='#DFDFDF', background='#2A2B2B')
            urav2.place(relx=0.1, rely=0.15)
            user = Label(test_window, text=cur_user, font='Tahoma 24', foreground='#DFDFDF', background='#2A2B2B',
                         width=10,
                         justify=CENTER)
            user.place(relx=0.87, rely=0.03)
            cur_ques = Label(test_window, text='{} of 10'.format(question_counter), font='Tahoma 30',
                             foreground='#DFDFDF', background='#2A2B2B')
            cur_ques.place(relx=0.88, rely=0.09)
            x_equals = Label(test_window, text='x=', font='Tahoma 24', foreground='#DFDFDF', background='#2A2B2B')
            x_equals.place(relx=0.4, rely=0.6)
            y_equals = Label(test_window, text='y=', font='Tahoma 24', foreground='#DFDFDF', background='#2A2B2B')
            y_equals.place(relx=0.4, rely=0.65)
            x_entry = Entry(test_window)
            x_entry.place(relx=0.43, rely=0.615)
            y_entry = Entry(test_window)
            y_entry.place(relx=0.43, rely=0.665)
            sign = Button(test_window, text='Sign', font='Tahoma 24', width=10, background='#454747',
                          command=sign_value,
                          activebackground='#5B5C5C')
            sign.place(relx=0.4, rely=0.75)
            hint = Button(test_window, text='Show correct', font='Tahoma 24', width=11, background='#454747',
                          command=show_correct,
                          activebackground='#5B5C5C')
            next = Button(test_window, text='Next question', font='Tahoma 24', width=12, background='#454747',
                          command=next_question,
                          activebackground='#5B5C5C', state=DISABLED)
            next.place(relx=0.8, rely=0.75)
            hint_x = Label(test_window, text='x = ', font='Tahoma 24', foreground='#DFDFDF', background='#2A2B2B')
            hint_y = Label(test_window, text='y = ', font='Tahoma 24', foreground='#DFDFDF', background='#2A2B2B')

            style = ttk.Style()
            style.theme_use('default')
            style.configure("black.Horizontal.TProgressbar", background='black')

            progress = ttk.Progressbar(test_window, length=200, style='black.Horizontal.TProgressbar')
            progress.step()
            progress.place(relx=0.85, rely=0.18)

            cursor.execute('SELECT * FROM `test_questions` WHERE `test` = 1;')
            test_questions = cursor.fetchall()
            cursor.execute('SELECT * FROM `test_answers` WHERE `test` = 1;')
            test_answers = cursor.fetchall()

            temp_index = random.randint(0, 14)
            tasks.add(temp_index)
            urav1['text'] = test_questions[temp_index][2]
            urav2['text'] = test_questions[temp_index][3]

        def exit_choosing():
            test1.place_forget()  # дописать сюда другие кнопки выбора тестов
            test2.place_forget()
            theory.place(relx=0.05, rely=0.25)
            tests.place(relx=0.05, rely=0.6)
            exit.place_forget()
            user.place(relx=0.78, rely=0.03)

        def test_2():
            global temp_index
            global question_counter
            global tasks
            global cur_user
            global cor_answers
            question_counter = 1
            tasks.clear()
            temp_index = 0
            cor_answers = 0

            def test_window_onclose():
                test_window.destroy()
                root.destroy()

            def open_global_stats():

                def stats_on_close():
                    stats.destroy()
                    root.destroy()

                test_window.destroy()
                stats = Toplevel(root)
                stats.title('ППС Решение систем нелинейных уравнений')
                stats.geometry('1280x1024')
                stats.configure(background='WHITE')
                stats.resizable(False, False)
                stats.protocol("WM_DELETE_WINDOW", stats_on_close)
                tree = ttk.Treeview(stats)
                tree["columns"] = ("test", "mark")
                tree.column("#0", width=340, minwidth=340, stretch=tk.NO)
                tree.column("test", width=340, minwidth=340, stretch=tk.NO)
                tree.column("mark", width=340, minwidth=340, stretch=tk.NO)
                tree.heading("#0", text="Users", anchor=tk.W)
                tree.heading("test", text="Test", anchor=tk.W)
                tree.heading("mark", text="Mark", anchor=tk.W)

                cursor.execute('SELECT * FROM `test_rating`;')
                ratings = cursor.fetchall()
                for item in ratings:
                    tree.insert('', 'end', text=str(item[0]), values=(str(item[1]), str(item[2])))

                tree.pack(expand=tk.YES, fill=tk.BOTH)

            def return_menu():
                test_window.destroy()
                main_menu()

            def sign_value():
                global cor_answers
                global correct
                check_x = str(x_entry.get())
                check_y = str(y_entry.get())
                if check_x != '' and check_y != '':
                    xs = check_x.split(',')
                    ys = check_y.split(',')
                    if len(xs) != 2 or len(ys) != 2:
                        messagebox.showinfo('Failure', 'Insert x1,x2 and y1,y2')
                    else:
                        value = (temp_index,)
                        cursor.execute('SELECT * FROM `test_answers` WHERE `question_id` = %s;', value)
                        ans = cursor.fetchall()
                        if ans[0][2] == float(xs[0]) and ans[1][2] == float(xs[1]) and ans[0][3] == float(ys[0]) and \
                                ans[1][3] == float(ys[1]):
                            correct = 1
                        if correct:
                            cor_answers += 1
                            correct = 0
                        sign.place_forget()
                        test_window.update()
                        time.sleep(0.15)
                        hint.place(relx=0.4, rely=0.75)
                        next['state'] = NORMAL
                else:
                    messagebox.showinfo('Failure', 'insert value')

            def show_correct():
                value = (temp_index,)
                cursor.execute('SELECT * FROM `test_answers` WHERE `question_id` = %s;', value)
                ans = cursor.fetchall()
                hint_x['text'] = 'x1,x2 = ' + str(ans[0][2]) + ',' + str(ans[1][2])
                hint_y['text'] = 'y1,y2 = ' + str(ans[0][3]) + ',' + str(ans[1][3])
                hint_x.place(relx=0.53, rely=0.595)
                hint_y.place(relx=0.53, rely=0.645)
                hint.place_forget()

            def next_question():  # почему то если проходить тест 2 раз на последнем вопросе (проверить) зависает
                global question_counter
                global temp_index
                global cor_answers
                global tasks
                global cur_user
                done = 0
                progress.step(20)
                hint.place_forget()
                next['state'] = DISABLED
                if question_counter == 4:
                    next['text'] = 'Finish'
                if question_counter != 5:
                    question_counter += 1
                    cur_ques['text'] = '{} of 5'.format(question_counter)
                    while temp_index in tasks:
                        temp_index = random.randint(16, 21)
                else:
                    next.place_forget()
                    tasks.clear()
                    question_counter = 1
                    urav1.place_forget()
                    urav2.place_forget()
                    x_entry.place_forget()
                    y_entry.place_forget()
                    x_equals.place_forget()
                    y_equals.place_forget()
                    cur_ques.place_forget()
                    progress.place_forget()
                    hint_x.place_forget()
                    hint_y.place_forget()
                    sign.place_forget()
                    done = 1
                    cor_answers *= 2

                    cursor.execute('SELECT * FROM `test_rating`;')
                    rating = cursor.fetchall()
                    coincidence = 0
                    best = int()
                    for temp in rating:
                        if str(cur_user) == str(temp[0]) and str(temp[1]) == '2':
                            coincidence = 1
                            best = temp[2]
                            if cor_answers / 2 > temp[2]:
                                best = cor_answers
                                upd = (cor_answers, cur_user)
                                cursor.execute(
                                    'UPDATE `test_rating` SET `best_result`=%s WHERE `user`=%s AND `test` = 2;',
                                    upd)
                                connection.commit()
                    if not coincidence:
                        ins = (cur_user, 2, float(cor_answers))
                        cursor.execute('INSERT INTO `test_rating` (`user`,`test`,`best_result`) VALUES (%s,%s,%s);',
                                       ins)
                        connection.commit()
                    cursor.execute('SELECT * FROM `test_rating` WHERE `test` = 2;')
                    rating = cursor.fetchall()
                    rating = list(rating)
                    marks = list()
                    for i in range(len(rating)):
                        marks.append(rating[i][2])

                    n = len(rating)
                    for i in range(n - 1):
                        for j in range(n - i - 1):
                            if marks[j] < marks[j + 1]:
                                marks[j], marks[j + 1] = marks[j + 1], marks[j]
                                rating[j], rating[j + 1] = rating[j + 1], rating[j]

                    user_index = int()
                    for temp in rating:
                        if cur_user == temp[0]:
                            user_index = rating.index(temp)

                    best = Label(test_window, text='Your best: {}'.format(int(best)), font='Tahoma 24',
                                 foreground='#DFDFDF', background='#2A2B2B')
                    best.place(relx=0.42, rely=0.27)
                    if cor_answers > 10:
                        cor_answers = 10
                    result = Label(test_window, text='Your mark: {}'.format(cor_answers), font='Tahoma 24',
                                   foreground='#DFDFDF', background='#2A2B2B')
                    result.place(relx=0.42, rely=0.33)
                    position = Label(test_window, text='Your place is: {}'.format(user_index + 1), font='Tahoma 24',
                                     foreground='#DFDFDF', background='#2A2B2B')
                    position.place(relx=0.41, rely=0.39)
                    test_stats = Button(test_window, text='View global stats', font='Tahoma 24', width=15,
                                        background='#454747',
                                        command=open_global_stats,
                                        activebackground='#5B5C5C', justify=CENTER)
                    test_stats.place(relx=0.39, rely=0.46)
                    back = Button(test_window, text='Return to menu', font='Tahoma 24', width=15,
                                  background='#454747',
                                  command=return_menu,
                                  activebackground='#5B5C5C')
                    back.place(relx=0.39, rely=0.55)

                    cor_answers = 0
                    # записать результат в базу, если он лучше предыдущего (или по другому)
                if question_counter != 6:
                    tasks.add(temp_index)
                    value = (temp_index,)
                    cursor.execute('SELECT * FROM `test_questions` WHERE `question_id` = %s;', value)
                    questions = cursor.fetchall()
                    urav1['text'] = questions[0][2]
                    urav2['text'] = questions[0][3]
                    if not done:
                        sign.place(relx=0.4, rely=0.75)
                    hint_x.place_forget()
                    hint_y.place_forget()

            menu.destroy()
            test_window = Toplevel(root)
            test_window.title('ППС Решение систем нелинейных уравнений')
            test_window.geometry('1400x900')
            test_window.configure(background='#2A2B2B')
            test_window.resizable(False, False)
            test_window.protocol("WM_DELETE_WINDOW", test_window_onclose)  # ФУНКЦИИ ПРОТОКОЛЬНЫЕ ПИСАТЬ БЕЗ СКОБОЧЕК
            # добавить фигурную скобочку картинкой (не получилось)
            urav1 = Label(test_window, text='.......', font='Tahoma 24', foreground='#DFDFDF', background='#2A2B2B')
            urav1.place(relx=0.1, rely=0.1)
            urav2 = Label(test_window, text='.......', font='Tahoma 24', foreground='#DFDFDF', background='#2A2B2B')
            urav2.place(relx=0.1, rely=0.15)
            user = Label(test_window, text=cur_user, font='Tahoma 24', foreground='#DFDFDF', background='#2A2B2B',
                         width=10,
                         justify=CENTER)
            user.place(relx=0.87, rely=0.03)
            cur_ques = Label(test_window, text='{} of 5'.format(question_counter), font='Tahoma 30',
                             foreground='#DFDFDF', background='#2A2B2B')
            cur_ques.place(relx=0.88, rely=0.09)
            x_equals = Label(test_window, text='x=', font='Tahoma 24', foreground='#DFDFDF', background='#2A2B2B')
            x_equals.place(relx=0.4, rely=0.6)
            y_equals = Label(test_window, text='y=', font='Tahoma 24', foreground='#DFDFDF', background='#2A2B2B')
            y_equals.place(relx=0.4, rely=0.65)
            x_entry = Entry(test_window)
            x_entry.place(relx=0.43, rely=0.615)
            y_entry = Entry(test_window)
            y_entry.place(relx=0.43, rely=0.665)
            sign = Button(test_window, text='Sign', font='Tahoma 24', width=10, background='#454747',
                          command=sign_value,
                          activebackground='#5B5C5C')
            sign.place(relx=0.4, rely=0.75)
            hint = Button(test_window, text='Show correct', font='Tahoma 24', width=11, background='#454747',
                          command=show_correct,
                          activebackground='#5B5C5C')
            next = Button(test_window, text='Next question', font='Tahoma 24', width=12, background='#454747',
                          command=next_question,
                          activebackground='#5B5C5C', state=DISABLED)
            next.place(relx=0.8, rely=0.75)
            hint_x = Label(test_window, text='x = ', font='Tahoma 24', foreground='#DFDFDF', background='#2A2B2B')
            hint_y = Label(test_window, text='y = ', font='Tahoma 24', foreground='#DFDFDF', background='#2A2B2B')

            style = ttk.Style()
            style.theme_use('default')
            style.configure("black.Horizontal.TProgressbar", background='black')

            progress = ttk.Progressbar(test_window, length=200, style='black.Horizontal.TProgressbar')
            progress.step()
            progress.place(relx=0.85, rely=0.18)

            temp_index = random.randint(16, 21)
            tasks.add(temp_index)
            value = (temp_index,)
            cursor.execute('SELECT * FROM `test_questions` WHERE `question_id` = %s;', value)
            questions = cursor.fetchall()
            urav1['text'] = questions[0][2]
            urav2['text'] = questions[0][3]

        theory.place_forget()
        tests.place_forget()
        test1 = Button(menu, text='Test №1', command=test_1, width=20, font='Tahoma 24', background='#454747',
                       activebackground='#5B5C5C')
        test1.place(relx=0.05, rely=0.25)
        test2 = Button(menu, text='Test №2', command=test_2, width=20, font='Tahoma 24', background='#454747',
                       activebackground='#5B5C5C')
        test2.place(relx=0.05, rely=0.6)
        exit = Button(menu, text='Go back', command=exit_choosing, width=8, font='Tahoma 24', background='#454747',
                      activebackground='#5B5C5C')
        exit.place(relx=0.8, rely=0.03)
        user.place_forget()

    app.destroy()
    menu = Toplevel(root)
    menu.title('ППС Решение систем нелинейных уравнений')
    menu.geometry('800x600')
    menu.configure(background='#2A2B2B')
    menu.resizable(False, False)
    menu.protocol("WM_DELETE_WINDOW", menu_onclose)
    theory = Button(menu, text='Theory', command=open_theory, width=20, font='Tahoma 24',
                    background='#454747',
                    activebackground='#5B5C5C')
    theory.place(relx=0.05, rely=0.25)

    tests = Button(menu, text='Choose test', command=choose_test, width=20, font='Tahoma 24', background='#454747',
                   activebackground='#5B5C5C')
    tests.place(relx=0.05, rely=0.6)
    user = Label(menu, text=cur_user, font='Tahoma 24', foreground='#DFDFDF', background='#2A2B2B', width=10,
                 justify=CENTER)
    user.place(relx=0.78, rely=0.03)


# кнопка Register
def registering():
    def create_user():
        log = ereglog.get()
        if (5 <= len(str(log)) <= 9) and eregpass.get() != '':
            coincidence = False
            cursor.execute("SELECT * FROM `users`")
            users = cursor.fetchall()
            testpass = hashlib.md5()
            testpass.update(eregpass.get().encode())
            for user in users:
                if ereglog.get() == user[1]:
                    coincidence = True
                    messagebox.showinfo('Failure', 'User already exists')
                    break
            if not coincidence:
                temp = eregpass.get()
                h = hashlib.md5()
                h.update(temp.encode())
                p = h.hexdigest()

                authorise = (ereglog.get(), p)
                cursor.execute('INSERT INTO `users` (`login`,`pass`) VALUES (%s,%s);', authorise)
                connection.commit()
                messagebox.showinfo('Success', 'Data inserted')

                time.sleep(0.5)
                reg.destroy()
        else:
            messagebox.showinfo('Failure', 'login must be from 5 to 9 symbols')

    reg = Toplevel(app)
    reg.title('ППС Решение систем нелинейных уравнений')
    reg.geometry('1024x860')
    reg.configure(background='#2A2B2B')
    reg.resizable(False, False)
    reg.grab_set()
    reg.focus_set()

    reglog = Label(reg, text='Login', font='Tahoma 24', foreground='#DFDFDF')
    reglog.place(relx=0.3, rely=0.3)
    regpass = Label(reg, text='Pass', font='Tahoma 24', foreground='#DFDFDF')
    regpass.place(rely=0.37, relx=0.3)
    regpass['background'] = '#2A2B2B'
    reglog['background'] = '#2A2B2B'

    ereglog = Entry(reg, justify=CENTER)
    ereglog.place(relx=0.39, rely=0.32)
    eregpass = Entry(reg, show='*', justify=CENTER)
    eregpass.place(relx=0.39, rely=0.39)

    friendly = Label(reg, text='Enter your login and password, please!', font='Tahoma 24', foreground='#DFDFDF',
                     background='#2A2B2B')
    friendly.place(relx=0.15, rely=0.20)

    create = Button(reg, text='Create', font='Tahoma 24', width=15, background='#454747',
                    activebackground='#5B5C5C', command=create_user)
    create.place(relx=0.3, rely=0.45)


# кнопка Enter
def entering():
    global cur_user
    if elogin.get() != '' and epassword.get() != '':
        cursor.execute("SELECT * FROM `users`")
        users = cursor.fetchall()
        testpass = hashlib.md5()
        testpass.update(epassword.get().encode())
        check = testpass.hexdigest()
        for user in users:
            if elogin.get() == user[1] and check == user[2]:
                cur_user = elogin.get()
                main_menu()
                break


if __name__ == '__main__':  # добавить изменение цветовой темы https://wiki.tcl-lang.org/page/List+of+ttk+Themes
    root = Tk()
    root.withdraw()
    app = Toplevel(root)
    app.title('ППС Решение систем нелинейных уравнений')
    app.geometry('320x600')
    app.configure(background='#2A2B2B')
    app.resizable(False, False)
    app.protocol("WM_DELETE_WINDOW", app_onclose)

    login = Label(app, text='Login', font='Tahoma 24', foreground='#DFDFDF', background='#2A2B2B')
    login.place(x=30, y=90)

    password = Label(app, text='Pass', font='Tahoma 24', foreground='#DFDFDF', background='#2A2B2B')
    password.place(x=30, y=150)

    elogin = Entry(app, justify=CENTER)
    elogin.place(x=135, y=106)
    epassword = Entry(app, show='*', justify=CENTER)
    epassword.place(x=135, y=166)

    enter = Button(app, text='Enter', font='Tahoma 24', width=15, background='#454747', command=entering,
                   activebackground='#5B5C5C')
    enter.place(x=20, y=400)
    register = Button(app, text='Registration', font='Tahoma 24', width=15, background='#454747',
                      activebackground='#5B5C5C', command=registering)
    register.place(x=20, y=500)


    root.mainloop()

    connection.close()

##2BBEB
