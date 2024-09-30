from tkinter.messagebox import showerror
from tkinter import *
from tkinter.ttk import Combobox
from m_caesar import *
from m_table_routing_permutation_cipher import *
import tkinter.filedialog as fd
from RSA import *
from variables_for_RSA import *
import time
import codecs




def open_error(er):
    showerror(title = "Ошибка", message = f"Ошибка: {er}")

def Start():
    global p, q, public, private, my_file, flag_txt, name_f

    def en_cl():
        clicked(1)
    
    def de_cl():
        clicked(0)
        
    def Write_file_res(vib_com, en_de_flag):
        print("Write_file_res running...")
        res = ''
        path = ""
        if en_de_flag: path = "en_"
        else: path = "de_"
        

        with open("res\\" + path + "result.txt", mode = "w") as f:

            print("vibor idet", vib_com.get())
            match vib_com.get():
                case "шифр Цезаря":
                    if en_de_flag:
                        try:
                            print(2)
                            res = Encode_caesar(my_file, int(txt2.get()))
                            print(res)
                        except:
                            showerror("Что-то пошло не так")
                    else:
                        try:
                            res = Decode_caesar(my_file, int(txt2.get()))
                        except:
                            showerror("Что-то пошло не так")
                
                case "шифр табличной маршрутной перестановки":
                    if en_de_flag:
                        res = enc(my_file)
                    else:
                        res = dec(my_file)
                    
                case "RSA":
                    if en_de_flag:
                        print("rsa running...")
                        res = encrypt(public, my_file)
                    else:
                        numbers = read_numbers_from_file(name_f)
                        res = decrypt(private, numbers)
                        
                        
                        

                        # message = input('Enter message to ecnrypt:  ')
                        # encrypted_message = encrypt(public, message)
                        # print("Encrypted message:", encrypted_message)

                        # decrypted_message = decrypt(private, encrypted_message)
                        # print("Decrypted message:", decrypted_message)

            print("res_:", res)
            if combo.get() == "RSA":
                res_str = ''
                for i in res:
                    if path == "en_":
                        # print(i, type(i))
                        res_str += str(i) + ","
                    elif path == "de_":
                        res_str += i
                print(res_str)
                f.write(res_str)
            else:
                f.write(res)
                            


    def clicked(en_de_flag):
        print("it clicked")
        flag_txt = False
        res = ''
        

        ttxtt = ""
        
        if txt.get() == "":
            flag_txt = True
        else:
            flag_txt = False
            ttxtt = txt.get()
        
        print(combo.get())
        match combo.get():
            case "шифр Цезаря":
                if en_de_flag:
                    if not flag_txt:
                        try:
                            res = Encode_caesar(ttxtt, int(txt2.get()))
                        except:
                            showerror("Что-то пошло не так")
                    else:   # для .txt файла
                        Write_file_res(combo, en_de_flag)
                else:
                    if not flag_txt:
                        try:
                            res = Decode_caesar(ttxtt, int(txt2.get()))
                        except:
                            showerror("Что-то пошло не так")
                    else:   # для .txt файла
                        Write_file_res(combo, en_de_flag)


            case "шифр табличной маршрутной перестановки":
                if en_de_flag:
                    if not flag_txt:
                        res = enc(ttxtt)
                    else:
                        Write_file_res(combo, en_de_flag)
                else:
                    if not flag_txt:
                        res = dec(ttxtt)
                    else:
                        Write_file_res(combo, en_de_flag)

            case "RSA":
                if en_de_flag:
                    if not flag_txt:
                        res = encrypt(public, ttxtt)
                    else:
                        Write_file_res(combo, en_de_flag)
                else:
                    if not flag_txt:
                        res = decrypt(private, ttxtt)
                    else:
                        Write_file_res(combo, en_de_flag)
                    
                    
                
                

                # message = input('Enter message to ecnrypt:  ')
                # encrypted_message = encrypt(public, message)
                # print("Encrypted message:", encrypted_message)

                # decrypted_message = decrypt(private, encrypted_message)
                # print("Decrypted message:", decrypted_message)
                pass
        print(res)
        

        


        


        


    def take():
        global my_file, name_f
        print("it take")
        filetypes = (("Текстовый файл", "*.txt"),)
        filename = fd.askopenfile(title = "Открыть файл", filetypes=filetypes)
        if filename:
            name_f = filename.name
            with codecs.open(filename.name, 'r', encoding = 'utf-8') as f:
               my_file = f.read()
               print(my_file, type(my_file))

        # try:
        #     one_char = my_file.read(1)                  # проверка на наличие и возможность чтения файла
        # except:
        #     print("Бим-бим")
        #     return

        # if one_char:
        #     print(one_char)
        #     my_file.seek(0, 0)                          # возвращение курсора на 0, 0 позиции
        #     # clicked()
        # else:
        #     open_error("Пустой текстовый файл.")        # ошибка на пустоту
        #     return



    window = Tk()
    window.geometry('500x500')
    window.title("Методы шифрования")

    #---------------
    combo = Combobox(window, width = 38, font = "Arial 14", state='readonly')  
    combo['values'] = ("шифр Цезаря", # вызов нового окна для сдвига
                       "шифр табличной маршрутной перестановки", 
                       "RSA")
    combo.place(relx = 0.5, rely = 0.1, anchor = CENTER)
    combo.current(0)
    #---------------


    #---------------
    lbl = Label(window, text = "Напишите в поле текст ниже или выберите файл", font = "Arial 14")
    lbl.place(relx = 0.5, rely = 0.2, anchor = CENTER)
    #---------------

    #---------------
    txt = Entry(window, width = 40, font = "Arial 14")
    txt.place(relx = 0.5, rely = 0.25, anchor = CENTER)
    #---------------
    
    #---------------
    lbl2 = Label(window, text = "Напишите какой сдвиг будет у шифра Цезаря", font = "Arial 14")
    lbl2.place(relx = 0.5, rely = 0.32, anchor = CENTER)
    #---------------

    #---------------
    txt2 = Entry(window, width = 4, font = "Arial 14")
    txt2.place(relx = 0.5, rely = 0.37, anchor = CENTER)
    #---------------


    #---------------
    take_file = Button(window, text = "Выбрать файл", command = take, font = "Arial 12")
    take_file.place(relx = 0.5, rely = 0.48, anchor = CENTER)
    #---------------



    #---------------
    but1 = Button(window, text = "Зашифровать", command = en_cl, font = "Arial 12")
    but1.place(relx = 0.3, rely = 0.9, anchor = CENTER)
    #---------------

    #---------------
    but2 = Button(window, text = "Расшифровать", command = de_cl, font = "Arial 12")
    but2.place(relx = 0.7, rely = 0.9, anchor = CENTER)
    #---------------


    window.mainloop()


if __name__ == "__main__":
    global p, q, public, private
    # p, q, public, private = gen_key_data()
    p = -1
    q = -1
    if p == -1:
        print("None")
        # p = -1, q = -1
        public, private = extract_data("res\\keys_for_RSA.txt") 
    Start()