# NovoAdere2025
Projeto Adere Poda 2025
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pandas as pd
import csv
df = pd.read_csv('dados_alimentador.csv',delimiter=';')
nomeAplicativo = input("Digiete o Nome do Usuário: ")
tokenAplicativo = input("Digiete o Nome do Token do Aplicativo: ")

navegador = webdriver.Chrome()
navegador.maximize_window()
navegador.get('https://streetservice.com.br/acesso/login.php')
sleep(2.5)
loginStreetService =navegador.find_element(By.XPATH, '//*[@id="username"]')
senhaStreetService =navegador.find_element(By.XPATH, '//*[@id="token"]')
loginStreetService.send_keys(nomeAplicativo)
senhaStreetService.send_keys(tokenAplicativo)
botaoEntrar = navegador.find_element(By.XPATH,'//*[@id="login-form"]/button')
botaoEntrar.click()
sleep(5)
navegador.get('https://streetservice.com.br/acesso/status.php')
sleep(10)
equipeStreetService = navegador.find_element(By.XPATH,'//*[@id="equipe"]')
equipeStreetService.send_keys("Poda de árvores")
sleep(0.5)

for index, row in df.iterrows():
    alimentador = row['Alimentador']
    alimentadorStreetService = navegador.find_element(By.XPATH,'//*[@id="alimentador"]')
    alimentadorStreetService.send_keys(alimentador)
    sleep(0.5)
    tabelaAlimentador = navegador.find_element(By.XPATH,'//*[@id="tabelaDados"]')
    linhas = tabelaAlimentador.find_elements(By.TAG_NAME, "tr")
    dadosTabela = []
    for linha in linhas:
        celulas = linha.find_elements(By.XPATH, ".//th | .//td")
        if celulas:
           linha_dados = [celula.text.strip() for celula in celulas]
           dadosTabela.append(linha_dados)
    nome_arquivo = f"tabela_{alimentador}.csv"
    df_tabela = pd.DataFrame(dadosTabela)
    df_tabela.to_csv(nome_arquivo, index=False, header=False, encoding='utf-8', sep=';')
    sleep(0.5)
print("Extração de Dados Terminada! ")
input("Precione qualquer Tecla")

Subestação;Alimentador;Regional
BETQ;BETQ404;
BETQ;BETQ405;
BETQ;BETQ407;
BETQ;BETQ408;
BETQ;BETQ410;
BETQ;BETQ413;
BETQ;BETQ415;
BETQ;BETQ416;
BETQ;BETQ417;
BETQ;BETQ419;
BETT;BETT317;
BHAT;BHAT03;
BHAT;BHAT04;
BHAT;BHAT16;
BHAT;BHAT18;
BHAT;BHAT20;
BHJT;BHJT14;
BHJT;BHJT17;
BHSR;BHSR29;
CEMQ;CEMQ404;
CEMQ;CEMQ407;
CEMC;CEMC502;
CEMC;CEMC503;
CEMT;CEMT02;
CEMT;CEMT03;
CEMT;CEMT04;
CEMT;CEMT07;
CEMT;CEMT10;
CEMT;CEMT12;
CEMT;CEMT13;
CEMT;CEMT14;
CEMT;CEMT20;
CEMT;CEMT21;
CEMT;CEMT22;
CEMT;CEMT24;
CEMT;CEMT25;
CICM;CICM01;
CICM;CICM02;
CICM;CICM03;
CICM;CICM04;
CICM;CICM05;
CICM;CICM15;
CICM;CICM26;
CICM;CICM27;
CICM;CICM28;
CICM;CICM30;
CICM;CICM31;
CICM;CICM32;
CICM;CICM34;
CICM;CICM35;
CINC;CINC01;
CINC;CINC02;
CINC;CINC03;
CINC;CINC05;
CINC;CINC07;
CINC;CINC09;
CINC;CINC10;
CINC;CINC11;
CINC;CINC18;
CINC;CINC19;
CINC;CINC20;
CINC;CINC22;
IBRU;IBRU04;
IBRU;IBRU06;
IBRU;IBRU07;
ESR;ESR18;
MDH;MDH06;
MDH;MDH07;
MDH;MDH08;
NLAE;NLAE704;
NLAE;NLAE705;
NLAE;NLAE714;
NLAE;NLAE723;
NLAE;NLAE724;
NLAE;NLAE732;
NLAE;NLAE733;
NLAQ;NLAQ405;
NLAQ;NLAQ407;
NLAQ;NLAQ408;
NLAQ;NLAQ410;
NLAQ;NLAQ413;
NLAQ;NLAQ414;
NLAU;NLAU06;
NLAU;NLAU08;
NLAU;NLAU09;
NLAU;NLAU12;
NLAU;NLAU13;
NLAU;NLAU15;
RCM;RCM05;
RCM;RCM06;
RBST;RBST333;
RBST;RBST334;

