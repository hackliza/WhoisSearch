from src.Logger.Logger import Logger


class ListReader:
    def get_white_list(self):
        Logger().info("Reading white list")
        return self.read_list("./config/white_list.txt")

    def get_black_list(self):
        Logger().info("Reading black list")
        return self.read_list("./config/black_list.txt")

    def read_list(self, path):
        with open(path, "r") as file:
            words = [line.strip("\n") for line in file.readlines()]
        return words
