from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
#from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup

from tkinter import *

import pandas as pd

import re


import datetime
import time


# -------------------------------------------- Funciones ------------------------------------

# -------------------- CREAR CAJA CEC --------------------------------------

# --------------------------------------------------------------------------


# ------------------------- LOGGIN -----------------------------------------
def loggin(n_id):
    # driver.maximize_window()
    driver.get("http://netcracker.telecentro.net.ar/login.jsp")
    time.sleep(2)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="user"]'))).send_keys("cchirinos")
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="pass"]'))).send_keys("Martes1001")
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="login_button"]/div/input'))).click()
    time.sleep(1)
    driver.get("http://netcracker.telecentro.net.ar/common/search.jsp?property_ishidden_widget_scope_options=yes&xtype_714051338784=714051338784&search_mode=search&resultID=9165816141113048703&resultID=9165816141113048703&resultID=9165816141113048703&resultID=9165816141113048703&ctrl=t4122758596013619618_4122758596013619619&fast_search=no&_r9153546144913342788=eq&_r_1=eq&project=9151724066113891696&_r_2=eq&currobject=o&_v9152341142913787049="+n_id +
               "&cfadmin=r3U5-7bmE-vDsU-Y21g-NkRk-2S7L&collapse_but=no&do_search=yes&tab=0&property_ishidden_widget_templates=yes&explorer_mode=disable&property_ishidden_group_1090440074013323208=no&_r9153546170713343080=eq&system_index_on=false&_r9153547191513344701=eq&_r9152341142913787049=eq&casesense=yes&performed=true&o=9164267356413376860&_r9152336626013786227=eq&property_ishidden_group_9151725483613892290=no&_r9153546135313342751=eq&property_ishidden_group_8033139507013843604=no&currproject=default&profile_id=9153545484513339406&property_ishidden_group_-10=no&return=%2Fncobject.jsp%3Fid%3D9164267356413376860&object=9153545484513339406&property_ishidden_group_9129989742913974018=no")
# --------------------------------------------------------------------------

# -------------------- CREAR CAJA CEC --------------------------------------


def crearCEC(ncaja):
    print("Crea la caja CEC -", ncaja)

    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="9153536506213318087"]'))).click()
    time.sleep(1)

    # ---------- koc / SSC2806-SM-8 / SPLICE ----------------
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="title"]'))).send_keys("SSC2806-SM-8")
    time.sleep(0)

    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="main_window"]/tbody/tr[7]/td/div[2]/div/a'))).click()
    time.sleep(1)

    """
    #---------------------- Link directo al resultado de buscar el tipo de caja pero toma otra referencia y no el ID --------------------- 
        driver.get("http://netcracker.telecentro.net.ar/common/uedit.jsp?parent=9165226387213207226&class=301&return=%2Fcommon%2Fuobject.jsp%3FisDefaultTab%3Dtrue%26tab%3Dsites_and_devices%26id%3D9165226387213207226%26object%3D9165226387213207226%26ctrl%3Dt9153483960513284291_0&attr=9153536506213318087&types=301&tab=repository&tab=template&tab=repository&title=SSC2806-SM-8&createnew=1&otype=301&reposprj=1091347815013411785&tab=repository&tab=template&tab=repository&lookin=301&types=301&class=301&search=1")
        time.sleep(50)
    #--------------------------------------------------------------------------------------------------------
    """
    # crear la CEC
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="xnewname"]')))
    driver.find_element(
        by="xpath", value='//*[@id="xnewname"]').clear()
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="xnewname"]'))).send_keys("CEC-"+ncaja)
    time.sleep(0)
    dropdwn = driver.find_element(
        By.XPATH, '/html/body/div[4]/div[1]/div[2]/div/form/table/tbody/tr/td/table[3]/tbody/tr[10]/td[2]/span/table/tbody/tr/td/div/select')
    dd = Select(dropdwn)
    dd.select_by_value("9157892687313570129")
    time.sleep(0)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="search_window"]/tbody/tr[11]/td/div[1]/div/a'))).click()

    # Pestaña Slots
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id = "id_tab_2"]/a'))).click()
    time.sleep(1)

    # insertar Splitter
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="s_t"]/tbody/tr/td[1]/label/input'))).click()
    time.sleep(0)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="7103060739013917222"]'))).click()
    time.sleep(1)

    # Insertar Card

    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="card1"]'))).click()
    time.sleep(0)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="create_bt_id"]'))).click()
    time.sleep(1)

    # Configurar Splitter
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="s_t"]/tbody/tr/td[3]/a/span'))).click()
    time.sleep(1)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="id_tab_9"]/a'))).click()
    time.sleep(0)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="pcEdit"]'))).click()
    time.sleep(1)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[4]/div[1]/div[2]/div/div/form/table/tbody/tr/td/table[3]/tbody[8]/tr/td[2]/span/table/tbody/tr/td/textarea'))).send_keys('{\n"version":1,\n"servicios":[\n{\n"pisos": "Todos",\n"departamentos": "todos",\n"descripcionCaja": "CEC-'+ncaja+'",\n"destinoPuertos":[\n{\n"1":"1",\n"2":"2",\n"3":"3",\n"4":"4",\n"5":"5",\n"6":"6",\n"7":"7",\n"8":"8"\n}\n]\n}\n]\n}\n')
    time.sleep(0)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="theform_update"]'))).click()
    time.sleep(1)

    # volver al home ID
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[4]/div[1]/div[1]/div[1]/div/a[8]/span[1]'))).click()
# --------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------


