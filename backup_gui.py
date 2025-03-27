import os
import shutil
from datetime import datetime
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

class BackupApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Резервное копирование")

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
        backup_root = self.backup_roo.get()

        if not source or not backup_root:
            messagebox.showerror("Ошибка", "Выберите обе папки!")
            return

        today = datetime.now().strftime("%D-%M-%Y")
        backup_folder = os.path.join(backup_root, f"backup_{today}")

        try:
            os.makedirs(backup_folder, exist_ok=True)
            shutil.copytree(
                source, 
                os.path.join(backup_folder. os.path.basename(source)),
                dirs_exist_ok=True    
            )
            self.status_label.config(text=f"✅ Успешно сохранено в:\n{backup_folder}", foregroud="green")
        except Exception as e:
            self.status_label.config(text=f"❌ Ошибка: {e}", foreground="red")
            messagebox.showerror("Ошибка", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = BackupApp(root)
    root.mainloop()