from whoissearch.logger import Logger

from tqdm import tqdm


class StandardNetworkClassifier:
    def classify(self, data, white_list, black_list):
        Logger().info("Classifying data")
        white_matched_nets = self.get_white_list_match_blocks(data, white_list)
        matched_nets = self.get_black_list_matched_blocks(white_matched_nets, black_list)
        return matched_nets

    def get_white_list_match_blocks(self, data, white_list):
        Logger().info("\tObtaining matched network block")
        white_matched_nets = []
        for network in tqdm(data):
            for word in white_list:
                if self.is_in_list(word, network):
                    network.matched_word = word
                    white_matched_nets.append(network)
                    break
        return white_matched_nets

    def is_in_list(self, word, network):
        return word.lower() in network.descr.lower() or word.lower() in network.netname.lower()

    def get_black_list_matched_blocks(self, white_matched_nets, black_list):
        if not black_list:
            return white_matched_nets

        Logger().info("\tDiscarding black listed network block")
        matched_nets = []
        for network in tqdm(white_matched_nets):
            if not self.is_black_list_word_in_block(network, black_list):
                matched_nets.append(network)
        return matched_nets

    def is_black_list_word_in_block(self, network, black_list):
        for word in black_list:
            if self.is_in_list(word, network):
                return True
        return False
