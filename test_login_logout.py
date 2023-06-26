import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="module")
def driver():
    # Set up the WebDriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    # Teardown code, called after the test module completes
    driver.quit()

def test_successful_login(driver):
    # Ouvrir la page web
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)
    # Locators
    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")
    # Entrer les inputs
    username_input.send_keys("Admin")
    password_input.send_keys("admin123")
    # Cliquer le bouton login
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)
    current_url = driver.current_url
    driver.get(current_url)
    time.sleep(5)
    # Le mot "Dashboard" est premiere position dans le current_url
    text_obtenu = driver.find_element(By.TAG_NAME, "h6").text

    txt_attendu = "Dashboard"
    # Verifier le login succes
    assert txt_attendu == text_obtenu

def test_successful_logout(driver):
    # Ce test utilise le test test_successful_login(driver), ca veut dire il est dans la page Dashboard
    # Cliquer sur le bouton user
    driver.find_element(By.CLASS_NAME, "oxd-topbar-header-userarea").click()
    # Le menu dropdown locator
    menu=driver.find_element(By.CLASS_NAME, "oxd-dropdown-menu")
    time.sleep(5)
    # La liste de menu
    liste = menu.find_elements(By.TAG_NAME, "li")
    # Le bouton logout locator
    btn_logout = liste[len(liste)-1]
    # Cliquer sur le bouton logout
    btn_logout.click()
    time.sleep(5)
    # Apres cliquer sur l'item logout, il retourne de la page Login par current_url
    current_url = driver.current_url
    driver.get(current_url)
    time.sleep(5)
    # Le mot "Dashboard" est premiere position dans le current_url
    text_obtenu = driver.find_element(By.TAG_NAME, "h5").text

    txt_attendu = "Login"
    # Verifier le logout avec succes
    assert txt_attendu == text_obtenu