# -------------------------------------------- VARIABLES ------------------------------------
#ID = "1408470"

path = "/chromedriver.exe"
Service = Service(executable_path=path)
driver = webdriver.Chrome(service=Service)
wait = WebDriverWait(driver, 10)
# driver.maximize_window()
# driver.minimize_window()


#input1 = input("Ingrese el ID")
#ID = input1


# ------------------------------- CICLO PRINCIPAL -----------------

def principal(numeroid, numerocaja1, numerocaja2, numerocaja3):
    print("Campo texto ID", numeroid)
    print("Campo texto CAJA1", numerocaja1)
    print("Campo texto CAJA2", numerocaja2)
    print("Campo texto CAJA3", numerocaja3)

    #label1 = Label(ventana, text="Generando...........")
    #label1.place(x=120, y=280)

    loggin(numeroid)

    time.sleep(1)

    if (len(driver.find_elements(by="xpath", value='/html/body/div[4]/div[1]/div[2]/div/table/tbody/tr/td[2]/font/div')) != 0):
        print("No se encuentra el ID", len(driver.find_elements(
            by="xpath", value='/html/body/div[4]/div[1]/div[2]/div/table/tbody/tr/td[2]/font/div')))
        label1 = Label(ventana, text="El ID no se encuentra cargado en NC")
        label1.place(x=120, y=320)
        driver.quit()
    else:
        print("Si se encuentra el ID", len(driver.find_elements(
            by="xpath", value='/html/body/div[4]/div[1]/div[2]/div/table/tbody/tr/td[2]/font/div')))

        wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="t4122361118013615427_9153545484513339405_t"]/tbody/tr/td[2]/a/span'))).click()

        # -------- Crea las cajas CEC -----------------

        if (numerocaja1 != ""):
            print("entro en: 1")
            crearCEC(numerocaja1)

        if (numerocaja2 != ""):
            print("entro en: 2")
            crearCEC(numerocaja2)

        if (numerocaja3 != ""):
            print("entro en: 3")
            crearCEC(numerocaja3)

        # -------- Crea las cajas CES -----------------

        time.sleep(10)

    # -------------------------------Bandeja de Cierre de Relevamiento-----
    print("Fin")

    input("Esperando que no se cierre webdriver: ")

    driver.quit()
# ---------------------------------------------------------------------------------------------------------------------------------


# ---------------------------------------- INTERFAZ VENTANA -----------------------------------
ventana = Tk()
ventana.geometry("400x500")
ventana.title("NetCracker")


# numeroID.set("111111")

titulo1 = Label(ventana, text="ASISTENTE CARGA NetCracker",
                font=("Tahoma", 20), fg="#FFFFFF", bg="#0059b3")
titulo1.pack(fill=X)
titulo2 = Label(ventana, text="Diseños Exterior", font=(
    "Tahoma", 12), fg="#FFFFFF", bg="#0059b3")
titulo2.pack(fill=X)


etiqueta1 = Label(ventana, text="Ingrese el ID")
etiqueta1.place(x=10, y=80)
inID = Entry(ventana, font="20")
inID.place(x=100, y=80)
# inID.set("1408470")

# ---------------- Cajas CEC ----------------------------

etiquetaCEC = Label(ventana, text="Ingrese el Nro de la CAJA CEC")
etiquetaCEC.place(x=20, y=120)

etiqueta2 = Label(ventana, text="CEC-")
etiqueta2.place(x=40, y=150)
inCAJA1 = Entry(ventana, font="20", width=3)
inCAJA1.place(x=70, y=150)

etiqueta3 = Label(ventana, text="CEC-")
etiqueta3.place(x=40, y=180)
inCAJA2 = Entry(ventana, font="20", width=3)
inCAJA2.place(x=70, y=180)

etiqueta4 = Label(ventana, text="CEC-")
etiqueta4.place(x=40, y=210)
inCAJA3 = Entry(ventana, font="20", width=3)
inCAJA3.place(x=70, y=210)

# ---------------- Cajas CES ----------------------------

etiquetaCES = Label(ventana, text="Ingrese el Nro de la CAJA CES")
etiquetaCES.place(x=220, y=120)

etiqueta10 = Label(ventana, text="CES-")
etiqueta10.place(x=250, y=150)
inCAJACES1 = Entry(ventana, font="20", width=3)
inCAJACES1.place(x=280, y=150)

etiqueta11 = Label(ventana, text="CES-")
etiqueta11.place(x=250, y=180)
inCAJACES2 = Entry(ventana, font="20", width=3)
inCAJACES2.place(x=280, y=180)

etiqueta12 = Label(ventana, text="CES-")
etiqueta12.place(x=250, y=210)
inCAJACES3 = Entry(ventana, font="20", width=3)
inCAJACES3.place(x=280, y=210)


boton1 = Button(ventana, text="GENERAR", font=("Tahoma", 12), fg="#FFFFFF", bg="#008f39",
                padx=30, pady=15, command=lambda: principal(inID.get(), inCAJA1.get(), inCAJA2.get(), inCAJA3.get()))
boton1.place(x=120, y=280)
ventana.mainloop()

# ---------------------------------------------------------------------------------------------
# ------------------------------------
"""





"""
