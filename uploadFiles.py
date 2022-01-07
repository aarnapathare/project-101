import dropbox
import os

class TransferData:
     def __init__(self, access_token):
        self.access_token = access_token
    
     def upload_file(self, file_from, file_to, local_path):
        for root, dirs, files in os.walk(file_from):
        
            relative_path = os.path.relpath(local_path, file_from)
            dropbox_path = os.path.join(file_to, relative_path)
    
        dbx = dropbox.Dropbox(self.access_token)

        with open(local_path, 'rb') as f:
            dbx.files_upload(f.read(), dropbox_path)

def main():
    access_token = 'access_token'
    transferData = TransferData(access_token)

    file_from = 'test.txt'
    file_to = '/test_dropbox/test.txt' 

    transferData.upload_file(file_from, file_to)

if  __name__ == '__main__':
    main()