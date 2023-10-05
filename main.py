import tkinter.messagebox
from tkinter import ttk
from tkinter import *
from tkinter import font as tkf
from write_to_file import *
from back_end_3 import *


def resize_image(im, new_width, new_height):
    ow = im.width()
    oh = im.height()
    newPhotoImage = PhotoImage(width=new_width, height=new_height)
    for x in range(new_width):
        for y in range(new_height):
            xOld = int(x * ow / new_width)
            yOld = int(y * oh / new_height)
            rgb = '#%02x%02x%02x' % im.get(xOld, yOld)
            newPhotoImage.put(rgb, (x, y))
    return newPhotoImage


def clean_ans():
    z1.config(text="")
    z2.config(text="")
    z3.config(text="")
    lab_img.place(x=10000, y=10000)
    lab_img2.place(x=10000, y=10000)
    sk.place(x=10000, y=10000)
    ra.config(text="")
    cc1.config(text="")
    lab_img3.place(x=10000, y=10000)
    lk11.config(text="")
    lk21.config(text="")
    lab_img4.place(x=10000, y=10000)
    le.config(text="")
    ll1.config(text="")
    lt.config(text="")
    lpl.config(text="")
    lpl2.config(text="")
    lc2.config(text="")
    lab_img5.place(x=10000, y=10000)
    lk12.config(text="")
    lk22.config(text="")
    lab_img6.place(x=10000, y=10000)
    lee.config(text="")
    ll2.config(text="")
    lt2.config(text="")
    lab_lamb1.config(text="")
    lab_lamb2.config(text="")
    lamb1_3.config(text="")
    lamb2_3.config(text="")
    lamb3_3.config(text="")
    clean.place(x=10000, y=10000)


