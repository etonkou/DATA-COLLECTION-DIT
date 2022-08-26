from libraries.utils import Utils
from libraries.csv import CsvFactory
from libraries.json import JsonFactory
from libraries.html import HtmlFactory
from libraries.devises import DeviseFactory # DataSouper, CurrencyScrapper # DeviceFactory

# Question4: Concatenation des 3 factories
def combine():
     dataList = []
     dataList.append(HtmlFactory.main())
     dataList.append(JsonFactory.main())
     dataList.append(CsvFactory.main())
     return dataList


if __name__ == '__main__':
     print(Utils.divider())
     print(CsvFactory.main())
     print(JsonFactory.main())

     # Recupration des donnees html sous forme de liste
     print('1- Recuperation des donnees de htlm\n')
     print(HtmlFactory.main())

     # Question4: Concatenation des 3 factories
     print(Utils.divider())
     print('4- Concatenation des donnees des 03 factory: CsvFactory, JsonFactory & HtmlFactory\n')
     print(combine())

     # Question5: Devises
     print(Utils.divider())
     print('5- Les Devises\n')

     print(DeviseFactory.main())

