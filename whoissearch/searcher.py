import os

from whoissearch.classifiers.standardnetworkclassifier import StandardNetworkClassifier
from whoissearch.decompressor import Decompressor
from whoissearch.downloader import Downloader
from whoissearch.parsers.standardparser import StandardParser
from whoissearch.reader import Reader
from whoissearch.writer import Writer


class Searcher:
    def search_networks(self, white_list_path, black_list_path):
        Downloader().download_dbs()

        db_names = os.listdir("./db")

        decompressor = Decompressor()

        data = []
        for db in db_names:
            if db.endswith(".db.gz"):
                decompressed_file = decompressor.decompress("./db", db)
                parsed_data = self.parse_db("./db", decompressed_file)
                data += parsed_data

        reader = Reader()
        white_list = reader.read_list(white_list_path)
        black_list = reader.read_list(black_list_path)

        classified_data = StandardNetworkClassifier().classify(data, white_list, black_list)

        writer = Writer()
        writer.write_csv(classified_data)
        writer.write_json(classified_data)

    def parse_db(self, path, file_name):
        file = open(os.path.join(path, file_name), "r", encoding="cp850")
        parsed_data = StandardParser().parse(file, file_name)
        file.close()
        return parsed_data
