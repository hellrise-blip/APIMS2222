import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import sys

class SmartHomeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Умный дом")
        self.root.geometry("800x500")

        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.dirname(os.path.abspath(__file__))

        try:
            icon_path = os.path.join(base_path, "smart_home_icon.ico")
            self.root.iconbitmap(icon_path)
        except:
            pass

        self.devices = {
            "Эл.замок": {
                "image_path": os.path.join(base_path, "images", "zamok.png"),
                "specs_path": os.path.join(base_path, "specs", "zamok1.png"),
                "button_icon": os.path.join(base_path, "zamok2.png"),
                "menu_icon": os.path.join(base_path, "menu_icons", "lock_menu.png"),
                "status_icon": os.path.join(base_path, "status_icons", "lock_status.png"),
                "functions": "• Дистанционное открытие/закрытие\n• Временные коды доступа\n• Интеграция с системой безопасности\n• Уведомления о событиях",
                "image_text": "Умный электронный замок с удаленным управлением и функцией временного доступа для гостей",
                "specs_text": "Технические характеристики:\n• Рабочее напряжение: 12В\n• Ток потребления: 500мА\n• Радиус действия: 50м\n• Защита от взлома: IP65\n• Срок службы: 5 лет"
            },
            "Умная лампочка": {
                "image_path": os.path.join(base_path, "images", "lamp.png"),
                "specs_path": os.path.join(base_path, "specs", "lamp1.png"),
                "button_icon": os.path.join(base_path, "lamp2.png"),
                "menu_icon": os.path.join(base_path, "menu_icons", "lamp_menu.png"),
                "status_icon": os.path.join(base_path, "status_icons", "lamp_status.png"),
                "functions": "• Настройка яркости\n• Изменение цвета\n• Расписание работы\n• Голосовое управление",
                "image_text": "RGB LED лампа с регулировкой цвета и яркости, поддержка 16 миллионов цветов",
                "specs_text": "Технические характеристики:\n• Мощность: 10W\n• Световой поток: 800 люмен\n• Цветовая температура: 1800-6500K\n• Совместимость: Wi-Fi 2.4GHz\n• Срок службы: 25,000 часов"
            },
            "Система отопления": {
                "image_path": os.path.join(base_path, "images", "heat.png"),
                "specs_path": os.path.join(base_path, "specs", "heat1.png"),
                "button_icon": os.path.join(base_path, "otopl2.png"),
                "menu_icon": os.path.join(base_path, "menu_icons", "heat_menu.png"),
                "status_icon": os.path.join(base_path, "status_icons", "heat_status.png"),
                "functions": "• Программирование температуры\n• Удаленное управление\n• Экономичный режим\n• Интеграция с погодой",
                "image_text": "Умный термостат с функцией обучения и автоматической оптимизацией температуры",
                "specs_text": "Технические характеристики:\n• Температурный диапазон: 5°C - 35°C\n• Точность: ±0.5°C\n• Питание: 220В или 2xAA\n• Протоколы: Wi-Fi, Bluetooth\n• Рабочая влажность: 20-80%"
            },
            "Автополив растений": {
                "image_path": os.path.join(base_path, "images", "poliv.png"),
                "specs_path": os.path.join(base_path, "specs", "poliv1.png"),
                "button_icon": os.path.join(base_path, "poliv2.png"),
                "menu_icon": os.path.join(base_path, "menu_icons", "plant_menu.png"),
                "status_icon": os.path.join(base_path, "status_icons", "plant_status.png"),
                "functions": "• Автоматический полив\n• Контроль влажности почвы\n• Ручной полив\n• Настройка объема полива",
                "image_text": "Система автоматического полива с датчиками влажности и управлением через приложение",
                "specs_text": "Технические характеристики:\n• Объем бака: 5 литров\n• Рабочее давление: 0.8-1.2 бар\n• Расход воды: 0.5-2 л/час\n• Датчик влажности: 0-100%\n• Автономность: 30 дней"
            }
        }

        self.device_icons = {}
        self.button_photos = {}
        self.load_device_icons(base_path)

        self.current_device = None
        self.current_content_type = None
        self.setup_ui()

    def load_device_icons(self, base_path):
        for device_name, paths in self.devices.items():
            try:
                if os.path.exists(paths["button_icon"]):
                    img = Image.open(paths["button_icon"])
                    img = img.resize((32, 32), Image.Resampling.LANCZOS)
                    photo = ImageTk.PhotoImage(img)
                    self.button_photos[device_name] = photo
            except:
                pass

    def setup_ui(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Файл", menu=file_menu)
        file_menu.add_command(label="Открыть", command=lambda: messagebox.showinfo("Открыть", "Открытие файла"))
        file_menu.add_command(label="Сохранить", command=lambda: messagebox.showinfo("Сохранить", "Сохранение файла"))
        file_menu.add_separator()
        file_menu.add_command(label="Закрыть", command=self.root.quit)

        devices_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Устройства", menu=devices_menu)
        for device in self.devices:
            device_menu = tk.Menu(devices_menu, tearoff=0)
            devices_menu.add_cascade(label=device, menu=device_menu)
            device_menu.add_command(label="Изображение", command=lambda d=device: self.show_content(d, "image"))
            device_menu.add_command(label="Характеристики", command=lambda d=device: self.show_content(d, "specs"))
            device_menu.add_command(label="Функции", command=lambda d=device: self.show_content(d, "functions"))

        instruction_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Инструкция", menu=instruction_menu)
        for device in self.devices:
            instruction_menu.add_command(label=device, command=lambda d=device: self.show_instruction(d))

        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Помощь", menu=help_menu)
        help_menu.add_command(label="О программе", command=lambda: messagebox.showinfo("Помощь", "Программа 'Умный дом'\nВерсия 1.0"))

        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        left_frame = tk.Frame(main_frame, width=180)
        left_frame.pack(side=tk.LEFT, fill=tk.Y)
        left_frame.pack_propagate(False)

        self.device_buttons = {}
        for device in self.devices:
            btn_frame = tk.Frame(left_frame, width=160, height=80)
            btn_frame.pack(pady=5)
            btn_frame.pack_propagate(False)

            if device in self.button_photos:
                icon_label = tk.Label(btn_frame, image=self.button_photos[device])
                icon_label.pack(pady=(5, 0))

                btn_text = tk.Label(btn_frame, text=device, font=("Arial", 10))
                btn_text.pack(pady=(2, 5))

                btn = tk.Button(btn_frame, text="", width=160, height=80,
                                command=lambda d=device: self.select_device(d))
                btn.place(x=0, y=0, width=160, height=80)
                btn.config(relief="flat", borderwidth=0)
            else:
                btn = tk.Button(btn_frame, text=device, width=20, height=2,
                                command=lambda d=device: self.select_device(d))
                btn.pack()

            tip = tk.Toplevel(self.root)
            tip.wm_overrideredirect(True)
            tip.withdraw()
            label = tk.Label(tip, text=f"Выбрать {device.lower()}", bg="lightyellow", relief="solid")

            def show_tip(event, t=tip, l=label):
                t.deiconify()
                t.wm_geometry(f"+{event.x_root+10}+{event.y_root+10}")
                l.pack()

            def hide_tip(event, t=tip):
                t.withdraw()

            if device in self.button_photos:
                btn_frame.bind("<Enter>", show_tip)
                btn_frame.bind("<Leave>", hide_tip)
                btn.bind("<Enter>", show_tip)
                btn.bind("<Leave>", hide_tip)
            else:
                btn.bind("<Enter>", show_tip)
                btn.bind("<Leave>", hide_tip)

            self.device_buttons[device] = btn

        right_frame = tk.Frame(main_frame)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(20, 0))

        self.content_frame = tk.Frame(right_frame, bg="lightgray")
        self.content_frame.pack(fill=tk.BOTH, expand=True)

        self.content_canvas = tk.Canvas(self.content_frame, bg="lightgray")
        scrollbar = tk.Scrollbar(self.content_frame, orient="vertical", command=self.content_canvas.yview)
        self.scrollable_frame = tk.Frame(self.content_canvas, bg="lightgray")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.content_canvas.configure(scrollregion=self.content_canvas.bbox("all"))
        )

        self.content_canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.content_canvas.configure(yscrollcommand=scrollbar.set)

        self.content_canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.image_label = tk.Label(self.scrollable_frame, bg="lightgray")
        self.image_label.pack()

        self.text_label = tk.Label(self.scrollable_frame, text="Выберите устройство",
                                   font=("Arial", 12), bg="lightgray", justify=tk.LEFT, wraplength=400)
        self.text_label.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        self.control_frame = tk.Frame(right_frame)
        self.control_frame.pack(fill=tk.X, pady=(10, 0))

        self.control_buttons = {}
        button_texts = ["Изображение", "Характеристики", "Функции"]
        for text in button_texts:
            btn = tk.Button(self.control_frame, text=text, width=15, command=lambda t=text: self.on_control_button(t))
            btn.pack(side=tk.LEFT, padx=5)
            self.control_buttons[text] = btn

        self.control_frame.pack_forget()

    def select_device(self, device_name):
        for name, btn in self.device_buttons.items():
            if device_name in self.button_photos:
                parent = btn.master
                for child in parent.winfo_children():
                    if isinstance(child, tk.Button):
                        child.config(bg="SystemButtonFace")
            else:
                btn.config(bg="SystemButtonFace")

        if device_name in self.button_photos:
            parent = self.device_buttons[device_name].master
            for child in parent.winfo_children():
                if isinstance(child, tk.Button):
                    child.config(bg="lightblue")
        else:
            self.device_buttons[device_name].config(bg="lightblue")

        self.current_device = device_name

        self.control_frame.pack(fill=tk.X, pady=(10, 0))

        self.show_content(device_name, "image")

    def show_content(self, device_name, content_type):
        self.current_content_type = content_type

        self.image_label.config(image="")
        self.text_label.config(text="")

        try:
            if content_type == "image":
                path = self.devices[device_name]["image_path"]
                if os.path.exists(path):
                    img = Image.open(path)
                    img = img.resize((400, 300), Image.Resampling.LANCZOS)
                    photo = ImageTk.PhotoImage(img)
                    self.image_label.config(image=photo)
                    self.image_label.image = photo
                    self.text_label.config(text=self.devices[device_name]["image_text"], font=("Arial", 10))
                else:
                    self.text_label.config(text=f"Файл не найден:\n{path}", font=("Arial", 10))

            elif content_type == "specs":
                path = self.devices[device_name]["specs_path"]
                if os.path.exists(path):
                    img = Image.open(path)
                    img = img.resize((400, 300), Image.Resampling.LANCZOS)
                    photo = ImageTk.PhotoImage(img)
                    self.image_label.config(image=photo)
                    self.image_label.image = photo
                    self.text_label.config(text=self.devices[device_name]["specs_text"], font=("Arial", 10))
                else:
                    self.text_label.config(text=f"Файл не найден:\n{path}", font=("Arial", 10))

            elif content_type == "functions":
                self.image_label.config(image="")
                text = f"Функции устройства:\n\n{self.devices[device_name]['functions']}"
                self.text_label.config(text=text, font=("Arial", 11))

        except Exception as e:
            error_msg = f"Ошибка загрузки {content_type}:\n{str(e)}"
            self.text_label.config(text=error_msg, font=("Arial", 10))

    def on_control_button(self, button_text):
        if self.current_device:
            if button_text == "Изображение":
                self.show_content(self.current_device, "image")
            elif button_text == "Характеристики":
                self.show_content(self.current_device, "specs")
            elif button_text == "Функции":
                self.show_content(self.current_device, "functions")

    def show_instruction(self, device_name):
        instructions = {
            "Эл.замок": "Подключите к Wi-Fi, установите приложение, настройте доступ.",
            "Умная лампочка": "Вкрутите лампочку, подключите к приложению, настройте освещение.",
            "Система отопления": "Установите термостат, подключите к сети, настройте температуру.",
            "Автополив растений": "Наполните бак, установите датчики, настройте график полива."
        }
        messagebox.showinfo(f"Инструкция: {device_name}", instructions.get(device_name, "Инструкция не найдена"))

def main():
    root = tk.Tk()
    app = SmartHomeApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()