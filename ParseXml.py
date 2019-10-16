# -*- coding:utf-8  -*-
from lxml import etree


class ParseXml(object):
    def __init__(self, config):
        parser = etree.XMLParser(remove_blank_text=True)
        self.root = etree.XML(config, parser)

    def addData(self, xpath, data, **kwargs):
        rowData = self.root.xpath(xpath, **kwargs)
        if not len(rowData) == 1:
            return False
        rowData[0].append(etree.Element('Param'))
        last = len(rowData[0]) - 1
        for k, v in data.items():
            rowData[0][last].attrib[k] = v
        return True

    def deleteData(self, xpath, **kwargs):
        rowData = self.root.xpath(xpath, **kwargs)
        if not len(rowData) == 1:
            return False
        rowData[0].getparent().remove(rowData[0])
        return True

    def editData(self, xpath, data, **kwargs):
        rowData = self.root.xpath(xpath, **kwargs)
        if not len(rowData) == 1:
            return False
        for k, v in data.items():
            rowData[0].attrib[k] = v
        return True

    def findData(self, xpath, **kwargs):
        rowData = self.root.xpath(xpath, **kwargs)
        return rowData

    def findValue(self, xpath, key, value='value'):
        rowData = self.root.xpath(xpath, name=key)
        result = rowData[0].attrib.get(value, '')
        return result

    def saveFile(self):
        return etree.tostring(self.root, encoding="utf-8", pretty_print=True)


if __name__ == '__main__':
    xmlString = """
    <Params>
        <LocalConfig>
            <Param key="ServiceIp" value="127.0.0.1" desc=""/>
            <Param key="ServicePort" value="1111" desc=""/>
            <Param key="DataPort" value="6655" desc=""/>
        </LocalConfig>
        <MysqlConfig>
            <Param key="user" value="root" desc="" />
            <Param key="password" value="" desc="" />
            <Param key="ip" value="localhost" desc="" />
            <Param key="port" value="3306" desc="" />
            <Param key="db" value="testtest" desc="" />
        </MysqlConfig>
    </Params>
    """
    testParse = ParseXml(xmlString)
    string_1 = testParse.findData('//Params/LocalConfig/Param')
    print('findData1', string_1)
    string_2 = testParse.findData('//Param[@key=$name]', name='user')
    print('findData2', string_2, string_2[0].attrib['value'])
    string_3 = testParse.addData('//Params/LocalConfig', {'key': 'test', 'value': 'test', 'desc': 'test'})
    print('addData', string_3)
    string_4 = testParse.editData('//Params/LocalConfig/Param[@key=$name]',
                                  {'key': 'test', 'value': 'test', 'desc': 'test1'}, name='test')
    print('editData', string_4)
    string_5 = testParse.deleteData('//Param[@key=$name]', name='test')
    print('deleteData', string_5)
    string_6 = testParse.saveFile()
    print('saveData', string_6)
