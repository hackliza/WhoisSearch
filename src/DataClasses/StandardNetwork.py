class StandardNetwork:
    def __init__(self, inetnum, netname, descr, country, admin_c, tech_c, remarks, notify, mnt_by, changed, status,
                 mnt_lower, created, last_modified, source, matched_word=""):
        self.inetnum = inetnum
        self.netname = netname
        self.descr = descr
        self.country = country
        self.admin_c = admin_c
        self.tech_c = tech_c
        self.remarks = remarks
        self.notify = notify
        self.mnt_by = mnt_by
        self.changed = changed
        self.status = status
        self.mnt_lower = mnt_lower
        self.created = created
        self.last_modified = last_modified
        self.source = source
        self.matched_word = matched_word

    def to_dict(self):
        return {
            "inetnum": self.inetnum,
            "netname": self.netname,
            "descr": self.descr,
            "country": self.country,
            "admin_c": self.admin_c,
            "tech_c": self.tech_c,
            "remarks": self.remarks,
            "notify": self.notify,
            "mnt_by": self.mnt_by,
            "changed": self.changed,
            "status": self.status,
            "mnt_lower": self.mnt_lower,
            "created": self.created,
            "last_modified": self.last_modified,
            "source": self.source,
            "matched_word": self.matched_word
        }

    def __iter__(self):
        return iter([self.inetnum, self.netname, self.descr, self.country, self.admin_c, self.tech_c, self.remarks,
                     self.notify, self.mnt_by, self.changed, self.status, self.mnt_lower, self.created,
                     self.last_modified, self.source, self.matched_word])