def but_ans():
    a1 = a1_en.get()
    b1 = b1_en.get()
    a2 = a2_en.get()
    b2 = b2_en.get()
    if a1 == '' or a2 == '' or b1 == '' or b2 == '':
        return tkinter.messagebox.showerror("Ошибка", "Заполните пустые поля!")
    a1 = int(a1)
    a2 = int(a2)
    b1 = int(b1)
    b2 = int(b2)
    if (a1 + b2) ** 2 - 4 * (a1 * b2 - a2 * b1) < 0:
        if sqrt(abs((a1 + b2) ** 2 - 4 * (a1 * b2 - a2 * b1))) != round(
                sqrt(abs((a1 + b2) ** 2 - 4 * (a1 * b2 - a2 * b1)))):
            l1, l2 = lambda_with_not(a1, a2, b1, b2)
        else:
            l1, l2 = lambda_with(a1, a2, b1, b2)
    else:
        l1 = ((a1 + b2) + sqrt((a1 + b2) ** 2 - 4 * (a1 * b2 - a2 * b1))) / 2
        l2 = ((a1 + b2) - sqrt((a1 + b2) ** 2 - 4 * (a1 * b2 - a2 * b1))) / 2
    lab_lamb1.config(text=f"\u03bb1 = {l1}")
    lab_lamb1.place(x=10, y=220)
    lab_lamb2.config(text=f"\u03bb1 = {l2}")
    lab_lamb2.place(x=10, y=250)
    if l1 == l2:
        alpha2 = "C1"
        beta2 = "C2"
        if (b1 / (l1 - a1)) == int(b1 / (l1 - a1)):
            beta1 = int(b1 / (l1 - a1))
        else:
            beta1 = b1 / (l1 - a1)
        if (beta1 / (a1 - l1)) != int(beta1 / (a1 - l1)):
            if b1 / (a1 - l1) > 0:
                if b1 / (a1 - l1) != int(b1 / (a1 - l1)):
                    alpha1 = str(beta1) + "/" + str(a1 - l1) + " " + beta2 + " - " + str(b1) + "/" + str(
                        a1 - l1) + " " + alpha2
                else:
                    alpha1 = str(beta1) + "/" + str(a1 - l1) + " " + beta2 + " - " + str(
                        int(b1 / (a1 - l1))) + " " + alpha2
            else:
                if b1 / (a1 - l1) != int(b1 / (a1 - l1)):
                    alpha1 = str(beta1) + "/" + str(a1 - l1) + " " + beta2 + " + " + str(abs(b1)) + "/" + str(
                        a1 - l1) + " " + alpha2
                else:
                    alpha1 = str(beta1) + "/" + str(a1 - l1) + " " + beta2 + " + " + str(
                        int(abs(b1 / (a1 - l1)))) + " " + alpha2
        else:
            if b1 / (a1 - l1) > 0:
                if b1 / (a1 - l1) != int(b1 / (a1 - l1)):
                    alpha1 = str(int(beta1 / (a1 - l1))) + " " + beta2 + " - " + str(b1) + "/" + str(
                        a1 - l1) + " " + alpha2
                else:
                    alpha1 = str(int(beta1 / (a1 - l1))) + " " + beta2 + " - " + str(int(b1 / (a1 - l1))) + " " + alpha2
            else:
                if b1 / (a1 - l1) != int(b1 / (a1 - l1)):
                    alpha1 = str(int(beta1 / (a1 - l1))) + " " + beta2 + " + " + str(abs(b1)) + "/" + str(
                        a1 - l1) + " " + alpha2
                else:
                    alpha1 = str(int(beta1 / (a1 - l1))) + " " + beta2 + " + " + str(
                        int(abs(b1 / (a1 - l1)))) + " " + alpha2
        beta1 = str(beta1) + " " + beta2
        imag = PhotoImage(file="figur.png")
        figur = Label(chek_ans, image=imag)
        figur.image = imag
        figur.place(x=0, y=280)
        Label(chek_ans, text="x(t)", font=tnr).place(x=10, y=280)
        Label(chek_ans, text="y(t)", font=tnr).place(x=10, y=310)
        Label(chek_ans, text="= ", font=tnr).place(x=42, y=282)
        Label(chek_ans, text="= ", font=tnr).place(x=42, y=312)
        stroka1 = "(" + alpha1 + " + " + beta1 + "t)*exp(" + str(int(l1)) + "t)"
        stroka2 = "(" + alpha2 + " + " + beta2 + "t)*exp(" + str(int(l1)) + "t)"
        Label(chek_ans, text=stroka1, font=tnr).place(x=60, y=282)
        Label(chek_ans, text=stroka2, font=tnr).place(x=60, y=312)
    elif l1 != l2 and type(l1) == float and type(l2) == float:
        k11 = 1
        k21 = (l1 - a1) * k11 / b1
        while k21 != int(k21):
            k11 += 1
            k21 = (l1 - a1) * k11 / b1
        k12 = 1
        k22 = (l2 - a1) * k12 / b1
        while k22 != int(k22):
            k12 += 1
            k22 = (l2 - a1) * k12 / b1
        k21 = int(k21)
        k22 = int(k22)
        l1 = int(l1)
        l2 = int(l2)

        z1.config(text="x(t)")
        z2.config(text="y(t)")
        ra.config(text="=")
        cc1.config(text="C1")
        le.config(text="e")
        lt.config(text="t")
        lpl.config(text="+")
        lpl2.config(text="+")
        lc2.config(text="C2")
        lee.config(text="e")
        lt2.config(text="t")

        z1.place(x=10, y=280)
        z2.place(x=10, y=310)
        lab_img.place(x=0, y=280)
        lab_img2.place(x=38, y=280)
        ra.place(x=50, y=300)
        cc1.place(x=60, y=300)
        lab_img3.place(x=87, y=280)
        lk11.config(text=k11)
        lk11.place(x=100, y=280)
        lk21.config(text=k21)
        lk21.place(x=100, y=310)
        lab_img4.place(x=130, y=280)
        le.place(x=142, y=300)
        ll1.config(text=l1)
        ll1.place(x=153, y=290)
        lt.place(x=173, y=290)
        lpl.place(x=180, y=300)
        lpl2.place(x=5, y=370)
        lc2.place(x=20, y=370)
        lab_img5.place(x=50, y=350)
        lk12.config(text=k12)
        lk22.config(text=k22)
        lk12.place(x=62, y=350)
        lk22.place(x=62, y=380)
        lab_img6.place(x=93, y=350)
        lee.place(x=105, y=370)
        ll2.config(text=l2)
        ll2.place(x=116, y=360)
        lt2.place(x=136, y=360)

    else:
        if "+" in l1:
            alpha = l1.split("+")[0]
            beta = l1.split("+")[1]
            beta = beta.replace('i', '')
            pass
        elif "-" in l1:
            if l1.split("-")[0] == "":
                alpha = "-" + l1.aplit("-")[1]
                beta = l1.split("-")[2]
                beta = beta.raplace('i', '')
                pass
        else:
            beta = l1.replace('i', '')
            pass
    clean.place(x=70, y=430)


