from pytest import mark
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

@mark.car
def test_carrito():
    driver = webdriver.Chrome()
    driver.get('https://www.amazon.com')
    wait = WebDriverWait(driver, 15)

    # INICIO DE SECCION
    # apunta al boton de cuenta para direccionarse en ella
    cuentbtn_car = driver.find_element(By.ID, 'nav-link-accountList-nav-line-1')
    cuentbtn_car.click()
    assert cuentbtn_car.is_displayed()

    # apunta al text para poner nombre o usuario y le envia un correo
    texcarcuenta = driver.find_element(By.XPATH, '//*[@id="ap_email"]')
    texcarcuenta.send_keys("natividadromney@gmail.com")
    assert texcarcuenta.is_displayed()

    # apunta al boton de continuar
    texcarcontinue = driver.find_element(By.ID, 'continue')
    texcarcontinue.click()
    assert texcarcontinue.is_displayed()

    # apunta a la contraseña y la introduce
    carpass = driver.find_element(By.NAME, 'password')
    carpass.send_keys("samuel.romney14")

    # apunta al boton de iniciar seccion
    carbtn = driver.find_element(By.ID, 'signInSubmit')
    carbtn.click()

    # CASO DE USO NUMERO 3, AÑADIR UN PRODUCTO AL CARRITO(iPhone 13 Pro Max Color Plateado de 512GB)
    # apunta al text del inicio para buscar el producto
    textbox = wait.until(EC.visibility_of_element_located((By.ID, 'twotabsearchtextbox')))
    textbox.send_keys("iPhone 13 Pro Max")

    # apunta al boton de buscar para buscar el producto
    searchbtn = wait.until(EC.visibility_of_element_located((By.ID, 'nav-search-submit-button')))
    searchbtn.click()
    assert searchbtn.is_displayed()

    # apunta al producto deseado
    iphonebtn = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[3]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/span/a/div/img')))
    iphonebtn.click()
    assert iphonebtn.is_displayed()

    # despues en el producto, seleccionamos las especificacion de almacenamiento
    iphonegb = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div[3]/div[2]/div[12]/div/div[1]/ul/li[4]/span/a/span/span/input')))
    iphonegb.click()
    assert iphonegb.is_displayed()

    # apunta al color del producto
    iphonecolor = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="a-autoid-27"]/span/input')))
    iphonecolor.click()
    assert iphonecolor.is_displayed()

    # apunta a la compañia telefonica deseada
    iphonecarrier = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="a-autoid-28-announce"]/div/div/div[1]/div/label/input')))
    iphonecarrier.click()
    assert iphonecarrier.is_displayed()

    # apunta al boton de añadir al carrito, despues de seleccionar las especificaciones
    iphonecarrito = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-form"]/div/span[1]/span/input')))
    iphonecarrito.click()
    sleep(3)

    # Apunta al boton de no thanks del plan de proteccion
    btnnothanks = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/span/span[2]/span/button')
    btnnothanks.click()
    sleep(2)
    sleep(15)
