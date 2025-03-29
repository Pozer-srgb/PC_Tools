import json
import tkinter as tk
from tkinter import ttk, messagebox
from modules.backup_gui import BackupApp
from modules.base import BaseModule

class UltraTool:
    def add_module(self, module_class, title):
        """Универсальный метод добавления модулей"""
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text=title)
        module_class(frame)

    def __init__(self, root):
        self.root = root
        self.root.title("UltraTool")
        self.root.geometry("800x600")

        self.config_file = "config.json"
        self.load_config()
        self.create_menu()
        self.load_styles()

        # Стилизация
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TNotebook.Tab", font=("Arial", 10, "bold"))

        # Создание вкладок
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)

        # Добавление модулей
        self.add_backup_tab()
        self.add_module(DiskCleaner, "Очистка диска")

    def load_styles(self):
        with open("assets/styles.css", "r") as f:
            self.root.tk.call("ttk::style", "theme", "use", "clam")
    
    def add_backup_tab(self):
        """Вкладка для резервного копирования"""
        backup_frame = ttk.Frame(self.notebook)
        self.notebook.add(backup_frame, text="Резервное копирование")
        BackupApp(backup_frame) # Инициализация текущего модуля

    def create_menu (self):
        """Создание верхнего меню"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        # Меню "Файл"
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Выход", command=self.root.quit)
        menubar.add_cascade(label="Файл", menu=file_menu)

        # Меню "Настройки"
        settings_menu = tk.Menu(menubar, tearoff=0)
        settings_menu.add_command(label="Сбросить настройки", command=self.reset_config)
        menubar.add_cascade(label="Настройки", menu=settings_menu)

    def load_config(self):
        """Загрузка последних путей из файла"""
        try:
            with open(self.config_file, "r") as f:
                self.config = json.load(f)
        except: 
            self.config = {"last_source": "", "last_backup": ""}

    def save_config(self):
        """Сохранение путей в файл"""
        with open(self.config_file, "w") as f:
            json.dump(self.config, f)

    def reset_config(self):
        """Сброс настроек"""
        self.config = {"last_source": "", "last_backup": ""}
        self.save_config()
        messagebox.showinfo("Успех", "Настройки сброшены!")

if __name__ == "__main__":
    root = tk.Tk()
    app = UltraTool(root)
    root.mainloop()