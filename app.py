import flet as ft

from controller import Controller
from view import View
 #FILE CHE METTE IN COMUNICAZIONE VIEW, CONTROLLER, MODEL(VOTO)
 # NORMALMENTE QUESTO PRENDE IL NOME DI MAIN, NON APP

def main(page: ft.Page):
    v = View(page) #CREO UNA ISTANZA DELLA CLASSE VIEW, CHE IMPORTO; INSERISCE NELLA PAGINA I CONTROLLER
    c = Controller(v) #GLI PASSO IL V (OVVERO LA VIEW)
    v.setController(c) #METODO DELLA VIEW IN CUI SETTO IL CONTROLLER, IN MODO DA METTERE IN COMUNICAZIONE VIEW E CONTROLLER
    v.loadInterface()

ft.app(target=main)
