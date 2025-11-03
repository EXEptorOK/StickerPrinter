import fitz
import math
import os
import keyboard
import time

import tkinter as tk
from tkinter import * 

width_mm = 58
height_mm = 40


window = Tk()

window.title("Печатник номеров Рамед 1.1.0")
window.geometry("600x400")

K_POINTS = 72 / 25.4
width_p = width_mm * K_POINTS
height_p = height_mm * K_POINTS

def makeStickers(amount, hospital_name, city, width_p, height_p):

    doc = fitz.open()
    name = "«" + hospital_name + "»"
    texts = [
        name,
        city, 
        "место",
        f" из {amount}"
    ]
    
    nameFontSize = 16
    if len(name) in range(4, 7): nameFontSize = 20
    elif len(name) > 7: nameFontSize = 16

    font_sizes = [nameFontSize, 14, 14, 16]
    
    
    for i in range(1, amount+1):
        page = doc.new_page(width=width_p, height=height_p)  # Этикетка: 58 × 40 мм
        
        fonts = {
        "F0": fitz.Font("helv"),  # Обычный
        "F1": fitz.Font("hebo"),  # Жирный  
        "F2": fitz.Font("heit"),  # Курсив
        "F3": fitz.Font("hebi")   # Жирный курсив
        }

        # Вставляем все шрифты в документ
        for fontname, font in fonts.items():
            page.insert_font(fontname=fontname, fontbuffer=font.buffer)

        
        y_start = 25
        page.draw_rect(rect=(0,0,width_p,height_p), color=(0, 0, 0), fill=None, width=1)
        for j, text in enumerate(texts):
            fontsize = font_sizes[j]
            
            text_width = fitz.get_text_length(text, fontname="tiro", fontsize=fontsize)
            
            x_center = (width_p - 3.2 * text_width) / 2
            if j == 0:
                page.insert_text(
                        (x_center, y_start),
                        text,
                        fontsize=fontsize,
                        fontname="F1",
                        color=(0, 0, 0),
                        overlay=False
                    )
            if j == 2:
                x_center = (width_p - 3.5 * text_width) / 2
                page.insert_text(
                        (x_center, y_start),
                        text,
                        fontsize=fontsize,
                        fontname="F2",
                        color=(0, 0, 0),
                        overlay=False
                    )
            if j == 3:
                x_center = (width_p - 2 * text_width) / 2
                page.insert_text(
                        (x_center, y_start),
                        str(i) + text,
                        fontsize=fontsize,
                        fontname="F1",
                        color=(0, 0, 0),
                        overlay=False
                    )
            else:
                page.insert_text(
                        (x_center, y_start),
                        text,
                        fontsize=fontsize,
                        fontname="F0",
                        color=(0, 0, 0),
                        overlay=False
                        )
            y_start += 25
        
    doc.save("stick.pdf")
    doc.close()
    os.system("stick.pdf")

frame = Frame(
    master=window,
    padx=30,
    pady=60,
    relief=SUNKEN,
    borderwidth=5
    )
frame.grid(row=1,column=1)

frame2 = Frame(
    master=window,
    padx=20,
    pady=10,
    relief=SUNKEN,
    borderwidth=3
    )
frame2.grid(row=2,column=1)

width_lbl = Label(
    frame, 
    text="Ширина наклейки: "
    )
width_lbl.grid(row=1, column=1, padx=10, pady=10)
width_ent = Entry(frame)
width_ent.insert(0, str(width_p))
width_ent.grid(row=1,column=2)

height_lbl = Label(
    frame,
    text="Высота наклейки: "
    )
height_lbl.grid(row=2, column=1, padx=10, pady=10)
height_ent = Entry(frame)
height_ent.insert(0, str(height_p))
height_ent.grid(row=2,column=2)

hosp_lbl = Label(
    frame, 
    text="Название санатория: "
    )
hosp_lbl.grid(row=1, column=3, padx=10, pady=10)
hosp_ent = Entry(frame)
hosp_ent.grid(row=1, column=4)

city_lbl = Label(
    frame, 
    text="Населенный пункт: "
    )
city_lbl.grid(row=2, column=3, padx=10, pady=10)
city_ent = Entry(frame)
city_ent.grid(row=2, column=4)


amount_lbl = Label(
    frame2,
    text="Количество мест: "
    )
amount_lbl.grid(row=1, column=1)

amount_ent = Entry(
    frame2,
    )
amount_ent.grid(row=1,column=2,padx=20)

print_btn = Button(
    frame2,
    text="Вывести на печать",
    padx=10,
    command=lambda: makeStickers(int(amount_ent.get()), hosp_ent.get(), city_ent.get(), int(width_ent.get()) * K_POINTS, int(height_ent.get()) * K_POINTS)
    )
print_btn.grid(row=1,column=3)


window.mainloop()