from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

navegador.get("https://www.magazineluiza.com.br/")

# Aguarde por uma entrada do usuário antes de encerrar o programa
input("Pressione Enter para encerrar o navegador...")

navegador.quit()  # O navegador será fechado somente após o usuário pressionar Enter
navegador.find_element(By.ID, 'input-search').send_keys("Smartphone")