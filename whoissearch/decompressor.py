import gzip
import os
import shutil


class Decompressor:
    def decompress(self, path, name):
        decompressed_file = name.replace(".gz", ".txt")
        with gzip.open(os.path.join(path, name), 'rb') as file_in:
            with open(os.path.join(path, decompressed_file), 'wb') as file_out:
                shutil.copyfileobj(file_in, file_out)
        return decompressed_file
