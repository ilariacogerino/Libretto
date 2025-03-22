import datetime

import flet as ft

#CONTIENE LA CLASSE VIEW
class View:
    def __init__(self, page: ft.Page):
        self._txtOut = None
        self._btnIn = None
        self._txtIn = None
        self._controller = None #LO AGGIUNGO ALL'INIT PARI A NULLO
        self._page = page #FUNZIONA DA COSTRUTTORE

    # FUNZIONE PER LA CREAZIONE DELL'INTERFACCIA
    def loadInterface(self):
        """
        In questo metodo definiamo e carichiamo
        tutti i controlli dell'interfaccia.
        :return:
        """
        self._page.bgcolor = "white"
        self._titolo = ft.Text("Libretto Voti", color="red", size=24) #INSERISCO IL TITOLO
        self._student = ft.Text(value=self._controller.getStudent(), color="brown")
        row1 = ft.Row([self._titolo],
                      alignment=ft.MainAxisAlignment.CENTER)
        row2 = ft.Row([self._student],
                      alignment=ft.MainAxisAlignment.END)

        self._txtIn = ft.TextField(label="Inserisci nome")
        self._btnIn = ft.ElevatedButton("Aggiungi",
                                        on_click=self._controller.handleAggiungi)

        # RIGA dei controlli
        self._txtInNome = ft.TextField(
            label="Nome esame",
            hint_text="Inserisci il nome dell'esame",
            width=300
        )
        self._ddVoto = ft.Dropdown(
            label="Voto",
            width=120
        )
        self._fillDDVoto() #SERVE PER INSERIRE LE OPZIONI ALL'INTERNO DEL MENU' A TENDINA

        self._dp = ft.DatePicker(
            first_date=datetime.datetime(2022, 1, 1),
            last_date=datetime.datetime(2026, 12, 31),
            on_change=lambda e: print(f"Giorno selezionato: {self._dp.value}"),
            on_dismiss=lambda e: print("Data non selezionata") #STAMPA IN CONSOLE NEL CASO IN CUI NON VENGA SELEZIONATA UNA DATA
        )
        self._btnCal = ft.ElevatedButton("Pick date",
                                         icon=ft.Icons.CALENDAR_MONTH,
                                         on_click=lambda _: self._page.open(self._dp))

        self._btnAdd = ft.ElevatedButton("Aggiungi",
                                         on_click=self._controller.handleAggiungi)
        self._btnPrint = ft.ElevatedButton("Stampa",
                                           on_click=self._controller.handleStampa)
        row3 = ft.Row([self._txtInNome,
                       self._ddVoto,
                       self._btnCal,
                       self._btnAdd,
                       self._btnPrint],
                      alignment=ft.MainAxisAlignment.CENTER)

        self._txtOut = ft.ListView(expand=True)
        self._page.add(row1, row2, row3, self._txtOut)
        #L'ORDINE DI AGGIUNTA EQUIVALE ALL'ORDINE DI VIUSALIZZAZIONE

    #FUNZIONE CHE PRENDE UN CONTROLLER E LO ASSEGNA ALLA VIEW
    def setController(self, c):
        self._controller = c

    def _fillDDVoto(self):
        for i in range(18, 30):
            self._ddVoto.options.append(ft.dropdown.Option(str(i)))
        self._ddVoto.options.append(ft.dropdown.Option("30L"))
