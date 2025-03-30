import os
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk

def setup_tool(app):
    """Кнопка для очистки корзины (только Windows)"""
    def clean_trash():
        try:
            os.system("rd /s /q C:\\$Recycle.Bin")
            messagebox.showinfo("Успех", "Корзина очищена")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    return ctk.CTkButton(app, text="Очистить корзину", command=clean_trash)