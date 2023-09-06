#Importando as bibliotecas a serem utilizadas
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
#Importando o cadastro dos cliente(já pre tratado sem celulas em branco)
df = pd.read_excel('cadastro_clientes.xlsx')
# Abrindo o navegador e fazendo o login
wb = webdriver.Edge()
wb.maximize_window()
wb.get('http://automacao.empowerdata.com.br')
email = wb.find_element(By.XPATH, '//*[@id="email"]')
email.send_keys('aluno@empowerdata.com.br')
senha = wb.find_element(By.XPATH, '//*[@id="password"]')
senha.send_keys('empowerpython')
time.sleep(1)
botao_entrar = wb.find_element(By.XPATH,'//*[@id="submit"]')
botao_entrar.click()
time.sleep(3)
# Cadastrando os cliente no sistema
for __, linha in df.iterrows(): 
   if len(linha['Nome'])>= 40 or len(linha['E-mail'])>=51 or len(linha['Telefone'])>=15 or len(linha['Cidade'])>= 35 or len(linha['Estado'])>=35:
      with open ('log_erros.txt','a') as log:
         log.write(f" O cliente: {linha['Nome']},não foi cadastrado devido ao numero de caracteres inserido maior do que o permitido. Abreviar e tentar novamente!\n")
   elif linha['E-mail'].count('@') != 1:
        with open ('log_erros.txt','a') as log:
         log.write(f" O cliente: {linha['Nome']}, não pode ser cadastrado pois não possui o campo e-mail (obrigatório) válido.\n")
   else:
      cliente = wb.find_element(By.XPATH,'//*[@id="nome"]')
      cliente.send_keys(linha['Nome'])
      email = wb.find_element(By.XPATH, '//*[@id="email"]')
      email.send_keys(linha['E-mail'])
      telefone = wb.find_element(By.XPATH, '//*[@id="telefone"]')
      telefone.send_keys(linha['Telefone'])
      cidade = wb.find_element(By.XPATH, '//*[@id="cidade"]')
      cidade.send_keys(linha['Cidade'])
      estado = wb.find_element(By.XPATH, '//*[@id="estado"]')
      estado.send_keys(linha['Estado'])
      time.sleep(1)
      estado.send_keys(Keys.ENTER)
      time.sleep(1)
# Mostra a aba consulta por 30 segundos
time.sleep (1)
botao_consulta = wb.find_element(By.XPATH,'/html/body/nav/div/ul/li[2]/a')
botao_consulta.click()
time.sleep (30)
#Fechando o navegador
wb.close()