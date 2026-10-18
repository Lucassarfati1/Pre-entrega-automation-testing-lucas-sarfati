
import os
import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    """Inicia Chrome y captura una evidencia si el test falla."""

    navegador = webdriver.Chrome()
    navegador.maximize_window()

    yield navegador

    # Revisar si el test falló durante su ejecución
    resultado = getattr(request.node, "rep_call", None)

    if resultado is not None and resultado.failed:
        os.makedirs("evidencias", exist_ok=True)

        nombre_test = request.node.name
        ruta_captura = os.path.join(
            "evidencias",
            f"{nombre_test}.png"
        )

        navegador.save_screenshot(ruta_captura)
        print(f"\nCaptura guardada en: {ruta_captura}")

    navegador.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Guarda el resultado de cada fase del test."""
    resultado = yield
    reporte = resultado.get_result()

    setattr(item, f"rep_{reporte.when}", reporte)
