from .utils import Utils
import requests
from bs4 import BeautifulSoup


PATH_URL = 'cours/cours-des-devises-contre-Franc-CFA-appliquer-aux-transferts'
URL = f'https://www.bceao.int/fr/{PATH_URL}'

class DeviseFactory(object):
    @classmethod
    def httpFetcher(cls, URL):
        with requests.Session() as session:
            result = session.get(URL)
            result = result.text
            return result

    @classmethod
    def scrapLink(cls, URL):
        return cls.httpFetcher(URL)

    @classmethod
    def souper(cls, URL):
        result = cls.scrapLink(URL)
        return BeautifulSoup(
            result,
            'html.parser')

    @classmethod
    def getBoxCourse(cls, URL=URL):
        soupering = cls.souper(URL)
        soupering = soupering \
            .find_all(attrs={
                'id': 'box_cours'})
        if soupering:
            table = soupering[0].table
            return table
        return None

    @classmethod
    def makeCurrencyList(cls, URL=URL):
        soupering = cls.getBoxCourse(URL)
        if soupering:
            tr = soupering.find_all('tr')
            factory = [
                item.find_all('td')
                for item in tr
            ][1:]
            factory = [
                {
                    'Devise': x.string.strip(),
                    'Achat': float(y.string.strip().replace(',', '.')),
                    'Vente': float(z.string.strip().replace(',', '.')),
                }
                for (x, y, z) in factory
            ]
            return factory
        return None

    @classmethod
    def save(cls, URL=URL, format=None):
        soupering = cls.makeCurrencyList(URL)
        if soupering:
            return soupering
        return None

    @classmethod
    def newEntry(cls, data):
        START = 1
        FINAL = 1000
        # data['RandomAmount'] = float(0)
        # data['XOF_>EUR'] = 0 #float(0)
        # data['XOF_>USD'] = 0 #float(0)
        # data['XOF_>JPY'] = 0 #float(0)
        data['RandomAmount'] = data['RandomAmount'].apply(lambda x: Utils.randomize(START, FINAL))
        data['XOF_>EUR'] = data['newEntry'] * data[0]['Vente']
        data['XOF_>USD'] = data['newEntry'] * data[1]['Vente']
        data['XOF_>JPY'] = data['newEntry'] * data[2]['Vente']
        return data

    @classmethod
    def conversionXOF(cls, currency1='EUR',currency2='US',currency3='JPY'):
        pass
        # data = cls.makeCurrencyList(URL)
        # if data
        #return data

    @classmethod
    def main(cls):
        data = cls.makeCurrencyList()
        #data = cls.newEntry(data)
        return data