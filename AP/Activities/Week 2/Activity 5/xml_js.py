import xml.etree.ElementTree as ET
from collections import defaultdict
import numpy as np
xml_tree = ET.parse('People.xml')
root = xml_tree.getroot()

def xml_to_json(root):
    xml_els = root.getchildren()
    ## Create a dictionary with tag as a key and storing space as dict or list
    js = {root.tag: dict() if np.logical_or(len(xml_els)<=1,len(set([el.tag for el in xml_els]))!=1) else []}
    ## Recursive scan
    if xml_els:
        for el in xml_els:
            if el.getchildren():
                if isinstance(js[root.tag],dict):
                    js[root.tag].update(xml_mk(el))
                else:
                    js[root.tag].append(xml_mk(el))
            else:
                if isinstance(js[root.tag], dict):
                    js[root.tag].update({el.tag: el.text})
                else:
                    js[root.tag].append({el.tag:el.text})
    ## Get Attributes
    if root.attrib:
        if isinstance(js[root.tag],dict):
            js[root.tag].update({k:v for k,v in root.attrib.items()})
        else:
            js[root.tag].append({k:v for k,v in root.attrib.items()})

    return js



