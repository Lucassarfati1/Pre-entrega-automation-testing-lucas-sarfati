# Pre-entrega - Automation Testing

## Descripción

Proyecto de automatización de pruebas funcionales para el sitio [SauceDemo](https://www.saucedemo.com/), desarrollado con Python, Selenium WebDriver y Pytest.

El objetivo es validar funcionalidades principales del sitio mediante pruebas automatizadas de interfaz de usuario.

## Tecnologías utilizadas

- Python
- Selenium WebDriver
- Pytest
- pytest-html
- Google Chrome

## Casos de prueba implementados

1. **Apertura del sitio:** verifica que SauceDemo cargue correctamente y que el campo de usuario esté visible.
2. **Inicio de sesión:** valida el acceso con credenciales válidas y la redirección al catálogo.
3. **Catálogo de productos:** comprueba que el título sea correcto, que existan productos y que el menú y el filtro estén visibles. También muestra el nombre y precio del primer producto.
4. **Carrito de compras:** agrega el primer producto, verifica el contador del carrito y comprueba que el producto figure correctamente en él.

## Requisitos previos

- Python instalado.
- Google Chrome instalado.
- Git, para clonar el repositorio si corresponde.

## Instalación

Clonar el repositorio y entrar en la carpeta del proyecto.

```bash
git clone URL_DEL_REPOSITORIO
cd NOMBRE_DEL_PROYECTO
```

Crear y activar un entorno virtual.

En Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución de las pruebas

Ejecutar todos los casos de prueba:

```bash
python -m pytest Tests/ -v -s
```

## Reportes

El proyecto contempla la generación de reportes HTML para consultar los resultados de la ejecución de las pruebas.

## Autor

Lucas Sarfati