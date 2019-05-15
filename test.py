import xml.etree.cElementTree as et
import pandas as pd


def getvalueofnode(node):
    """ return node text or None """
    return node.text if node is not None else None


def main():
    """ main """
    parsed_xml = et.parse("text.xml")
    dfcols = ['name', 'email', 'phone', 'street']
    df_xml = pd.DataFrame(columns=dfcols)

    for node in parsed_xml.getroot():
        name = node.attrib.get('name')
        email = node.find('email')
        phone = node.find('phone')
        street = node.find('address/street')

        df_xml = df_xml.append(
            pd.Series([name, getvalueofnode(email), getvalueofnode(phone),
                       getvalueofnode(street)], index=dfcols),
            ignore_index=True)

    print(df_xml)


main()

class XML2DataFrame():

    def __init__(self, xml_data):
        self.tree = et.parse(xml_data)
        self.root = self.tree.getroot()

