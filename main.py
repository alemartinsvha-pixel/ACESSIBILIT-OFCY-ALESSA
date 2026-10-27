import tkinter as tk
from tkinter import ttk, filedialog, messagebox

class EstudeComAlessa:
    def __init__(self, root):
        self.root = root
        root.title("Estude com Alessa - Todo merito e de Deus")
        root.geometry("900x650")
        style = ttk.Style()
        style.configure("TButton", font=("Arial", 12), padding=8)
        topo = tk.Frame(root, bg="#6A1B9A", height=70)
        topo.pack(fill="x")
        tk.Label(topo, text="Estude com Alessa", fg="white", bg="#6A1B9A", font=("Arial", 20, "bold")).pack(pady=5)
        tk.Label(topo, text="Pacote de escritorio acessivel, brasileiro e com proposito", fg="#E1BEE7", bg="#6A1B9A", font=("Arial", 11)).pack()
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)
        self.criar_aba_texto()
        self.criar_aba_planilha()
        self.criar_aba_slides()
        rodape = tk.Label(root, text="Todo merito e de Deus - Criado por Alessandra com Alessa TTS", bg="#F3E5F5", fg="#4A148C", font=("Arial", 9), pady=6)
        rodape.pack(fill="x", side="bottom")

    def criar_aba_texto(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="  Editor de Texto  ")
        barra = ttk.Frame(frame)
        barra.pack(fill="x", pady=5)
        ttk.Button(barra, text="Salvar (Ctrl+S)", command=self.salvar_texto).pack(side="left", padx=5)
        self.texto = tk.Text(frame, font=("Arial", 14), wrap="word", undo=True, padx=10, pady=10)
        self.texto.pack(fill="both", expand=True, padx=5, pady=5)
        self.texto.insert("1.0", "Digite seu texto aqui... Deus te capacita!")

    def criar_aba_planilha(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="  Planilha  ")
        cols = ["", "A", "B", "C", "D", "E", "F"]
        for c, nome in enumerate(cols):
            ttk.Label(frame, text=nome, font=("Arial", 11, "bold"), width=12, borderwidth=1, relief="solid").grid(row=0, column=c, sticky="nsew")
        for l in range(1, 11):
            ttk.Label(frame, text=str(l), font=("Arial", 11, "bold"), width=4, borderwidth=1, relief="solid").grid(row=l, column=0, sticky="nsew")
            for c in range(1, 7):
                e = ttk.Entry(frame, width=12, font=("Arial", 11))
                e.grid(row=l, column=c, sticky="nsew", padx=1, pady=1)

    def criar_aba_slides(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="  Slides  ")
        self.slide_text = tk.Text(frame, font=("Arial", 16), wrap="word", padx=15, pady=15)
        self.slide_text.pack(fill="both", expand=True, padx=10, pady=10)
        self.slide_text.insert("1.0", "Titulo do Slide\n\nConteudo simples e acessivel!")

    def salvar_texto(self):
        path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Texto", "*.txt")])
        if path:
            with open(path, "w", encoding="utf-8") as f:
                f.write(self.texto.get("1.0", tk.END))
            messagebox.showinfo("Salvo", f"Salvo em {path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = EstudeComAlessa(root)
    root.mainloop()
