"""Exemplo do livro capitulo 13."""
import xml.etree.ElementTree as et

tree = et.parse('arquivo.xml')
root = tree.getroot()
# for tag in tree:
#    print(tag)
for child in root:
    print(child.tag, child.text)

print(root.find('xNome').text)
