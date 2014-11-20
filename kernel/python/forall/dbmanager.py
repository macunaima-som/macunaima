
import os
from pymongo import MongoClient
import time
import uuid
import web

# Global variables
import os
here = os.path.dirname(__file__)
filedir = os.path.join(here, 'static/pub') # File storage directory

class DBManager():
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.nics
        self.collection = self.db.multimedia

    def find(self, search_parameters = None):
        return list(self.collection.find( search_parameters ).sort("timestamp", -1))

    def insert(self, file_pointer, metadata):
        id = uuid.uuid4().hex

        if file_pointer is not None:
            filepath=file_pointer.filename.replace('\\','/')
            filename=filepath.split('/')[-1]
            filename = id+filename
            fout = open(os.path.abspath(
os.path.join(filedir, filename)) ,'w')
            fout.write(file_pointer.file.read())
            fout.close()
        else:
            return False

        if 'TITLE' not in metadata.keys() or\
                metadata['TITLE'] == '':
            metadata['TITLE'] = time.strftime("%c")

        if 'AUTHOR' not in metadata.keys() or\
                metadata['AUTHOR'] == '': 
            metadata['AUTHOR'] = "Anonymous"

        for k in metadata.keys():
            if metadata[k] == "":
                del metadata[k]

        datagram = dict()
        datagram["_id"] = id
        datagram["filename"] = filename
        datagram["timestamp"] = time.time()
        datagram["metadata"] = metadata

        print datagram
        
        self.collection.insert(datagram)

        return id

    def delete(self, id, filename = None):
        if filename is None:
            filename = self.find({ '_id' : id})[0]['filename']

        self.collection.remove({ "_id": id })
        os.remove(os.path.abspath(
os.path.join(filedir, filename)))
        return True

    def update(self, id, metadata):
        filename = self.find({ '_id' : id})[0]['filename']
        
        self.collection.update(
            { "_id": id },
            { "$set" :
            { "metadata": metadata }},
            upsert = True
            )


