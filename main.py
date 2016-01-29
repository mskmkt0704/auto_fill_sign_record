#!python
# coding=utf-8


import json, bs4


class SignRecod(object):
    """docstring for SignRecod"""
    def __init__(self):
        super(SignRecod, self).__init__()
        self._data = []

    def GetName(self):
        return self._data[1]

    def GetDate(self):
        return self._data[0]

    def GetSignInTime(self):
        return self._data[2]

    def GetSignOutTime(self):
        return self._data[3]

    def GetComment(self):
        if self._data.count < 5:
            return ''
        else:
            return self._data[4]

    def AppendData(self, data):
        self._data.append(data)

# load config
'''
fp = open("config.json","r")
configData = json.load(fp)
fp.close()
'''

#load html may access web
fp = open("E:\\autoexecel\\example.html","r")
soup = bs4.BeautifulSoup(fp.read())
fp.close()

trs = soup.find("table", class_="table table-bordered table-striped").tbody.find_all("tr")

SignRecods = []
for tr in trs:
    sr = SignRecod()
    SignRecods.append(sr)
    for td in tr:
        if isinstance(td, bs4.element.Tag):
            print td
            if td.string:
                sr.AppendData(td.string)
            else:
                sr.AppendData('')
