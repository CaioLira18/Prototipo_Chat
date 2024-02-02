  # Título Hashzap
  # Botão de Iniciar o chat
  # Popup
  # Bem Vindo ao hashzap
  # Escreva seu nome
  # Entrar no chat
  
# Chat
  # Lira entrou no chat
  # Mensagens do usuario

# Campo para enviar mensagem
# Botão de enviar    

import flet as ft



def main(pagina: ft.Page): # Importar a Pagina
    
    
    texto = ft.Text("Prototipo de Chat", font_family="ChaletCmprime")
    nome_usuario = ft.TextField(label="Escreva seu nome: ") # campo de texto para o usuario preencher    
    chat = ft.Column()
    
  
    def enviar_mensagem_tunel(informacoes):
        chat.controls.append(ft.Text(informacoes))
        pagina.update()

    
    
    pagina.pubsub.subscribe(enviar_mensagem_tunel)
    
    def enviar_mensagem(evento):
        texto_campo_mensagem = f"{nome_usuario.value}: {campo_mensagem.value}"
        pagina.pubsub.send_all(texto_campo_mensagem)
        campo_mensagem.value = " " # Limpando o campo
        pagina.update()
        
    campo_mensagem = ft.TextField(label="Escreva sua mensagem aqui", on_submit=enviar_mensagem) # criar o campo de enviar mensagem  
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem) # criar botao de enviar mensagem
    
    def entrar_chat(evento):
       
        popup.open = False # Tirar o popup
        pagina.remove(botao_iniciar) # Tirar o botao de "Inciar Chat"
        pagina.add(chat) # Adicionar o chat
        linha_mensagem = ft.Row([campo_mensagem, botao_enviar]) # Criar o campode enviar mensagem
       
        pagina.add(linha_mensagem) # Botão de enviar mensagem
        texto = f"{nome_usuario.value} entrou no chat"
        pagina.pubsub.send_all(texto)

        pagina.update()
        
        
    popup = ft.AlertDialog(open= False, modal=True,title=ft.Text("Hashzap"), # Qual o titulo do pop up
    content= nome_usuario, # O que vai ter no popup
    actions=[ft.ElevatedButton("Entrar", on_click=entrar_chat)]) # Botões do Popup
    
    def iniciar_chat(evento): # Toda função que recebe "On_Click" recebe geralmente o parametro "evento"
        pagina.dialog = popup
        popup.open = True # Ativar o Popup
        pagina.update() # Atualizar a Pagina
        
           
    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=iniciar_chat)
    
    pagina.add(texto) # Adicionando o "Texto"
    pagina.add(botao_iniciar) # Adicionando o botao_iniciar
    
ft.app(main, view=ft.WEB_BROWSER) # O Começo do App começa no main