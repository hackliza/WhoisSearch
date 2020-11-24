import os

import requests
from tqdm import tqdm

from whoissearch.logger import Logger


class Downloader:
    configuration = {
        "https://ftp.afrinic.net/dbase/afrinic.db.gz": "AFRINIC",
        "https://ftp.apnic.net/apnic/whois/apnic.db.inetnum.gz": "APNIC",
        "https://ftp.ripe.net/ripe/dbase/split/ripe.db.inetnum.gz": "RIPE"
    }

    def download_dbs(self, db_directory):
        os.makedirs(db_directory, exist_ok=True)

        for url, db_name in self.configuration.items():
            self.download_stardard_db(url, db_directory, db_name)

    def download_stardard_db(self, url, path, db_name):
        Logger().info("Downloading {db_name}".format(db_name=db_name))
        response = requests.get(url, stream=True)
        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024
        progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True)
        with open(os.path.join(path, db_name + ".db.gz"), 'wb') as file:
            for data in response.iter_content(block_size):
                progress_bar.update(len(data))
                file.write(data)
        progress_bar.close()
