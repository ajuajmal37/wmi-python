import clr

clr.AddReference('System.Management')
clr.AddReference('System')
from System.Management import *
from System import *


class WMISearcher:
    def __init__(self, key, attr, objname=None):
        self.key = key
        self.attributes = attr
        self.objname = objname

    def get(self, key=None, value=None):
        obj_name = self.objname if self.objname is not None else self.key.split('_')[1]

        results = {obj_name: list()}

        try:
            query = "SELECT * FROM " + self.key + " WHERE " + key + " = " + "'"+ value +"'" if key is not None and value is not None else "SELECT * FROM " + self.key
            searcher = ManagementObjectSearcher("root\\CIMV2", query, )
            for res in searcher.Get():
                op = dict()
                for attr in self.attributes:
                    op[attr] = res[attr]
                results[obj_name].append(op)

            return results

        except Exception as ex:
            print(ex)
            return results

