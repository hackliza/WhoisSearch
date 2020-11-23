from whoissearch.logger import Logger


class Reader:
    def read_list(self, path):
        words = []
        if path is not None:
            Logger().info("Reading {path}".format(path=path))
            with open(path, "r") as file:
                words = [line.strip("\n") for line in file.readlines()]
        return words
