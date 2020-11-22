import xml.etree.ElementTree as ET
import numpy as np
import json
import os

class GenJSON:

    def __init__(self, xml_path, target_path = None):
        self.xml_path = xml_path
        self.target_path = os.getcwd() if not target_path else target_path
        self.target_file = ''.join(os.path.split(xml_path)[-1].partition('.')[:2] + ('json',))
        self.xml_tree = ET.parse(self.xml_path)
        self.root = self.xml_tree.getroot()

    def xml_to_json(self, root = None):
        if not root:
            root = self.root
        xml_els = root.getchildren()
        ## Create a dictionary with tag as a key and storing space as dict or list
        js = {root.tag: dict() if np.logical_or(len(xml_els)<=1,len(set([el.tag for el in xml_els]))!=1) else []}
        ## Recursive scan
        if xml_els:
            for el in xml_els:
                if el.getchildren():
                    if isinstance(js[root.tag],dict):
                        js[root.tag].update(self.xml_to_json(el))
                    else:
                        js[root.tag].append(self.xml_to_json(el))
                else:
                    if isinstance(js[root.tag], dict):
                        js[root.tag].update({el.tag: el.text})
                    else:
                        js[root.tag].append({el.tag: el.text})
        ## Get Attributes
        if root.attrib:
            if isinstance(js[root.tag],dict):
                js[root.tag].update({k:v for k,v in root.attrib.items()})
            else:
                js[root.tag].append({k:v for k,v in root.attrib.items()})

        return js

    def gen_json(self):
        with open(os.path.join(self.target_path,self.target_file), 'w') as f:
            f.write(json.dumps(self.xml_to_json()))
