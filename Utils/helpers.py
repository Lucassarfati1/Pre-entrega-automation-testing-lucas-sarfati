
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def iniciar_sesion(driver):
    """Abre SauceDemo e inicia sesión con un usuario válido."""

    driver.get("https://www.saucedemo.com/")

    wait = WebDriverWait(driver, 10)

    campo_usuario = wait.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )
    campo_usuario.send_keys("standard_user")

    campo_password = wait.until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    campo_password.send_keys("secret_sauce")

    boton_login = wait.until(
        EC.element_to_be_clickable((By.ID, "login-button"))
    )
    boton_login.click()

    wait.until(EC.url_contains("/inventory.html"))
