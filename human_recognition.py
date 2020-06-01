
from detection.detector import Detector
from file_management.file_provider import FileProvider
from detection_file import DetectionFile
from messaging.email_provider import EmailProvider
from xml_file_services.settings_writer import SettingsWriter
from xml_file_services.settings_reader import SettingsReader

writer = SettingsWriter()
writer.write_file()
reader = SettingsReader()
detector = Detector()
file_provider = FileProvider()

path = reader.get_value(reader.path_node_key)
files = file_provider.get_files(path)
files_with_detected_people = []

for file_name in files:
    file = DetectionFile(path, file_name)

    print(file.get_full_name())
    detector.run_detection(file)
    if file.hasDetected:
        files_with_detected_people.append(file.file_name)

message = ""
for file in files_with_detected_people:
    message = "\n" + message + file

if(message != ""):
    sender = EmailProvider()
    sender.send(
        message,
        reader.get_value(reader.email_node_key),
        reader.get_value(reader.sender_email_node_key),
        reader.get_value(reader.sender_email_node_password_key))



