import csv
import json
import os

from whoissearch.logger import Logger


class Writer:
    def write_csv(self, data):
        Logger().info("Writing CSV")
        os.makedirs("./results", exist_ok=True)
        header = ["inetnum", "netname", "descr", "country", "admin_c", "tech_c", "remarks", "notify", "mnt_by",
                  "changed", "status", "mnt_lower", "created", "last_modified", "source", "matched_word"]
        data_to_write = [list(net) for net in data]
        with open("./results/result.csv", "w", encoding="utf8", newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=";", quotechar='"')
            writer.writerow(header)
            writer.writerows(data_to_write)

    def write_json(self, data):
        Logger().info("Writing JSON")
        results = [obj.to_dict() for obj in data]
        with open("./results/result.json", "w", encoding="utf8") as file:
            json.dump({"results": results}, file, indent=4)