def but_ans3():
    a1 = a1_3_en.get()
    b1 = b1_3_en.get()
    c1 = c1_3_en.get()
    a2 = a2_3_en.get()
    b2 = b2_3_en.get()
    c2 = c2_3_en.get()
    a3 = a3_3_en.get()
    b3 = b3_3_en.get()
    c3 = c3_3_en.get()
    if a1 == '' or a2 == '' or a3 == '' or b1 == '' or b2 == '' or b3 == '' or c1 == '' or c2 == '' or c3 == '':
        return tkinter.messagebox.showerror("Ошибка", "Заполните пустые поля!")
    a1 = int(a1)
    a2 = int(a2)
    a3 = int(a3)
    b1 = int(b1)
    b2 = int(b2)
    b3 = int(b3)
    c1 = int(c1)
    c2 = int(c2)
    c3 = int(c3)
    l1 = 0
    if (a1 + b2 + c3) ** 2 - 4 * (a1 * c3 + a1 * b2 + b2 * c3 - c2 * b3 - a2 * b1 - a3 * c1) < 0:
        if sqrt(abs((a1 + b2 + c3) ** 2 - 4 * (a1 * c3 + a1 * b2 + b2 * c3 - c2 * b3 - a2 * b1 - a3 * c1))) != round(
                sqrt(abs((a1 + b2 + c3) ** 2 - 4 * (a1 * c3 + a1 * b2 + b2 * c3 - c2 * b3 - a2 * b1 - a3 * c1)))):
            l2, l3 = lambda_re_im(a1, a2, a3, b1, b2, b3, c1, c2, c3)
        else:
            l2, l3 = lambda_re(a1, a2, a3, b1, b2, b3, c1, c2, c3)
    else:
        l2 = (-(a1 + b2 + c3) + sqrt(
            (a1 + b2 + c3) ** 2 - 4 * (a1 * c3 + a1 * b2 + b2 * c3 - c2 * b3 - a2 * b1 - a3 * c1))) / (-2)
        l3 = (-(a1 + b2 + c3) - sqrt(
            (a1 + b2 + c3) ** 2 - 4 * (a1 * c3 + a1 * b2 + b2 * c3 - c2 * b3 - a2 * b1 - a3 * c1))) / (-2)
    lamb1_3.config(text=f"\u03bb1 = {l1}")
    lamb1_3.place(x=280, y=240)
    lamb2_3.config(text=f"\u03bb2 = {l2}")
    lamb2_3.place(x=280, y=270)
    lamb3_3.config(text=f"\u03bb3 = {l3}")
    lamb3_3.place(x=280, y=300)
    if l2 == l3:
        pass
    elif l2 != l3 and type(l2) == float and type(l3) == float:
        z1.place(x=280, y=330)
        z2.place(x=280, y=360)
        z3.place(x=280, y=390)
        sk.place(x=260, y=320)

    else:
        if "+" in l2:
            alpha = l2.split("+")[0]
            beta = l2.split("+")[1]
            beta = beta.replace('i', '')
            pass
        elif "-" in l2:
            if l2.split("-")[0] == "":
                alpha = "-" + l2.aplit("-")[1]
                beta = l2.split("-")[2]
                beta = beta.raplace('i', '')
                pass
        else:
            beta = l2.replace('i', '')
            pass
    clean.place(x=360, y=440)


def write_to_file_with_ans():
    vol = int(text_vol.get())
    por_sys = int(combobox.get())
    if por_sys == 2:
        write_to_file_with_ans2(t, vol)
    elif por_sys == 3:
        write_to_file_with_ans3(t, vol)
    tkinter.messagebox.showinfo("Успех", "Варианты успешно созданы! ")


def write_to_file_without_ans():
    vol = int(text_vol.get())
    por_sys = int(combobox.get())
    if por_sys == 2:
        write_to_file_without_ans2(t, vol)
    elif por_sys == 3:
        write_to_file_without_ans3(t, vol)
    tkinter.messagebox.showinfo("Успех", "Варианты успешно созданы!")


