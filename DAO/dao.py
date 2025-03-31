import mysql.connector

from DAO.dbConnect import DBConnect
from voto.voto import Voto


#PROTOTIPO DI QUALSIASI DAO FAREMO:
class LibrettoDAO:

    def getAllVoti(self):
        """
        cnx = mysql.connector.connect( #CREO UNA CONNESSIONE
            user = "root",
            password = "bngh56ty",
            host = "127.0.0.1",
            database = "libretto"
        )
        """
        cnx = DBConnect.getConnection() #USO DIRETTAMENTE IL METODO DALLA CLASSE
        cursor = cnx.cursor(dictionary=True) #CREO UN CURSORE, DICO CHE I DATI VANNO INSERITI IN UN DIZIONARIO

        query = """select * from voti"""
        cursor.execute(query) #CHIEDO AL CURSORE DI ESEGUIRE LA QUERY, RESTITUISCE DEI DATI A CUI DEVO DARE UN NOME

        res = []
        for row in cursor: #STAMPO LE RIGHE DELLA TABELLA
            #materia = row["materia"]
            #punteggio = row["punteggio"]
            #lode = row["lode"]
            #data = row["data"]
            #v = Voto(materia, punteggio, data, lode)
            #res.append(v)
            if row["lode"] == False:
                res.append(Voto(row["materia"], row["punteggio"], row["data"].date(), False))
            else:
                res.append(Voto(row["materia"], row["punteggio"], row["data"].date(), True))


        cnx.close()
        return res

    def addVoto(self, voto:Voto):
        """
        cnx = mysql.connector.connect(user = "root",
                                      password = "bngh56ty",
                                      host = "127.0.0.1",
                                      database = "libretto")
        """
        cnx = DBConnect.getConnection()  # USO DIRETTAMENTE IL METODO DALLA CLASSE
        cursor = cnx.cursor()

        query = ("insert into" 
                 "voti{materia, punteggio, data, lode}"
                 "values (%s, %s, %s, %s)")

        cursor.execute(query, (voto.materia, voto.punteggio, voto.data, str(voto.lode)))
        cnx.commit() #METOOD CHE VA AD GGIORNARE IL DATABASE, DATO CHE LO STO MODIFICANDO
        cnx.close()
        return

    def hasVoto(self,voto:Voto):
        """
        cnx = mysql.connector.connect(user = "root",
                                      password = "bngh56ty",
                                      host = "127.0.0.1",
                                      database = "libretto")
        """
        cnx = DBConnect.getConnection()  # USO DIRETTAMENTE IL METODO DALLA CLASSE
        cursor = cnx.cursor()
        query = """select *
                    from voti v
                    where v.materia = %s"""
        cursor.execute(query, (voto.materia,))
        res = cursor.fetchall() #PERCHE' DEVO LEGGERE TUTTI I DATI DELLA TABELLA, ALTRIMENTI MI DA ERRORE
        return len(res) > 0



if __name__ == "__main__":
    mydao = LibrettoDAO() #CREO UNA ISTANZA
    mydao.getAllVoti()