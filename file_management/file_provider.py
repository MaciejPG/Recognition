import os

class FileProvider:
    def get_files(self, path):
        files = []
        for dirpath, dirnames, filenames in os.walk(path):
            files.extend(filenames)
            return files