def create_mas():
    por_sys = int(combobox.get())  # порядок системы
    n = int(text_abs.get())  # коэффициенты от - и до +
    vol = int(text_vol.get())  # количество вариантов
    get_rb = selected_rb.get()
    get_rb = int(get_rb)  # 1 - разные, 2 - одинаковые, 3 - комплексные
    # берём готовый массив
    if por_sys == 2:
        if get_rb == 1:
            # сделать массив из вариантов
            mas_var = []
            for i in range(vol):
                mas_var.append(different(n))
                for _ in range(i):
                    while mas_var[i] in mas_var[0:i]:
                        mas_var[i] = different(n)
        elif get_rb == 2:
            mas_var = []
            for i in range(vol):
                mas_var.append(similar(n))
                for _ in range(i):
                    while mas_var[i] in mas_var[0:i]:
                        mas_var[i] = similar(n)
        else:
            mas_var = []
            for i in range(vol):
                mas_var.append(complex_diff(n))
                for _ in range(i):
                    while mas_var[i] in mas_var[0:i]:
                        mas_var[i] = complex_diff(n)
    else:
        if get_rb == 1:
            mas_var = []
            for i in range(vol):
                mas_var.append(sys3_different(n))
                for _ in range(i):
                    while mas_var[i] in mas_var[0:i]:
                        mas_var[i] = sys3_different(n)
        elif get_rb == 2:
            mas_var = []
            for i in range(vol):
                mas_var.append(sys3_similar(n))
                for _ in range(i):
                    while mas_var[i] in mas_var[0:i]:
                        mas_var[i] = sys3_similar(n)
        else:
            mas_var = []
            for i in range(vol):
                mas_var.append(sys3_complex(n))
                for _ in range(i):
                    while mas_var[i] in mas_var[0:i]:
                        mas_var[i] = sys3_complex(n)
    return mas_var


def create_new_window():
    if combobox.get() == '':
        return tkinter.messagebox.showerror("Ошибка порядка", "Выберите порядок системы!")
    if text_abs.get() == '':
        return tkinter.messagebox.showerror("Ошибка модуля", "Задайте границы!")
    if int(text_abs.get()) < 5:
        return tkinter.messagebox.showerror("Ошибка модуля", "Слишком маленькое число.")
    if int(text_vol.get()) > 40:
        return tkinter.messagebox.showerror("Ошибка количества вариантов", "Вы хотите создать слишком много вариантов!")
    if int(text_vol.get()) < 0:
        return tkinter.messagebox.showerror("Ошибка количества вариантов", "Нельзя создать отрицательно количество вариантов!")
    if selected_rb.get() == '':
        return tkinter.messagebox.showerror("Ошибка вида решения", "Выберите вид общего решения!")
    global t
    t = create_mas()
    new_window = Toplevel(window)
    new_window.geometry('300x200')
    Label(new_window, text="Варианты сгенерированы.", font=tnr).pack()
    Button(new_window, text="Составить файл с ответами", font=tnr, command=lambda: write_to_file_with_ans()).place(x=20,
                                                                                                                   y=50)
    Button(new_window, text="Составить файл без ответов", font=tnr, command=lambda: write_to_file_without_ans()).place(
        x=15, y=100)


window = Tk()
window.title('Генератор систем ДУ')
window.geometry('600x500')
tab_control = ttk.Notebook(window)
generate = ttk.Frame(tab_control)
chek_ans = ttk.Frame(tab_control)
tab_control.add(generate, text="Генератор")
tab_control.add(chek_ans, text="Проверка")
tab_control.pack(expand=1, fill="both")
# style = ttk.Style(window)
# style.theme_create(
#    "mytheme", settings={"TFrame": {"configure": {"background": 'white'}}}
# )
# style.theme_use("mytheme")
tnr = tkf.Font(family='TimesNewRoman', size=14)
# Вкладка генератора
Label(generate, text="Сгенерировать системы", font=tnr).place(x=5, y=20)
combobox = ttk.Combobox(generate, values=[2, 3], width=1, font=tnr)
combobox.place(x=230, y=20)
Label(generate, text="порядка", font=tnr).place(x=270, y=20)

Label(generate, text="Модуль коэффициентов \u2264", font=tnr).place(x=5, y=65)
text_abs = Entry(generate, width=4, font=tnr)
text_abs.insert(0, "20")
text_abs.place(x=250, y=65)

