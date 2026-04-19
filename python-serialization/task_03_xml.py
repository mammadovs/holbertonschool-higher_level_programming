#!/usr/bin/python3
"""
Module for serializing and deserializing dictionaries using XML.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into an XML file.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Reads an XML file and reconstructs it into a Python dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        # Reconstruct dictionary from child elements
        return {child.tag: child.text for child in root}
    except FileNotFoundError:
        return None
    except Exception:
        return None
