import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BKrm3XW89icxpxb4OIodpgRGpwPEIqMsQwKBIU4f7v1LNIKqMWke051gEzyj1qkPVY4PLeROsu5wb0w6Xo8qgB_MLniNcQ5W3Zt1Djo3OdiyQCMyHtvpW0tbijx2tAKUmA2h5dnMlf0'
    transferData = TransferData(access_token)

    file_from = 'test.txt.txt'
    file_to = '/test_dropbox/test.txt'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print("uploading done!")

if __name__ == '__main__':
    main()
    