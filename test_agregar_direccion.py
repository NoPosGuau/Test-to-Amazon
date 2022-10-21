from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from pytest import mark
from time import sleep

@mark.add
def test_address():
     driver = webdriver.Chrome()
    driver.get('https://www.amazon.com')
    wait = WebDriverWait(driver, 120)

    # INICIO DE SECCION
    # apunta al boton de cuenta para direccionarse en ella
    cuentbtn_add = wait.until(EC.visibility_of_element_located((By.ID, 'nav-link-accountList-nav-line-1')))
    cuentbtn_add.click()
    assert cuentbtn_add.is_displayed()

    # apunta al text para poner nombre o usuario y le envia un correo
    cuentain = driver.find_element(By.XPATH, '//*[@id="ap_email"]')
    cuentain.send_keys("natividadromney@gmail.com")

    # apunta al boton de continuar
    cuentabtn2_add = wait.until(EC.visibility_of_element_located((By.ID, 'continue')))
    cuentabtn2_add.click()
    assert cuentabtn2_add.is_displayed()

    # apunta a la contraseña y la introduce
    cuentabtn3_add = driver.find_element(By.NAME, 'password')
    cuentabtn3_add.send_keys("samuel.romney14")

    # apunta al boton de iniciar seccion
    cuentabtn4add = wait.until(EC.visibility_of_element_located((By.ID, 'signInSubmit')))
    cuentabtn4add.click()

    # CASO DE USO NUMERO 2, AÑADIR UNA DIRECCION DE ENTREGA
    #apunta al boton de la cuenta
    cuentbtn5_add = wait.until(EC.visibility_of_element_located((By.ID, 'nav-link-accountList-nav-line-1')))
    cuentbtn5_add.click()
    assert cuentbtn_add.is_displayed()

    #apunta al boton de la seccion de direccion
    addreuser = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="a-page"]/div[2]/div/div[6]/div[1]/div/div/ul/li[1]/span/a')))
    addreuser.click()
    assert addreuser.is_displayed()

    # apunta al boton de añadir direccion
    addaddress = wait.until(EC.visibility_of_element_located((By.ID, 'ya-myab-plus-address-icon')))
    addaddress.click()
    assert addaddress.is_displayed()

    # apunta a el text de nombre de direccion y envia el nombre
    addressname = wait.until(EC.visibility_of_element_located((By.ID, 'address-ui-widgets-enterAddressFullName')))
    addressname.clear()
    addressname.send_keys("Samuel Romney Mejia #RD77044")

    # apunta al text del telefono y envia el telefono
    addressphone = wait.until(EC.visibility_of_element_located((By.ID, 'address-ui-widgets-enterAddressPhoneNumber')))
    addressphone.send_keys("8098282892")

    # apunta al text de la calle de la direccion
    addressstreet = wait.until(EC.visibility_of_element_located((By.ID, 'address-ui-widgets-enterAddressLine1')))
    addressstreet.send_keys("7801 NW 37th Street")

    # apunta al text de ciudad de la direccion y envia la ciudad
    addresscity = wait.until(EC.visibility_of_element_located((By.ID, 'address-ui-widgets-enterAddressCity')))
    addresscity.send_keys("Doral")

    # apunta al Combobox selec del estado y selecciona el estado
    addressselect_file = Select(wait.until(EC.visibility_of_element_located((By.NAME, 'address-ui-widgets-enterAddressStateOrRegion'))))
    addressselect_file.select_by_value('FL')

    # apunta al zip code y envia el code postal
    zipcode = wait.until(EC.visibility_of_element_located((By.ID, 'address-ui-widgets-enterAddressPostalCode')))
    zipcode.send_keys("33195")

    # apunta al boton de añadir direccion creada
    addaddress1 = wait.until(EC.visibility_of_element_located((By.ID, 'address-ui-widgets-form-submit-button')))
    addaddress1.click()
    assert addaddress1.is_displayed()

    # INICIO DE AMAZON
    # apunta al boton de inicio y direcciona al inicio de amazon
    inicio = wait.until(EC.visibility_of_element_located((By.ID, 'nav-logo-sprites')))
    inicio.click()
    assert inicio.is_displayed()
    sleep(15)
