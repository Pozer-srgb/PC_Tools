import psutil
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk

def setup_tool(app):
    """Кнопка для показа системной информации"""
    def show_sysinfo():
        info = f"""
        Процессор: 
        - Загружен: {psutil.cpu_percent()}%
        - Ядра: {psutil.cpu_count()}

        Память: 
        - Использовано: {psutil.virtual_memory().percent}%
        - Всего: {round(psutil.virtual_memory().total / (1024**3), 1)} GB
        """
        messagebox.showinfo("Системная информация", info)

    return ctk.CTkButton(
        app, 
        text="💻 Системная информация",
        fg_color="#1E90FF",
        command=show_sysinfo
    )