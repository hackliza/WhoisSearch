from tqdm import tqdm

from whoissearch.data.standardnetwork import StandardNetwork
from whoissearch.logger import Logger


class StandardParser:
    def parse(self, file, name):
        Logger().info("Parsing data from {filename}".format(filename=name))
        parsed_data = []
        block_count = self.get_block_count(file)
        file.seek(0)
        for block in tqdm(self.get_block(file), total=block_count):
            if self.is_network_block(block):
                inetnum = self.get_data("inetnum:", block)
                netname = self.get_data("netname:", block)
                descr = self.get_data("descr:", block)
                country = self.get_data("country:", block)
                admin_c = self.get_data("admin-c:", block)
                tech_c = self.get_data("tech-c:", block)
                remarks = self.get_data("remarks:", block)
                notify = self.get_data("notify:", block)
                mnt_by = self.get_data("mnt-by:", block)
                changed = self.get_data("changed:", block)
                status = self.get_data("status:", block)
                mnt_lower = self.get_data("mnt-lower:", block)
                created = self.get_data("created:", block)
                last_modified = self.get_data("last-modified:", block)
                source = self.get_data("source:", block)
                net = StandardNetwork(inetnum, netname, descr, country, admin_c, tech_c, remarks, notify, mnt_by,
                                      changed, status, mnt_lower, created, last_modified, source)
                parsed_data.append(net)
        return parsed_data

    def get_block(self, file):
        block = ""
        for line in file:
            block += line
            if self.is_separator(line):
                yield block
                block = ""

    def is_separator(self, line):
        return line == "\n"

    def is_network_block(self, block):
        return "inetnum:" in block

    def get_data(self, attribute, block):
        data = ""
        lines = block.split("\n")
        for line in lines:
            if line.startswith(attribute):
                data += line[16:] + "\n"
        return data[:-1]

    def get_block_count(self, file):
        block_count = 0
        for line in file:
            if self.is_separator(line):
                block_count += 1
        return block_count
