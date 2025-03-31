import os
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk

def setup_tool(app):
    """Кнопка для очистки корзины (только Windows)"""
    def clean_trash():
        answer = messagebox.askyesno("Подтверждение", "Очистить корзину? Это нельязя отменить!")
        if not answer:
            return
        try:
            os.system("rd /s /q C:\\$Recycle.Bin")
            messagebox.showinfo("Успех", "Корзина очищена")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    return ctk.CTkButton(
        app, 
        text="🚮 Очистить корзину",
        fg_color="#B22222",
        command=clean_trash
    )