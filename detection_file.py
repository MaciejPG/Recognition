class DetectionFile:
    hasDetected = False
    path = ""
    file_name = ""

    def __init__(self, path, file_name):
        self.path = path
        self.file_name = file_name

    def get_full_name(self):
        return self.path + "\\" + self.file_name