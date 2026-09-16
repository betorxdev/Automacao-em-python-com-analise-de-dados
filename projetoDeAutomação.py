#automação em python com analise de dados

import pyautogui
import time
import pandas
import pyperclip

# passo a passo do código
# passo um: abrir o navegador e entrar no link do drive

#anotação de funções do pyautogui

#pyautogui.click
#pyautogui.write
#pyautogui.press
#pyautogui.hotkey

pyautogui.press('win')
pyautogui.write('Chrome')
pyautogui.press('enter')

time.sleep(5)

link = ('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga')

pyautogui.write(link)
pyautogui.press('enter')

time.sleep(3)

#passo dois: entrar na pasta exportar e fazer o download da base de dados

pyautogui.click(x=321, y=363, clicks=2) #abre a pasta
time.sleep(5)
pyautogui.click(x=1576, y=363, clicks=1) #clica nos tres pontinhos
time.sleep(5)
pyautogui.click(x=1312, y=450) #clica no download
time.sleep(5)

#passo tres: importar a base de dados para o python
caminho_arquivo = r"D:\Download\Vendas - Dez (1).xlsx"
tabela = pandas.read_excel(caminho_arquivo)
print(tabela)
faturamento = tabela['Valor Final'].sum()
qtde_vendas = tabela['Quantidade'].sum()

print(faturamento)
print(qtde_vendas)

#paso quatro: enviar um e-mail pelo gmail
pyautogui.hotkey('ctrl', 't')
pyautogui.write('https://mail.google.com/mail/u/0/#inbox') 
pyautogui.press('enter')

time.sleep(5)

pyautogui.click(x=56, y=225) #clica no botão escrever
time.sleep(10)

pyautogui.write('betoex97+codigo@gmail.com') #escreve o e-mail do destinatário
pyautogui.press('tab') #passa para o campo de assunto
pyautogui.press('tab') #passa para o campo de assunto

pyperclip.copy('Relatório de vendas') #copia o assunto do e-mail
pyautogui.hotkey('ctrl', 'v') #escreve o assunto do e-mail

pyautogui.press('tab') #passa para o campo de corpo do e-mail
time.sleep(5)
#corpo do e-mail
texto = f"""
Prezados,

Segue o relatório de vendas do mês de dezembro.

Faturamento: R$ {faturamento:,.2f}
Quantidade de Vendas: {qtde_vendas:,}

Atenciosamente,
Roberto
"""
pyperclip.copy(texto)
pyautogui.hotkey('ctrl', 'v') #escreve o corpo do e-mail
time.sleep(5)
pyautogui.click(x=1048, y=976)