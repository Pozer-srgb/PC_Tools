import tkinter as tk
from tkinter import ttk

class BaseModule:
    def __init__(self, parent):
        self.parent = parent
        self.root = ttk.Frame(parent)
        self.root.pack(fill="both", expand=True)

    def create_widgets(self):
        raise NotImplementedError()