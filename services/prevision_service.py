from business.components.pollution import Pollution

class PrevisionsService:
    def __init__(self, nom_ville):
        print("Initialisation du service de prévisions")
        self._pollution_ville = Pollution(nom_ville)


    def previsions_indice(self):
        previsions = {}
        data = self._pollution_ville.get_aqi()
        for index in range(len(data)):
            previsions[index] = data[index]
        return previsions

    def previsions_pm2_5(self):
        previsions = {}
        data = self._pollution_ville.get_so2()
        for index in range(len(data)):
            previsions[index] = data[index]
        return previsions





