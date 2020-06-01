from xml.dom import minidom
import xml.etree.ElementTree as ET
from xml_file_services.base_settings import BaseSettings
import os

class SettingsWriter(BaseSettings):

    def write_file(self):
        print(self.get_file_path())
        if os.path.exists(self.get_file_path()) == False:
            root = ET.Element("settings")
            ET.SubElement(root, self.email_node_key, name=self.email_node_key).text= input("Provide an email: ")
            ET.SubElement(root, self.path_node_key, name=self.path_node_key).text= input("Files path: ")
            ET.SubElement(root, self.sender_email_node_key, name=self.sender_email_node_key).text= input("Sender email: ")
            ET.SubElement(root, self.sender_email_node_password_key, name=self.sender_email_node_password_key).text= input("Sender email password: ")

            tree = ET.ElementTree(root)
            tree.write(self.output_file_name)


