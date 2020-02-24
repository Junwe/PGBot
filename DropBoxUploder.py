import dropbox

class DropBoxManager:
    def __init__(self,token, filename,pathname):
        self.token = token
        self.fileName = filename
        self.pathName = pathname

    def UpLoadFile(self):
        dbx = dropbox.Dropbox(self.token,timeout=3000)
        with open(self.fileName, "rb") as f:
            dbx.files_upload(f.read(), self.pathName, mode=dropbox.files.WriteMode.overwrite)

    def GetFileLink(self):
        dbx = dropbox.Dropbox(self.token,timeout=3000)
        shared_URL = dbx.sharing_create_shared_link_with_settings(self.pathName).url
        modified_URL = shared_URL[:-1] + '1'
        return modified_URL
