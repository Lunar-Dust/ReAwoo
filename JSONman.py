import json
import inspect
import os


class JSONMan(object):
    """
    Manage a supplied json file

    Parameters
    ----------
    file : string
        The name of the file to manage.
    cog_path: string, optional
        Determines folder the file is held in.
        Defaults to the filename of the calling function.
    """

    def __init__(self, file, cog_path):
        self.path = "data/{}/{}.json".format(cog_path, file)
        try:
            self.file = open(self.path, 'r+')
            self.data = json.load(self.file)
            self.file.close()
        except:
            if not os.path.exists("data/" + cog_path):
                os.makedirs("data/" + cog_path)
            open(self.path, 'w+').write("{}").close()
            self.data = {}

    def __call__(self):
        return self.data

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

    def save(self):
        """Saves the file being managed"""
        f = open(self.file.name, 'w')
        json.dump(self.data,
                  f,
                  indent=4)
        f.close()
        return True

    def __contains__(self, key):
        try:
            return bool(self.data[key])
        except:
            return False


def JMan(file, cog_path: str=""):
    if not cog_path:
        cog_path = inspect.stack()[1].filename
        cog_path = os.path.basename(cog_path).split('.')[0]
    return JSONMan(file, cog_path)
