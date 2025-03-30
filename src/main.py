import customtkinter as ctk
from tools.task_manager import setup_tool as setup_taskmgr
from tools.system_info import setup_tool as setup_sysinfo
from tools.trash_cleaner import setup_tool as setup_trash_cleaner

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        # Настройки окна
        self.title("PC Tools v1.0")
        self.geometry("600x400")
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        # Загрузка модулей
        self.load_tools()

    def load_tools(self):
        # Список всех модулей
        tools = [
            setup_taskmgr,
            setup_sysinfo,
            setup_trash_cleaner
        ]

        # Создаём кнопки для каждого модуля
        for tool in tools:
            button = tool(self)
            button.pack(pady=10)

if __name__ == "__main__":
    app = App()
    app.mainloop()