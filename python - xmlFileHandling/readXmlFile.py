from xml.dom import minidom
https://mkyong.com/python/python-read-xml-file-dom-example/

doc = minidom.parse("")

# doc.getElementsByTagName returns NodeList
name = doc.getElementsByTagName("name")[0]
print(name.firstChild.data)