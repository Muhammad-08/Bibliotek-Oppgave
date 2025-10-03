import tkinter as tk
from tkinter import messagebox, simpledialog
import json

FIL = "bibliotek.json"

try:
    with open(FIL, "r", encoding="utf-8") as f:
        bibliotek = json.load(f)
except:
    bibliotek = []

def lagre():
    with open(FIL, "w", encoding="utf-8") as f:
        json.dump(bibliotek, f, ensure_ascii=False, indent=2)

def vis_bøker():
    liste.delete(0, tk.END)
    if not bibliotek:
        liste.insert(tk.END, "📚 Ingen bøker i biblioteket")
    for b in bibliotek:
        liste.insert(tk.END, f"{b['tittel']} - {b['forfatter']} ({b['status']})")

def legg_til():
    tittel = simpledialog.askstring("Ny bok", "Tittel:")
    forfatter = simpledialog.askstring("Ny bok", "Forfatter:")
    if tittel and forfatter:
        bibliotek.append({"tittel": tittel, "forfatter": forfatter, "status": "ledig"})
        lagre()
        vis_bøker()

def lån():
    søk = simpledialog.askstring("Lån bok", "Søk tittel:")
    for b in bibliotek:
        if søk and søk.lower() in b['tittel'].lower():
            if b['status'] == "ledig":
                b['status'] = "utlånt"
                lagre(); vis_bøker()
                messagebox.showinfo("OK", f"✅ Du lånte {b['tittel']}")
                return
            else:
                messagebox.showwarning("Opptatt", "⚠️ Boka er allerede utlånt")
                return
    messagebox.showerror("Feil", "❌ Fant ikke boka")

def lever():
    søk = simpledialog.askstring("Lever bok", "Søk tittel:")
    for b in bibliotek:
        if søk and søk.lower() in b['tittel'].lower():
            if b['status'] == "utlånt":
                b['status'] = "ledig"
                lagre(); vis_bøker()
                messagebox.showinfo("OK", f"🙌 Du leverte {b['tittel']}")
                return
    messagebox.showerror("Feil", "❌ Fant ikke boka")

root = tk.Tk()
root.title("📚 Mitt Bibliotek")
root.geometry("500x400")
root.configure(bg="#ecf0f1")

overskrift = tk.Label(root, text="--- Velkommen til biblioteket ---", 
                      font=("Arial", 14, "bold"), bg="#ecf0f1", fg="#2c3e50")
overskrift.pack(pady=10)

liste = tk.Listbox(root, width=55, height=12, font=("Arial", 11), bg="white", fg="black")
liste.pack(pady=10)

knapper = tk.Frame(root, bg="#ecf0f1")
knapper.pack(pady=15)

# Litt stiligere knapper med "flat" stil + padding + avrundede kanter
style = {
    "width": 12,
    "font": ("Arial", 10, "bold"),
    "relief": "flat",
    "bd": 0,
    "pady": 6
}

tk.Button(knapper, text="➕ Legg til", command=legg_til, bg="#27ae60", fg="white", **style).grid(row=0, column=0, padx=8, pady=5)
tk.Button(knapper, text="📖 Lån", command=lån, bg="#2980b9", fg="white", **style).grid(row=0, column=1, padx=8, pady=5)
tk.Button(knapper, text="↩️ Lever", command=lever, bg="#f39c12", fg="white", **style).grid(row=1, column=0, padx=8, pady=5)
tk.Button(knapper, text="❌ Avslutt", command=root.quit, bg="#c0392b", fg="white", **style).grid(row=1, column=1, padx=8, pady=5)

vis_bøker()
root.mainloop()
