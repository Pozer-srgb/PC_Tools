import os
import tkinter as tk
from tkinter import ttk, messagebox

class DiskCleaner:
    def __init__(self, parent):
        self.parent = parent
        self.root = ttk.Frame(parent)
        self.root.pack(fill="both", expand=True)
        self.create_widgets()

    def create_widgets(self):
        # Кнопка анализа
        self.scan_btn = ttk.Button(self.root, text="Сканировать", command=self.scan_disk)
        self.scan_btn.pack(pady=10)

        # Дерево файлов
        self.tree = ttk.Treeview(self.root, columns=("size"), show='headings')
        self.tree.heading("#0", text="Файл")
        self.tree.heading("size", text="Размер (МБ)")
        self.tree.pack(fill="both", expand=True)

        # Кнопка очистки
        self.clean_btn = ttk.Button(self.root, text="Очистить", command=self.clean_files)
        self.clean_btn.pack(pady=10)
    
    def scan_disk(self):
        """Поиск временных файлов"""
        temp_dirs = ["C:/Windows/Temp", os.environ["TEMP"]]
        for dir in temp_dirs:
            for root, _, files in os.walk(dir):
                for file in files:
                    path = os.path.join(root, file)
                    size = os.path.getsize(path) / 1024 / 1024
                    self.tree.insert("", "end", text=path, values=(f"{size:.2f}"))
    
    def clean_files(self):
        """Удаление выбранных файлов"""
        for item in self.tree.selection():
            path = self.tree.item(item, "text")
            try:
                os.remove(path)
                self.tree.delete(item)
            except Exception as e:
                messagebox.showerror("Ошибка", str(e))
