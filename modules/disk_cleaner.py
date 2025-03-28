class DiskCleaner:
    def __init__(self, parent):
        self.parent = parent
        self.create_widgets()

    def create_widgetes(self):
        label = ttk.Label(self.parent, text="Очистка диска...")
        label.pack()