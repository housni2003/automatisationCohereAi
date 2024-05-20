from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Lancement d'une instance de navigateur
driver = webdriver.Chrome()

# Ouvrir la page
driver.get("https://dashboard.cohere.com/welcome/login")

# Attendre que le champ de texte soit cliquable
email_field = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'email'))
)

# Entrer du texte dans le champ de texte
email_field.send_keys("") ## your mail
email_field.submit()

# Attendre que le champ de texte soit cliquable
mdp_field = WebDriverWait(driver, 50).until(
    EC.element_to_be_clickable((By.ID, 'password'))
)

# Entrer du texte dans le champ de texte
mdp_field.send_keys("") #your password
mdp_field.submit()
# Attendre avant de fermer le navigateur


button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/div[2]/div[2]/div/div/form/button/div/div/div[1]/div/div/span/span'))
)

# Cliquez sur le bouton
button.click() #clique sur login

button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/div/div[2]/main/div[2]/div/section[2]/div[1]/a/div/div/div[1]/div/div/span/span'))
)

# Cliquez sur le bouton
button.click() #clique sur coral+
# Input text into the text field

all_windows = driver.window_handles

driver.switch_to.window(all_windows[1]) # ne pas oublier de changer de page

text_field = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="composer"]')) # cherche à définir text field
)
text_field.send_keys("hello") #text you want to submit to cohere

# Attendre que le bouton soit cliquable
button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div/div[2]/button[3]'))
)

# Cliquer sur le bouton
button.click()

# Attendre que le bouton soit cliquable
button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="message-list"]/div[2]/div/div/div/button'))
)

# Cliquer sur le bouton
button.click()
input("Appuyez sur Entrée pour fermer le navigateur...")

