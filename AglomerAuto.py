from selenium import webdriver
import time

browser = webdriver.Chrome(executable_path='./driver/chromedriver')

def seleccionar_chat(nombre : str):
    buscando = True

    while buscando:
        print("BUSCANDO CHAT")
        elements = browser.find_elements_by_tag_name("span")
        for element in elements:
            if element.text == nombre:
                print("ENCONTRAMOS AL IMPOSTOR")
                element.click()
                buscando = False
                break

def enviar():
    element = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
    element.click()
    print("MENSAJE ENVIADO")

def enviar_mensaje(mensaje: str):
    chatbox = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
    chatbox.send_keys(mensaje)
    time.sleep(2)
    enviar()

def leer_archivo(ruta:str):
    archivo = open(ruta, mode='r', encoding='utf-8')
    chatbox = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')

    for linea in archivo.readlines():
        print ("MENSAJE : ", linea)
        chatbox.send_keys(linea)

    archivo.close()

def valida_qr():
    try:
        element = browser.find_element_by_tag_name('canvas')
    except:
        return False
    return True

def bot_whatsapp():
    browser.get("https://web.whatsapp.com/")
    time.sleep(5)

    espera = True

    while espera:
        print("ESTOY ESPERANDO")
        espera = valida_qr()
        time.sleep(2)
        if espera == False:
            print("SE AUTENTICO")
            break

    seleccionar_chat("Madre")
    time.sleep(2)
    leer_archivo('./resource/plantilla.txt')

bot_whatsapp()