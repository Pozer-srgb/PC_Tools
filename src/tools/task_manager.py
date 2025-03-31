import os
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk

def setup_tool(app):
    """Добавляет кнопку для открытия диспетчера задач"""
    def open_taskmgr():
        if os.name != 'nt':
            messagebox.showerror("Ошибка", "Только для Windows!")
            return
        try:
            os.system("taskmgr")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось открыть: {str(e)}")

    return ctk.CTkButton(
        app, 
        text="📂 Диспетчер задач",
        fg_color="#2E8B57",
        command=open_taskmgr
    )