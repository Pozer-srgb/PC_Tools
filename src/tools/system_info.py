import psutil
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk

def setup_tool(app):
    """Кнопка для показа системной информации"""
    def show_sysinfo():
        info = f"""
        Процессор: {psutil.cpu_percent()}% загружен
        Память: {psutil.virtual_memory().percent}% использовано
        """
        messagebox.showinfo("Системная информация", info)

    return ctk.CTkButton(app, text="Системная информация", command=show_sysinfo)