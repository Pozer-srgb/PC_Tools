import sys
import os
from tkinter import ttk
import customtkinter as ctk
import importlib
from pathlib import Path

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        # Настройки окна
        self.title("PC Tools v1.0.2")
        self.geometry("600x400")
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        # Заголовок
        self.title_label = ctk.CTkLabel(self, text="PC Tools", font=("Arial", 24))
        self.title_label.pack(pady=20)

        # Разделитель
        self.separator = ttk.Separator(self, orient="horizontal")
        self.separator.pack(fill="x", padx=20, pady=10)

        # Загрузка модулей
        self.load_tools()

    def load_tools(self):
        modules = []
        # Ищем все .py файлы в папке tools (кроме __init__.py)
        for file in Path("tools").glob("*.py"):
            if file.name == "__init__.py":
                continue
            module_name = file.stem
            try:
                module = importlib.import_module(f"tools.{module_name}")
                if hasattr(module, "setup_tool"):
                    modules.append(module.setup_tool)
                else:
                    print(f"Ошибка: В модуле {module_name} нет функции setup_tool")
            except Exception as e:
                print(f"Ошибка загрузки {module_name}: {str(e)}")

        # Создаём кнопки для каждого модуля
        for tool in modules:
            button = tool(self)
            button.pack(pady=10)

if __name__ == "__main__":
    app = App()
    app.mainloop()