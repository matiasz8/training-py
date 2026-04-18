"""
Example: SBOM Formats - JSON and XML
Demonstrates different SBOM serialization formats.
"""
import json
import xml.etree.ElementTree as ET


def main():
    """
    Create SBOM in JSON and XML formats.
    """
    component = {
        "name": "requests",
        "version": "2.31.0",
        "type": "library"
    }
    
    # JSON format
    json_sbom = json.dumps(component, indent=2)
    print("SBOM in JSON format:")
    print(json_sbom)
    
    # XML format
    root = ET.Element("sbom")
    comp = ET.SubElement(root, "component")
    ET.SubElement(comp, "name").text = component["name"]
    ET.SubElement(comp, "version").text = component["version"]
    ET.SubElement(comp, "type").text = component["type"]
    
    xml_str = ET.tostring(root, encoding='unicode')
    print("\nSBOM in XML format:")
    print(xml_str)


if __name__ == "__main__":
    main()
