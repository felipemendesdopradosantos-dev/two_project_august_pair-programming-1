'''
'''
import tkinter as tk
from datetime import datetime
from tkinter import messagebox, ttk


class BancoGUI:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Simulador Bancário")
        self.root.geometry("450x400")
        self.root.resizable(False, False)


        self.titular = "Usuário"
        self.saldo = 0.0
        self.extrato = []

        
        self.modo_escuro = False

        
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self._criar_interface()
        self._aplicar_tema()

    def _criar_interface(self):
        
        self.frame_header = ttk.Frame(self.root, padding=10)
        self.frame_header.pack(fill="x")

        self.lbl_titulo = ttk.Label(
            self.frame_header, text="BANCO DIGITAL", font=("Helvetica", 16, "bold")
        )
        self.lbl_titulo.pack(side="left", padx=5)

        self.btn_tema = ttk.Button(
            self.frame_header, text="🌙 Modo Escuro", command=self.alternar_tema
        )
        self.btn_tema.pack(side="right", padx=5)

        
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

    
        self.tab_inicio = ttk.Frame(self.notebook, padding=15)
        self.notebook.add(self.tab_inicio, text=" Inicio ")

  
        self.tab_extrato = ttk.Frame(self.notebook, padding=15)
        self.notebook.add(self.tab_extrato, text=" Extrato ")

        self._montar_aba_inicio()
        self._montar_aba_extrato()

    def _montar_aba_inicio(self):
        # Exibição do Saldo
        self.lbl_saldo_titulo = ttk.Label(
            self.tab_inicio, text="Saldo Disponível", font=("Helvetica", 11)
        )
        self.lbl_saldo_titulo.pack(pady=(10, 0))

        self.lbl_saldo = ttk.Label(
            self.tab_inicio,
            text="R$ 0.00",
            font=("Helvetica", 22, "bold"),
            foreground="#2e7d32",
        )
        self.lbl_saldo.pack(pady=(0, 20))

  
        self.frame_acoes = ttk.LabelFrame(
            self.tab_inicio, text=" Realizar Operação ", padding=15
        )
        self.frame_acoes.pack(fill="x", pady=10)

        ttk.Label(
            self.frame_acoes, text="Valor (R$):", font=("Helvetica", 10)
        ).grid(row=0, column=0, sticky="w", pady=5)

        self.ent_valor = ttk.Entry(self.frame_acoes, font=("Helvetica", 11))
        self.ent_valor.grid(
            row=0, column=1, columnspan=2, sticky="ew", pady=5, padx=(10, 0)
        )

        btn_depositar = ttk.Button(
            self.frame_acoes, text="Depositar", command=self.depositar
        )
        btn_depositar.grid(row=1, column=1, pady=15, padx=5, sticky="ew")

        btn_sacar = ttk.Button(
            self.frame_acoes, text="Sacar", command=self.sacar
        )
        btn_sacar.grid(row=1, column=2, pady=15, padx=5, sticky="ew")

        self.frame_acoes.columnconfigure(1, weight=1)
        self.frame_acoes.columnconfigure(2, weight=1)

    def _montar_aba_extrato(self):
        lbl_extrato_titulo = ttk.Label(
            self.tab_extrato,
            text="Histórico de Movimentações",
            font=("Helvetica", 12, "bold"),
        )
        lbl_extrato_titulo.pack(anchor="w", pady=(0, 10))

    
        frame_lista = ttk.Frame(self.tab_extrato)
        frame_lista.pack(fill="both", expand=True)

        self.lst_extrato = tk.Listbox(
            frame_lista, font=("Consolas", 10), bd=0, highlightthickness=1
        )
        self.lst_extrato.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(
            frame_lista, orient="vertical", command=self.lst_extrato.yview
        )
        scrollbar.pack(side="right", fill="y")
        self.lst_extrato.config(yscrollcommand=scrollbar.set)

    def alternar_tema(self):
        self.modo_escuro = not self.modo_escuro
        self.btn_tema.config(
            text="☀️ Modo Claro" if self.modo_escuro else "🌙 Modo Escuro"
        )
        self._aplicar_tema()

    def _aplicar_tema(self):
        if self.modo_escuro:
            bg_general = "#1e1e1e"
            bg_panel = "#252526"
            fg_text = "#ffffff"
            entry_bg = "#3c3c3c"
            entry_fg = "#ffffff"
            border_color = "#474747"
        else:
            bg_general = "#f4f5f9"
            bg_panel = "#ffffff"
            fg_text = "#000000"
            entry_bg = "#ffffff"
            entry_fg = "#000000"
            border_color = "#dcdcdc"

        self.root.configure(bg=bg_general)

    
        self.style.configure(".", background=bg_general, foreground=fg_text)
        self.style.configure("TFrame", background=bg_general)
        self.style.configure("TLabelframe", background=bg_panel)
        self.style.configure(
            "TLabelframe.Label",
            background=bg_panel,
            foreground=fg_text,
            font=("Helvetica", 10, "bold"),
        )
        self.style.configure("TLabel", background=bg_general, foreground=fg_text)
        self.style.configure(
            "TButton", padding=6, relief="flat", background=border_color
        )
        self.style.configure("TNotebook", background=bg_general)
        self.style.configure(
            "TNotebook.Tab", background=border_color, foreground=fg_text, padding=[10, 5]
        )
        self.style.map(
            "TNotebook.Tab",
            background=[("selected", bg_panel)],
            foreground=[("selected", fg_text)],
        )


        self.tab_inicio.configure(style="TFrame")
        self.tab_extrato.configure(style="TFrame")
        self.lbl_saldo_titulo.configure(background=bg_general)

        self.lst_extrato.configure(
            bg=entry_bg,
            fg=entry_fg,
            selectbackground="#007acc",
            selectforeground="#ffffff",
            highlightbackground=border_color,
        )

    def _obter_valor_valido(self) -> float | None:
        texto = self.ent_valor.get().strip().replace(",", ".")
        try:
            valor = float(texto)
            if valor <= 0:
                messagebox.showwarning(
                    "Aviso", "Digite um valor maior que zero."
                )
                return None
            return valor
        except ValueError:
            messagebox.showerror(
                "Erro", "Por favor, digite um número válido."
            )
            return None

    def depositar(self):
        valor = self._obter_valor_valido()
        if valor is not None:
            self.saldo += valor
            data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")
            mensagem = f"[{data_hora}] DEPÓSITO:  +R$ {valor:10.2f}"
            self.extrato.append(mensagem)
            self._atualizar_interface()
            messagebox.showinfo(
                "Sucesso", f"Depósito de R$ {valor:.2f} realizado!"
            )

    def sacar(self):
        valor = self._obter_valor_valido()
        if valor is not None:
            if valor > self.saldo:
                messagebox.showerror(
                    "Erro", f"Saldo insuficiente! Saldo atual: R$ {self.saldo:.2f}"
                )
            else:
                self.saldo -= valor
                data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")
                mensagem = f"[{data_hora}] SAQUE:     -R$ {valor:10.2f}"
                self.extrato.append(mensagem)
                self._atualizar_interface()
                messagebox.showinfo(
                    "Sucesso", f"Saque de R$ {valor:.2f} realizado!"
                )

    def _atualizar_interface(self):
        self.lbl_saldo.config(text=f"R$ {self.saldo:.2f}")
        self.ent_valor.delete(0, tk.END)

        self.lst_extrato.delete(0, tk.END)
        for item in self.extrato:
            self.lst_extrato.insert(tk.END, item)


if __name__ == "__main__":
    root = tk.Tk()
    app = BancoGUI(root)
    root.mainloop()
    
    