# coding: utf-8
import json,sys
import  xml.etree.ElementTree as ET

tree = ET.parse('test.xml')
root = tree.getroot()
root_tree=ET.ElementTree(root)

for  i in root.iter('dog'):# iter поиск по  имени тега
    i.set('name_new','!!!!!')
    print(i.attrib['name'])
    print(i.text.strip())
root_tree.write('test.xml')

#print(i) рекрусивность . из  функции вызвать в цикле саму функцию, чтобы пробежать по  например детей дерева.

#&#1089;&#1086;&#1073;&#1072;&#1082;&#1072;2


sys.exit(0)




py_obj = ['foo',{'bar':('baz', None, 1.0, 2)}]

s = json.dumps(py_obj)

print(s)

s1 = json.load(s)


