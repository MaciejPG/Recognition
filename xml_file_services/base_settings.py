from abc import ABC, abstractmethod
import os
import sys

class BaseSettings(ABC):
    output_file_name = "human_recognition.xml"
    email_node_key = "email"
    sender_email_node_key = "sender_email"
    sender_email_node_password_key = "password"
    path_node_key = "path"

    def get_file_path(self):
        return os.path.dirname(os.path.realpath(sys.argv[0])) +"\\" + self.output_file_name