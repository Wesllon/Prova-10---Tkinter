# Usando seus conhecimentos aprendidos em sala, realize uma interface de login utilizando a biblioteca Tkinter em Python. O objetivo é permitir que o usuário faça login somente se a senha tiver mais de 6 dígitos e se o e-mail contiver o caractere "@", ou seja, realizar uma tela de login com restrições de e-mail e senha.
from tkinter import *

# Função para realizar o login
def fazer_login_certo():
    # Obtém o email e a senha inseridos pelo usuário
    email = dados_login.get()
    senha = dados_senha.get()
    
    # Verifica se a senha tem mais de 6 caracteres e se o email contém '@'
    if len(senha) <= 6 or "@" not in email:
        # Define a mensagem de erro
        msg.set("Senha deve ter mais de 6 caracteres e o email deve conter o símbolo '@'.")
        # Configura a cor e a fonte da mensagem de erro
        msg_label.config(fg='red', font='Georgia')
    else:
        # Define a mensagem de sucesso
        msg.set("Login realizado com sucesso!")
        # Configura a cor e a fonte da mensagem de sucesso
        msg_label.config(fg='green', font='Georgia')

# Cria a janela principal
root = Tk()
root.title('Tela de Login')
root.geometry('600x250')

# Variável para armazenar a mensagem de erro/sucesso
msg = StringVar()

# Configura o fundo da janela
root.config(background='black')

# Label e Entry para o email
txt_login = Label(root, text='Email:')
txt_login.grid(row=0, column=0, padx=5, pady=5)
dados_login = Entry(root)
dados_login.grid(row=0, column=1, padx=5, pady=5)

# Label e Entry para a senha
txt_senha = Label(root, text='Senha:')
txt_senha.grid(row=1, column=0, padx=5, pady=5)
dados_senha = Entry(root, show='*')
dados_senha.grid(row=1, column=1, padx=5, pady=5)

# Botão para realizar o login
btn = Button(root, text='Entrar', command=fazer_login_certo)
btn.grid(row=2, column=1, padx=5, pady=5)

# Label para exibir a mensagem de erro/sucesso
msg_label = Label(root, textvariable=msg, bg='black')
msg_label.grid(row=3, columnspan=2, padx=5, pady=5)

# Label para exibir o autor
msg_autor = Label(root, text='Wes ©2024', fg='white', bg='black')
msg_autor.grid(pady=45)

# Inicia o loop principal da aplicação
root.mainloop()


