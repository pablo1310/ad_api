#Importing required modules

# for Flask-RESTful
from flask import Flask
from flask_restful import Api, Resource, reqparse

# in order to use powershell inside python
import subprocess, sys;

# I need "load" powershell output as json --> for Postman
import json

app = Flask(__name__)
api = Api(app)


class ADGroupManagement(Resource):
    def get(self):
        # keep it simple so name of group is hardcoded for now
        process = subprocess.check_output(["powershell","Get-ADGroupMember -Identity Administrators | select name,objectClass | ConvertTo-Json"]);
        output_json = json.loads(process)
        return {'members':output_json}


    def post(self, name):
        pass

    def put (self, name):
        pass

    def delete(self, name):
        pass


api.add_resource(ADGroupManagement, "/group")
app.run(debug=True)
