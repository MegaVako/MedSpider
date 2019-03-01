#此程序可用于查询携程机票，查询需要指定出发日期、出发城市、目的城市！（模仿了12306火车订票查询程序）
import requests,json,os
from docopt import docopt
from prettytable import PrettyTable
from colorama import init,Fore

class TrainsCollection:
    header = 'Name Price'.split()
    def __init__(self,inputResult):
        self.inputResult = inputResult
    @property
    def plains(self):
        #航空公司的总表没有找到，但是常见航空公司也不是很多就暂时用这个dict{air_company}来收集！
        #如果strs没有查询成功，则会返回一个KeyError，表示此dict中未找到目标航空公司，则会用其英文代码显示！
        # air_company = {"G5":"华夏航空","9C":"春秋航空","MU":"东方航空","NS":"河北航空","HU":"海南航空","HO":"吉祥航空","CZ":"南方航空","FM":"上海航空","ZH":"深圳航空","MF":"厦门航空","CA":"中国国航","KN":"中国联航"}
        for item in self.inputResult:
            # try:
            #     strs = air_company[item['alc']]
            # except KeyError:
            #     strs = item['alc']
            price_data = [
            # Fore.BLUE + strs + Fore.RESET,
            Fore.BLUE + str(item['tag']) + Fore.RESET,
            '\n'.join([Fore.YELLOW + str(item['price'])]),
            # '\n'.join([Fore.YELLOW + item['dt'] + Fore.RESET,
            #            Fore.CYAN + item['at'] + Fore.RESET]),
            ]
            yield price_data

    def pretty_print(self):
        #PrettyTable（）用于在屏幕上将查询到的航班信息表逐行打印到终端
        pt = PrettyTable()
        pt._set_field_names(self.header)
        for price_data in self.plains:
            pt.add_row(price_data)
        print(pt)

def doit():
    with open('amazonResult.json') as f:
        inputResult = json.load(f)
    # airline_tickets = r.json()['fis']
    TrainsCollection(inputResult).pretty_print()

if __name__ == '__main__':
    doit()
