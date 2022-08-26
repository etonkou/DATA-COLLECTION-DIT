from .utils import Utils
import json
from bs4 import BeautifulSoup

BASE_URL = '../../COURSE/DATABASES/data-zIybdmYZoV4QSwgZkFtaB.html'


# BASE_URL = 'COURSE/DATABASES/data-zIybdmYZoV4QSwgZkFtaB.html'


class HtmlFactory(object):
    @classmethod
    def openFile(cls):
        with open(BASE_URL) as file:
            data = file.read()
            data = BeautifulSoup(data,'html.parser')
            file.close()
        return data

    @classmethod
    def getRows(cls):
        data = cls.openFile()
        rows = data.find_all('tr')
        return rows[1:]

    @classmethod
    def getRecord(cls):
        lines =[]
        data = cls.getRows()
        for line in data:
            datas = line.find_all('td')
            myRecord = {
                'Name':datas[0].getText(),
                'Phone':datas[1].getText(),
                'Email':datas[2].getText(),
                'LatLon':datas[3].getText(),
                'Salary':datas[4].getText(),
                'Age':datas[5].getText()
            }
            lines.append(myRecord)
        return lines


    @classmethod
    def main(cls):
        data = cls.openFile()
        data = cls.getRows()
        data = cls.getRecord()
        return data

