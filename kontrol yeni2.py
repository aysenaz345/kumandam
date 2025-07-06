import tkinter as tk
import pyautogui

def mouse_hareket(x, y):
    pyautogui.moveRel(x, y)

def tikla():
    pyautogui.click()

def klavye_yaz(karakter):
    pyautogui.typewrite(karakter)

def klavye_tus(tus):
    pyautogui.press(tus)  # Özel tuşlar için (örneğin backspace, space)

# Pencere oluştur
pencere = tk.Tk()
pencere.title("Ayşo'nun Uzaktan Kumandası")
pencere.geometry("320x450")

# === 🖱️ Mouse Kontrolleri ===
mouse_frame = tk.Frame(pencere)
mouse_frame.pack(pady=10)

tk.Label(mouse_frame, text="🖱️ Mouse Kontrolleri").pack()

tk.Button(mouse_frame, text="↑", width=10, command=lambda: mouse_hareket(0, -20)).pack()
mouse_yon = tk.Frame(mouse_frame)
mouse_yon.pack()
tk.Button(mouse_yon, text="←", width=5, command=lambda: mouse_hareket(-20, 0)).pack(side="left")
tk.Button(mouse_yon, text="TIK", width=5, command=tikla).pack(side="left")
tk.Button(mouse_yon, text="→", width=5, command=lambda: mouse_hareket(20, 0)).pack(side="left")
tk.Button(mouse_frame, text="↓", width=10, command=lambda: mouse_hareket(0, 20)).pack()

# === ⌨️ Klavye Tuşları ===
klavye_frame = tk.Frame(pencere)
klavye_frame.pack(pady=20)

tk.Label(klavye_frame, text="⌨️ Klavye Tuşları").pack()

harfler = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I",
    "İ", "J", "K", "L", "M", "N", "O", "Ö", "P", "R",
    "S", "Ş", "T", "U", "Ü", "V", "Y", "Z"
]


harf_frame = tk.Frame(klavye_frame)
harf_frame.pack()

for harf in harfler:
    tk.Button(harf_frame, text=harf, width=3,
              command=lambda h=harf: klavye_yaz(h.lower())).pack(side="left")

# === SPACE ve BACKSPACE ===
ozel_frame = tk.Frame(klavye_frame)
ozel_frame.pack(pady=10)

tk.Button(ozel_frame, text="␣ Space", width=10, command=lambda: klavye_tus("space")).pack(side="left", padx=5)
tk.Button(ozel_frame, text="⌫ Sil", width=10, command=lambda: klavye_tus("backspace")).pack(side="left", padx=5)
# GÖRÜNTÜ (ekran görüntüsü alan)
goruntu_frame = tk.Frame(pencere, bg="white")
goruntu_frame.pack(pady=10)
tk.Label(goruntu_frame, text="🖼 Bilgisayar Görüntüsü (3 saniyede bir güncellenir)", bg="white").pack()
ekran_label = tk.Label(goruntu_frame, bg="white")
ekran_label.pack()

def ekran_guncelle():
    import PIL.ImageGrab
    from PIL import ImageTk
    screenshot = PIL.ImageGrab.grab()
    screenshot = screenshot.resize((300, 180))
    img = ImageTk.PhotoImage(screenshot)
    ekran_label.img = img  # referans tut
    ekran_label.config(image=img)
    pencere.after(3000, ekran_guncelle)

ekran_guncelle()

# SES kontrol fonksiyonları
def sesi_azalt():
    pyautogui.press("volumedown")

def sesi_kapat():
    pyautogui.press("volumemute")

def sesi_arttir():
    pyautogui.press("volumeup")

# SES
ses_frame = tk.Frame(pencere, bg="white")
ses_frame.pack(pady=10)
tk.Label(ses_frame, text="🔊 Ses Kontrolleri", font=("Arial", 12, "bold"), bg="white").pack()
tk.Button(ses_frame, text="🔈-", width=5, command=sesi_azalt).pack(side="left", padx=5)
tk.Button(ses_frame, text="🔇", width=5, command=sesi_kapat).pack(side="left", padx=5)
tk.Button(ses_frame, text="🔊+", width=5, command=sesi_arttir).pack(side="left", padx=5)

# Uygulamayı çalıştır
pencere.mainloop()
