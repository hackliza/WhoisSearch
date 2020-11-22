import gzip
import multiprocessing
import os

import requests

from src.Logger.Logger import Logger


class Downloader:
    configuration = {
        "https://ftp.afrinic.net/dbase/afrinic.db.gz": "afrinic.txt",
        "https://ftp.apnic.net/apnic/whois/apnic.db.inetnum.gz": "apnic.txt",
        "https://ftp.ripe.net/ripe/dbase/split/ripe.db.inetnum.gz": "ripe.txt"
    }

    directory = "./db"

    def download_dbs(self):
        Logger().info("Downloading databases")
        os.makedirs(self.directory, exist_ok=True)

        process_list = []
        for key, value in self.configuration.items():
            process = multiprocessing.Process(target=self.download_stardard_db, args=(key, self.directory, value))
            process_list.append(process)

        for p in process_list:
            p.start()

        for p in process_list:
            p.join()

    def download_stardard_db(self, url, path, name):
        compressed_data = requests.get(url)
        decompressed_data = gzip.decompress(compressed_data.content)
        with open(os.path.join(path, name), "wb") as file:
            file.write(decompressed_data)
