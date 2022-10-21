from pytest import mark
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

@mark.name
def test_nombre():
    driver = webdriver.Chrome()
    driver.get('https://www.amazon.com')
    wait = WebDriverWait(driver, 120)

    # INICIO DE SECCION
    # apunta al boton de cuenta para direccionarse en ella
    namein = wait.until(EC.visibility_of_element_located((By.ID, 'nav-link-accountList-nav-line-1')))
    namein.click()
    assert namein.is_displayed()

    # apunta al text para poner nombre o usuario y le envia un correo.
    #si quieres puedes ponerle tu correo para iniciar
    nameuser = wait.until(EC.visibility_of_element_located((By.ID, 'ap_email')))
    nameuser.send_keys("natividadromney@gmail.com")

    # apunta al boton de continuar
    namecontinue = wait.until(EC.visibility_of_element_located((By.ID, 'continue')))
    namecontinue.click()
    assert namecontinue.is_displayed()

    # apunta a la contraseña y la introduce
    #tambien cambiar la contraseña
    namepass = wait.until(EC.visibility_of_element_located((By.ID, 'ap_password')))
    namepass.send_keys("samuel.romney14")

    # apunta al boton de iniciar seccion
    nameintro = wait.until(EC.visibility_of_element_located((By.ID, 'signInSubmit')))
    nameintro.click()

    # MENU DE AJUSTES EN AMAZON
    # apunta al boton que direcciona a la cuenta
    cuent2btn = wait.until(EC.visibility_of_element_located((By.ID, 'nav-link-accountList')))
    cuent2btn.click()
    assert cuent2btn.is_displayed()

    # apunta al boton de security para editar el nombre
    profile = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="a-page"]/div[2]/div/div[2]/div[2]/a')))
    profile.click()
    assert profile.is_displayed()

    # PRIMER CASO DE USO NUMERO 1, CAMBIAR NOMBRE DEL PROPIETARIO
    # apunta al boton para editar el nombre
    editname = wait.until(EC.visibility_of_element_located((By.ID, 'auth-cnep-edit-name-button')))
    editname.click()
    assert editname.is_displayed()

    # apunta al text elemento de editar y borra
    edittext = wait.until(EC.visibility_of_element_located((By.ID, 'ap_customer_name')))
    edittext.clear()
    # apunta al text elemento de editar y envia el nombre
    edittext.send_keys("Samuel Romney")

    # apunta al boton guardar y hace cambios
    savecha = wait.until(EC.visibility_of_element_located((By.ID, 'cnep_1C_submit_button')))
    savecha.click()
    assert savecha.is_displayed()

    # MENU DE AJUSTED DE LA CUENTA DE AMAZON
    # returna a la ventana de tu cuenta
    returnyouraccount = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="breadcrumb_CNEP"]/li[1]/span/a')))
    returnyouraccount.click()
    assert returnyouraccount.is_displayed()

    # apunta al boton de direccion del usuario
    youraddress = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="a-page"]/div[2]/div/div[6]/div[1]/div/div/ul/li[1]/span/a')))
    youraddress.click()
    assert youraddress.is_displayed()
    sleep(15)