Label(generate, text="Где собственные числа", font=tnr).place(x=5, y=145)
selected_rb = StringVar()

Label(generate, text='различны', font=tnr).place(x=260, y=106)
different_rb = ttk.Radiobutton(generate, value=1, variable=selected_rb)
different_rb.place(x=240, y=110)

Label(generate, text="равны (минимум 2)", font=tnr).place(x=260, y=141)
similar_rb = ttk.Radiobutton(generate, value=2, variable=selected_rb)
similar_rb.place(x=240, y=145)

Label(generate, text="комплексно-сопряжённые", font=tnr).place(x=260, y=176)
complex_rb = ttk.Radiobutton(generate, value=3, variable=selected_rb)
complex_rb.place(x=240, y=180)

Label(generate, text="Количество вариантов ", font=tnr).place(x=5, y=230)
text_vol = Entry(generate, width=4, font=tnr)
text_vol.insert(0, "30")
text_vol.place(x=220, y=230)
t = 0
Button(generate, text="Сгенерировать", font=tnr, command=lambda: create_new_window()).place(x=215, y=300)

# Вкладка проверки
# Первое уравнение системы
img_skoba = PhotoImage(file="res_skoba2.png")
Label(chek_ans, image=img_skoba).place(x=0, y=40)
Label(chek_ans, text="_", font=tnr).place(x=35, y=51)
Label(chek_ans, text="dx", font=tnr).place(x=30, y=46)
Label(chek_ans, text="dt", font=tnr).place(x=30, y=76)
Label(chek_ans, text="=", font=tnr).place(x=55, y=61)
a1_en = Entry(chek_ans, width=4)
a1_en.place(x=75, y=65)
Label(chek_ans, text="x +", font=tnr).place(x=105, y=60)
b1_en = Entry(chek_ans, width=4)
b1_en.place(x=140, y=65)
Label(chek_ans, text="y", font=tnr).place(x=170, y=60)
# Второе уравнение системы
Label(chek_ans, text="_", font=tnr).place(x=35, y=110)
Label(chek_ans, text="dy", font=tnr).place(x=30, y=105)
Label(chek_ans, text="dt", font=tnr).place(x=30, y=135)
Label(chek_ans, text="=", font=tnr).place(x=55, y=120)
a2_en = Entry(chek_ans, width=4)
a2_en.place(x=75, y=124)
Label(chek_ans, text="x +", font=tnr).place(x=105, y=119)
b2_en = Entry(chek_ans, width=4)
b2_en.place(x=140, y=124)
Label(chek_ans, text="y", font=tnr).place(x=170, y=119)
with_ans = Button(chek_ans, text="Ответ", font=tkf.Font(family='TimesNewRoman', size=12), command=but_ans)
with_ans.place(x=80, y=170)

# Системы третьего порядка
img_skoba3 = PhotoImage(file="res_skoba3.png")
Label(chek_ans, image=img_skoba3).place(x=250, y=0)
Label(chek_ans, text="_", font=tnr).place(x=285, y=11)
Label(chek_ans, text="dx", font=tnr).place(x=280, y=6)
Label(chek_ans, text="dt", font=tnr).place(x=280, y=36)
Label(chek_ans, text="=", font=tnr).place(x=305, y=21)
a1_3_en = Entry(chek_ans, width=4)
a1_3_en.place(x=325, y=25)
Label(chek_ans, text="x +", font=tnr).place(x=355, y=20)
b1_3_en = Entry(chek_ans, width=4)
b1_3_en.place(x=390, y=25)
Label(chek_ans, text="y +", font=tnr).place(x=420, y=20)
c1_3_en = Entry(chek_ans, width=4)
c1_3_en.place(x=455, y=25)
Label(chek_ans, text="z", font=tnr).place(x=485, y=20)
# Второе уравнение системы
Label(chek_ans, text="_", font=tnr).place(x=285, y=71)
Label(chek_ans, text="dy", font=tnr).place(x=280, y=66)
Label(chek_ans, text="dt", font=tnr).place(x=280, y=96)
Label(chek_ans, text="=", font=tnr).place(x=305, y=81)
a2_3_en = Entry(chek_ans, width=4)
a2_3_en.place(x=325, y=85)
Label(chek_ans, text="x +", font=tnr).place(x=355, y=80)
b2_3_en = Entry(chek_ans, width=4)
b2_3_en.place(x=390, y=85)
Label(chek_ans, text="y +", font=tnr).place(x=420, y=80)
c2_3_en = Entry(chek_ans, width=4)
c2_3_en.place(x=455, y=85)
Label(chek_ans, text="z", font=tnr).place(x=485, y=80)
# Третье уравнение системы
Label(chek_ans, text="_", font=tnr).place(x=285, y=131)
Label(chek_ans, text="dz", font=tnr).place(x=280, y=126)
Label(chek_ans, text="dt", font=tnr).place(x=280, y=156)
Label(chek_ans, text="=", font=tnr).place(x=305, y=141)
a3_3_en = Entry(chek_ans, width=4)
a3_3_en.place(x=325, y=145)
Label(chek_ans, text="x +", font=tnr).place(x=355, y=140)
b3_3_en = Entry(chek_ans, width=4)
b3_3_en.place(x=390, y=145)
Label(chek_ans, text="y +", font=tnr).place(x=420, y=140)
c3_3_en = Entry(chek_ans, width=4)
c3_3_en.place(x=455, y=145)
Label(chek_ans, text="z", font=tnr).place(x=485, y=140)

