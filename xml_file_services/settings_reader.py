from xml_file_services.base_settings import BaseSettings
import xml.etree.ElementTree as ET

class SettingsReader(BaseSettings):

    def get_tree(self):
        return ET.parse(self.get_file_path()).getroot()

    def get_value(self, node_key):
        result = ""
        settings = self.get_tree()
        result = settings.find(node_key).text
        return result