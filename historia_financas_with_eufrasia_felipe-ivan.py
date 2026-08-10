import io
import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk

# ----------------------
# Paleta de Cores
# ----------------------
COLOR_AZUL_ESC = "#004d6e"  # Fundo da tela principal
COLOR_AZUL_MED = "#0081ab"  # Bordas e detalhes
COLOR_AZUL_CLA = "#00b1cd"  # Destaque de textos
COLOR_AMARELO  = "#edce01"  # Destaque / Botões de Curiosidade


# ----------------------
# Funções Específicas
# ----------------------
def mostrar_fato(detalhe):
    messagebox.showinfo("Curiosidade - Eufrásia Teixeira Leite", detalhe)

def mostrar_heranca_e_negocios():
    texto = (
        "Detalhes Financeiros:\n\n"
        "• 23 Anos: Idade em que assumiu a gestão e independência total de sua imensa fortuna.\n"
        "• 7 Países: Países onde diversificou seus investimentos globais.\n"
        "• Mais de 8 Moedas Diferentes: Ativos operados em múltiplos câmbios e moedas internacionais para proteção patrimonial."
    )
    messagebox.showinfo("Herança", texto)

def mostrar_legado_e_romance():
    texto = (
        "Curiosidade - Legado e Relacionamento:\n\n"
        "Eufrásia manteve um longo relacionamento com o diplomata e abolicionista Joaquim Nabuco. "
        "No entanto, o casamento nunca aconteceu porque ela impôs uma condição estrita: "
        "queria se casar em Paris, e não no Rio de Janeiro, rompendo com as convenções sociais impostas às mulheres da época."
    )
    messagebox.showinfo("Curiosidades", texto)


# ----------------------
# Janela Principal
# ----------------------
janela = tk.Tk()
janela.title("História: Eufrásia Teixeira Leite")
janela.geometry("520x740")
janela.configure(bg=COLOR_AZUL_ESC)


# ----------------------
# Título e Subtítulo
# ----------------------
lbl_titulo = tk.Label(
    janela,
    text="Eufrásia Teixeira Leite",
    font=("Times New Roman", 22, "bold"),
    bg=COLOR_AZUL_ESC,
    fg="white",
)
lbl_titulo.pack(pady=7)

lbl_subtitulo = tk.Label(
    janela,
    text="A primeira investidora global do Brasil",
    font=("Arial", 10, "italic"),
    bg=COLOR_AZUL_ESC,
    fg=COLOR_AMARELO,
)
lbl_subtitulo.pack(pady=2)


# ----------------------
# Carregando Imagem da Internet
# ----------------------
url_imagem = "https://upload.wikimedia.org/wikipedia/commons/4/40/Eufr%C3%A1sia_Teixeira_Leite_aos_30_anos_%282%29.jpg"
foto_eufrasia = None

try:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    resposta = requests.get(url_imagem, headers=headers, timeout=5)
    resposta.raise_for_status()

    dados_imagem = resposta.content
    imagem_pil = Image.open(io.BytesIO(dados_imagem))
    imagem_pil = imagem_pil.resize((110, 140), Image.Resampling.LANCZOS)

    foto_eufrasia = ImageTk.PhotoImage(imagem_pil)

    lbl_imagem = tk.Label(janela, image=foto_eufrasia, bg=COLOR_AZUL_ESC)
    lbl_imagem.image = foto_eufrasia
    lbl_imagem.pack(pady=5)

except Exception as erro:
    print(f"Erro ao carregar imagem: {erro}")
    lbl_erro = tk.Label(
        janela,
        text="[Foto de Eufrásia Teixeira Leite - Indisponível]",
        font=("Arial", 9, "italic"),
        fg="gray",
        bg=COLOR_AZUL_ESC,
    )
    lbl_erro.pack(pady=5)


# ----------------------
# Dados da Linha do Tempo
# ----------------------
eventos = {
    "1850 - Nascimento": "Nasceu em Vassouras (RJ), no auge do ciclo do café.",
    "1872 - Herança & Europa": "Após perder os pais, mudou-se para Paris e assumiu a gestão da fortuna da família.",
    "1873-1930 - Carteira Global": "Investiu em títulos, ações e ferrovias em múltiplos países e moedas diferentes.",
    "1930 - Legado": "Faleceu deixando sua imensa fortuna para causas sociais, beneficentes e educacionais no Brasil.",
}

# Criação dos Botões da Linha do Tempo
for data, detalhe in eventos.items():
    btn = tk.Button(
        janela,
        text=data,
        font=("Arial", 10, "bold"),
        bg=COLOR_AZUL_MED,
        fg="white",
        relief="flat",
        command=lambda d=detalhe: mostrar_fato(d),
    )
    btn.pack(fill="x", padx=40, pady=4)


# ----------------------
# Botões Especiais com Nomes Curtos e Azul Padrão
# ----------------------
btn_heranca = tk.Button(
    janela,
    text="Herança",
    font=("Arial", 10, "bold"),
    bg=COLOR_AZUL_MED,
    fg="white",
    relief="flat",
    command=mostrar_heranca_e_negocios,
)
btn_heranca.pack(fill="x", padx=40, pady=4)

btn_legado = tk.Button(
    janela,
    text="Curiosidades",
    font=("Arial", 10, "bold"),
    bg=COLOR_AZUL_MED,
    fg="white",
    relief="flat",
    command=mostrar_legado_e_romance,
)
btn_legado.pack(fill="x", padx=40, pady=4)


# ----------------------
# Loop Principal
# ----------------------
janela.mainloop()
