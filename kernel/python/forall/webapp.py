from pymongo import MongoClient
import uuid
import web
import time

import dbmanager
import text_to_dict

default_metadata = {'TITLE': '',
                    'AUTHOR': 'Anonymous',
                    'COLLECTION': 'ALL',
                    'DATE': '',
                    'PLACE': '',
                    'EQUIPMENT': '',
                    'CONTENT': ''}

class WebApp:
    def __init__(self):
        self.dbm = dbmanager.DBManager()
        
    def GET(self):
        return "I CAN WORK"
    
        
        x = web.input(id = "")
        if x.id == "":
            return self.show_dataset()
        else:
            return self.show_specific(x.id)

    def POST(self):
        x = web.input(myfile={}, metadata="", action="")

        if x.action == "insert":
            id = self.dbm.insert(x.myfile, text_to_dict.text_to_dict(x.metadata))
            return self.show_dataset()

        if x.action == "delete":
            self.dbm.delete(x.id, x.filename)
            return self.show_dataset()

        if x.action == "update":
            self.dbm.update(x.id, text_to_dict.text_to_dict(x.metadata))
            return self.show_specific(id = x.id)

    def show_dataset(self):
        dataset = self.dbm.find()
        webpage = web.template.frender('templates/database_app.html')
        metadata = default_metadata
        metadata['DATE'] = time.strftime("%c")
        return webpage(dataset=dataset, metadata=text_to_dict.dict_to_text(default_metadata))  

    def show_specific(self, id):
        dataset = self.dbm.find( { "_id": id } )
        webpage = web.template.frender('templates/view_app.html')
        return webpage(metadata=text_to_dict.dict_to_text(dataset[0]['metadata']),
                    id=dataset[0]['_id'], filename=dataset[0]['filename'])
