import os
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk

def setup_tool(app):
    """Добавляет кнопку для открытия диспетчера задач"""
    def open_taskmgr():
        os.system("taskmgr")

    return ctk.CTkButton(app, text="Диспетчер задач", command=open_taskmgr)