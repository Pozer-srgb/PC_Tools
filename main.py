import tkinter as tk
from tkinter import ttk
from modules.backup_gui import BackupApp

class UltraTool:
    def __init__(self, root):
        self.root = root
        self.root.title("UltraTool")
        self.root.geometry("800x600")

        # Стилизация
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TNotebook.Tab", font=("Arial", 10, "bold"))

        # Создание вкладок
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)

        # Добавление модулей
        self.add_backup_tab()
        # self.add_disk_cleaner_tab()  # Пример другой вкладки
    
    def add_backup_tab(self):
        """Вкладка для резервного копирования"""
        backup_frame = ttk.Frame(self.notebook)
        self.notebook.add(backup_frame, text="Резервное копирование")
        BackupApp(backup_frame) # Инициализация текущего модуля

if __name__ == "__main__":
    root = tk.Tk()
    app = UltraTool(root)
    root.mainloop()