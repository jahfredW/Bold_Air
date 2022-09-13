from datetime import date

import psycopg2

class PollutionData():
    def __init__(self):

        self.params = {
            "host" : "localhost",
            "database" : "test2",
            "user" : "dev",
            "password" : "Farte512!",
            "port" : 5432
        }


    def get_all_departements(self):
        try:
            connection = psycopg2.connect(**self.params)
            cursor = connection.cursor()
            cursor.execute("SELECT * from departement")

            departements = cursor.fetchall()
            print(departements)

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if connection is not None:
                connection.close()
                print('connection à la BDD fermée')


    def get_id_ville(self, nom_ville: str):
        sql = "select id_ville from ville where nom = '{0}'".format(nom_ville)

        try:
            connection = psycopg2.connect(**self.params)
            cursor = connection.cursor()
            cursor.execute(sql)

            row = cursor.fetchall()
            connection.commit()
            cursor.close()

            return row

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if connection is not None:
                connection.close()


    def ville_exists(self, ville: str):
        sql = "SELECT id_ville from ville where nom like '%{}%'".format(ville)

        connection = None
        try:
            connection = psycopg2.connect(**self.params)
            cursor = connection.cursor()

            cursor.execute(sql)
            row = cursor.fetchone()

            connection.commit()
            cursor.close()

            if row is not None:
                return True
            return False

        except (Exception, psycopg2.DatabaseError) as error:
            print("error ville exits")
            print(error)

        finally:
            if connection is not None:
                connection.close()


    def ajout_pollution_ville(self,
                              aqi,
                              co,
                              no,
                              no2,
                              o3,
                              so2,
                              pm2_5,
                              pm10,
                              nh3,
                              day,
                              last_update,
                              id_ville):
        """
        Fonction qui permet d'ajouter un enregistrement dans la table prévision
        :param id_pollution: (nom du champ se suffit à la même)
        :param aqi: (nom du champ se suffit à la même)
        :param co: (nom du champ se suffit à la même)
        :param no: (nom du champ se suffit à la même)
        :param no2: (nom du champ se suffit à la même)
        :param o3: (nom du champ se suffit à la même)
        :param so2: (nom du champ se suffit à la même)
        :param pm2_5: idem
        :param pm_10: (nom du champ se suffit à la même)
        :param nh3: (nom du champ se suffit à la même)
        :param last_update
        """

        sql = """ INSERT INTO pollution ( aqi, co, no, no2, o3, so2, pm2_5, pm10, nh3, day, last_update, id_ville) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""

        connection = None
        try:
            # obtention de la connexion à la base de données
            connection = psycopg2.connect(**self.params)
            # create a new cursor
            cursor = connection.cursor()
            record_to_insert = (aqi, co, no,
                                no2, o3, so2, pm2_5, pm10,
                                nh3, day, date.today(), id_ville)
            cursor.execute(sql, record_to_insert)

            # commit the changes to the database
            connection.commit()
            # close communication with the database
            cursor.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print("Erreur ajout_prevision_ville:")
            print(error)
        finally:
            if connection is not None:
                connection.close()


    def get_last_update(self,nom_ville):
        """
        :param nom_ville:
        :return: retourne la date de dernière mise à jour d'une ville dans la table pollution.py
        """
        sql = "select last_update from pollution inner join ville on pollution.id_ville = ville.id_ville where ville.nom = '{0}' limit 1;".format(nom_ville)

        connection = None

        try:
            connection = psycopg2.connect(**self.params)
            cursor = connection.cursor()
            cursor.execute(sql, nom_ville)
            row = cursor.fetchone()[0]
            connection.commit()
            cursor.close()

            return row
        except (Exception, psycopg2.DatabaseError) as error:
            print('Error get_last_update : La ville n est pas encore enregistrée')
        finally:
            if connection is not None:
                connection.close()



    def delete_prevision_ville(self,nom_ville):
        """
        Supprime les prévisions météo pour une ville
        :param nom_ville: nom de la ville
        :return:
        """
        sql = f"DELETE FROM pollution WHERE id_ville in (select id_ville from ville where nom = '{nom_ville}');"

        connection = None
        try:
            # obtention de la connexion à la base de données
            connection = psycopg2.connect(**self.params)
            # create a new cursor
            cursor = connection.cursor()

            cursor.execute(sql, nom_ville)

            # commit the changes to the database
            connection.commit()
            # close communication with the database
            cursor.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print("Erreur delete_prevision_ville:")
            print(error)
        finally:
            if connection is not None:
                connection.close()


    def read_pollution_forecast(self,ville):
        sql = "select pollution.day,pollution.aqi, pollution.co, pollution.no, pollution.no2, pollution.o3, " \
              "pollution. so2, pollution.pm2_5, pollution.pm10, pollution.nh3 from pollution inner join ville " \
              "on pollution.id_ville = ville.id_ville where ville.nom = '{0}' order by pollution.day;".format(ville)

        connection = None
        try:
            connection = psycopg2.connect(**self.params)
            cursor = connection.cursor()
            cursor.execute(sql, ville)
            row = cursor.fetchall()
            connection.commit()
            cursor.close()

            return row

        except(Exception, psycopg2.DatabaseError) as error:
            print('Error read_pollution_forecast')
            print(error)
        finally:
            if connection is not None:
                connection.close()


    def get_all_ville(self):
        """
        :param nom_ville:
        :return: retourne la date de dernière mise à jour d'une ville dans la table pollution.py
        """
        sql = "SELECT nom from ville "

        connection = None

        try:
            connection = psycopg2.connect(**self.params)
            cursor = connection.cursor()
            cursor.execute(sql)
            row = cursor.fetchall()
            connection.commit()
            cursor.close()

            return row
        except (Exception, psycopg2.DatabaseError) as error:
            print('Error get_last_update')
            print(error)
        finally:
            if connection is not None:
                connection.close()

