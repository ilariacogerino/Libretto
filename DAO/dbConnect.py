import mysql.connector


class DBConnect:
    # CLASSE CHE HA UN METODO CHE GENERA CONNESSIONI
    @classmethod #QUESTO DICE AL MIO PROGRAMMA CHE QUESTO E' UN METODO DI CLASSE, NON DI ISTANZA
    def getConnection(cls):
        #LA CREAZIONE DELLA CONNESSIONI PUA' ANCHE FALLIRE, USO TRY E EXCEPT
        try:
            cnx = mysql.connector.connect(user="root",
                                          password="bngh56ty",
                                          host="127.0.0.1",
                                          database="libretto")
            return cnx
        except mysql.connector.Error as err:
            print("Non riesco a collegarmi al database")
            print(err)
            return None
