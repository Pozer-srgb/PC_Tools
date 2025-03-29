import os
import shutil
from datetime import datetime
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import zipfile

class BackupApp:
    def __init__(self, parent):
        self.parent = parent
        self.root = ttk.Frame(self.parent)
        self.root.pack(fill="both", expand=True)
        self.progress = ttk.Progressbar(self.root, mode="indeterminate")
        self.progress.pack(pady=5)

        # Стили
        self.style = ttk.Style()
        self.style.theme_use("clam")

        # Переменные для путей
        self.source_dir = tk.StringVar()
        self.backup_root = tk.StringVar()

        # Создание элементов интерфейса
        self.create_widgets()
    
    def create_widgets(self):

        # Фрейм для исходной папки
        frame_source = ttk.LabelFrame(self.root, text="Папка для копирования")
        frame_source.pack(padx=10, pady=5, fill="x")

        ttk.Entry(frame_source, textvariable=self.source_dir, width=50).pack(side="left", padx=5)
        ttk.Button(frame_source, text="Обзор...", command=self.browse_source).pack(side="left", padx=5)

        # Фрейм для папки бэкапа
        frame_backup = ttk.LabelFrame(self.root, text="Куда сохранить")
        frame_backup.pack(padx=10, pady=5, fill="x")

        ttk.Entry(frame_backup, textvariable=self.backup_root, width=50).pack(side="left", padx=5)
        ttk.Button(frame_backup, text="Обзор...", command=self.browse_backup).pack(side="left", padx=5)

        # Кнопка создания бэкапа
        ttk.Button(self.root, text="Создать резервную копию", command=self.create_backup).pack(pady=10)

        # Статус
        self.status_label = ttk.Label(self.root, text="Готово к работе", foreground="gray")
        self.status_label.pack(pady=5)
    
    def browse_source(self):
        """Выбор исходной папки"""
        dir_path = filedialog.askdirectory()
        if dir_path:
            self.source_dir.set(dir_path)

    def browse_backup(self):
        """Выбор папки для бэкапов"""
        dir_path = filedialog.askdirectory()
        if dir_path:
            self.backup_root.set(dir_path)

    def create_backup(self):
        """Основная логика копирования"""
        source = self.source_dir.get()
        backup_root = self.backup_root.get()

        if not source or not backup_root:
            messagebox.showerror("Ошибка", "Выберите обе папки!")
            return

        today = datetime.now().strftime("%Y-%m-%d")
        backup_folder = os.path.join(backup_root, f"backup_{today}")
        zip_filename = os.path.join(backup_folder, f"backup_{today}.zip")

        try:
            os.makedirs(backup_folder, exist_ok=True)

            self.progress.start()
            
            # Создание ZIP-архив
            with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, dirs, files in os.walk(source):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, source)
                        zipf.write(file_path, arcname)
            
            self.progress.stop()
            
            self.status_label.config(text=f"✅  Архив создан: {zip_filename}", foreground="green")
        except Exception as e:
            self.progress.stop()
            self.status_label.config(text=f"❌ Ошибка: {e}", foreground="red")
            messagebox.showerror("Ошибка", str(e))
    
    # Фильр
    def should_include(self, file_path):
        exclude_extensions = [".tmp", ".log"]
        return not any(file_path.endswith(ext) for ext in exclude_extensions)
