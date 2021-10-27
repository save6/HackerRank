import sys
import xml.etree.ElementTree as etree

count = 0

def get_attr_number(node):
    global count
    count += len(node.attrib)
    
    for child in node:
        get_attr_number(child)
        
    return count

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))