from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utils.helpers import iniciar_sesion

def test_chrome_abre_saucedemo(driver):
    # Navega al sitio de pruebas
    driver.get("https://www.saucedemo.com/")

    # Espera hasta 10 segundos a que aparezca el campo de usuario
    usuario = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )

    # Verifica que la página sea la esperada
    assert "Swag Labs" in driver.title
    assert usuario.is_displayed()

    print("El navegador Chrome se abrió correctamente y la página de pruebas está disponible.")

def test_login_exitoso(driver):
    # 1. Abrir la página de login
   iniciar_sesion(driver)

def test_catalogo_productos(driver):
    # Inicio de sesion
    iniciar_sesion(driver)
    # 4. Validar el título de la página
    wait = WebDriverWait(driver, 10)

    titulo = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    )
    assert "/inventory.html" in driver.current_url, (
    f"No se ingresó al inventario. URL actual: {driver.current_url}"
    )

    assert titulo.text == "Products", (
    f"Título inesperado. Se esperaba 'Products' y se obtuvo '{titulo.text}'"
    )

    # 5. Comprobar que haya productos visibles
    productos = driver.find_elements(
        By.CLASS_NAME, "inventory_item"
    )

    assert len(productos) > 0, (
    "El catálogo no contiene productos visibles."
)

    # 6. Obtener el nombre y precio del primer producto
    primer_producto = productos[0]

    nombre = primer_producto.find_element(
        By.CLASS_NAME, "inventory_item_name"
    ).text

    precio = primer_producto.find_element(
        By.CLASS_NAME, "inventory_item_price"
    ).text

    print(f"Primer producto: {nombre}")
    print(f"Precio: {precio}")

    # 7. Validar que el menú y el filtro estén presentes
    menu = driver.find_element(By.ID, "react-burger-menu-btn")
    filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")

    assert menu.is_displayed(), "El menú no está visible"
    assert filtro.is_displayed(), "El filtro no está visible"



def test_agregar_producto_al_carrito(driver):
    # 1. Iniciar sesión
    iniciar_sesion(driver)
    # 4. Obtener el primer producto
    wait = WebDriverWait(driver, 10)
    primer_producto = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_item")
        )
    )
    assert "/inventory.html" in driver.current_url, (
    f"No se ingresó al inventario. URL actual: {driver.current_url}"
)

    nombre_producto = primer_producto.find_element(
        By.CLASS_NAME, "inventory_item_name"
    ).text

    # 5. Agregar el producto al carrito
    boton_agregar = primer_producto.find_element(
        By.TAG_NAME, "button"
    )
    boton_agregar.click()

    # 6. Verificar que el contador del carrito sea 1
    contador = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "shopping_cart_badge")
        )
    )

    assert contador.text == "1", "El contador del carrito no es 1"

    # 7. Entrar al carrito
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    wait.until(EC.url_contains("/cart.html"))

    # 8. Verificar que el producto esté en el carrito
    producto_carrito = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "cart_item")
        )
    )

    nombre_carrito = producto_carrito.find_element(
        By.CLASS_NAME, "inventory_item_name"
    ).text

    assert nombre_carrito == nombre_producto, (
    f"El producto del carrito ('{nombre_carrito}') no coincide "
    f"con el agregado ('{nombre_producto}')."
)

    print(f"Producto agregado correctamente: {nombre_carrito}")