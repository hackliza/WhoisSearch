import os

from whoissearch.classifiers.standardnetworkclassifier import StandardNetworkClassifier
from whoissearch.downloader.downloader import Downloader
from whoissearch.parsers.standardparser import StandardParser
from whoissearch.reader.reader import Reader
from whoissearch.writer.writer import Writer


class Searcher:
    def search_networks(self):
        Downloader().download_dbs()
        db_names = os.listdir("./db")
        data = []
        for db in db_names:
            parsed_data = self.parse_db("./db", db)
            data += parsed_data

        list_reader = Reader()
        white_list = list_reader.get_white_list()
        black_list = list_reader.get_black_list()

        classified_data = StandardNetworkClassifier().classify(data, white_list, black_list)

        writer = Writer()
        writer.write_csv(classified_data)
        writer.write_json(classified_data)

    def parse_db(self, path, file_name):
        file = open(os.path.join(path, file_name), "r", encoding="cp850")
        parsed_data = StandardParser().parse(file)
        return parsed_data
