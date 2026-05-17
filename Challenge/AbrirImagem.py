import tkinter as tk
from tkinter import messagebox


# Função que será chamada quando o Item 1 for clicado
def abrir_imagem():
    try:
        # Cria uma nova janela (Janela Pop-up)
        janela_imagem = tk.Toplevel(root)
        janela_imagem.title("Imagem do Item 1")
        
        # Carrega a imagem (substitua pelo caminho da sua imagem)
        # Exemplo: "foto.jpg" ou "C:/Users/Nome/Pictures/imagem.png"
        img = Image.open("./SoulUp_post.jpeg") 
        
        # Converte a imagem para o formato que o Tkinter entende
        img_tk = ImageTk.PhotoImage(img)
        
        # Cria um Label para colocar a imagem dentro
        label_img = tk.Label(janela_imagem, image=img_tk)
        label_img.image = img_tk # Mantém uma referência para a imagem não sumir da memória
        label_img.pack(padx=10, pady=10)
        
    except FileNotFoundError:
        messagebox.showerror("Erro", "O arquivo de imagem não foi encontrado. Verifique o caminho!")