with_ans = Button(chek_ans, text="Ответ", font=tkf.Font(family='TimesNewRoman', size=12), command=but_ans3)
with_ans.place(x=370, y=200)

clean = Button(chek_ans, text="Очистить", font=tkf.Font(family='TimesNewRoman', size=12), command=clean_ans)
lab_lamb1 = Label(chek_ans, text=0, font=tkf.Font(family='TimesNewRoman', size=12))
lab_lamb2 = Label(chek_ans, text=0, font=tkf.Font(family='TimesNewRoman', size=12))
z1 = Label(chek_ans, text="x(t) = -5 C1 - 1 C2*exp(3.0t) + 7 C3*exp(9.0t)", font=tnr)
z2 = Label(chek_ans, text="y(t) = 1 C1 + 2 C2*exp(3.0t) + 4 C3*exp(9.0t)", font=tnr)
z3 = Label(chek_ans, text="z(t) = 11 C1 + 10 C2*exp(3.0t) + 26 C3*exp(9.0t)", font=tnr)

skim = PhotoImage(file="figur2.png")
sk = Label(chek_ans, image=skim)
sk.image = skim
img_skobka = PhotoImage(file="skobka.png")
img_skobka2 = PhotoImage(file="skobka2.png")
lab_img = Label(chek_ans, image=img_skobka)
lab_img.image = img_skobka
lab_img2 = Label(chek_ans, image=img_skobka2)
lab_img2.image = img_skobka2
ra = Label(chek_ans, text="=", font=tnr)
cc1 = Label(chek_ans, text="C1", font=tnr)
lab_img3 = Label(chek_ans, image=img_skobka)
lab_img3.image = img_skobka
lk11 = Label(chek_ans, text=0, font=tnr)
lk21 = Label(chek_ans, text=0, font=tnr)
lab_img4 = Label(chek_ans, image=img_skobka2)
lab_img4.image = img_skobka2
shrift = tkf.Font(family='TimesNewRoman', size=10)
le = Label(chek_ans, text="e", font=tnr)
ll1 = Label(chek_ans, text=0, font=shrift)
lt = Label(chek_ans, text="t", font=shrift)
lpl = Label(chek_ans, text="+", font=tnr)
lpl2 = Label(chek_ans, text="+", font=tnr)
lc2 = Label(chek_ans, text="C2", font=tnr)
lab_img5 = Label(chek_ans, image=img_skobka)
lab_img5.image = img_skobka
lk12 = Label(chek_ans, text=0, font=tnr)
lk22 = Label(chek_ans, text=0, font=tnr)
lab_img6 = Label(chek_ans, image=img_skobka2)
lab_img6.image = img_skobka2
lee = Label(chek_ans, text="e", font=tnr)
ll2 = Label(chek_ans, text=0, font=shrift)
lt2 = Label(chek_ans, text="t", font=shrift)

lamb1_3 = Label(chek_ans, text=0, font=tkf.Font(family='TimesNewRoman', size=12))
lamb2_3 = Label(chek_ans, text=0, font=tkf.Font(family='TimesNewRoman', size=12))
lamb3_3 = Label(chek_ans, text=0, font=tkf.Font(family='TimesNewRoman', size=12))

window.mainloop()
