#importing required modules

# for Flask-RESTful
from flask import Flask
from flask_restful import Api, Resource, reqparse

# in order to use powershell inside python
import subprocess, sys;

# I need "load" powershell output as json --> for Postman
import json

app = Flask(__name__)
api = Api(app)

# class ADGroupManagement(Resource):
#     def get(self):
#         process = subprocess.Popen(["powershell","Get-ADGroupMember -Identity Administrators | select name,objectClass | ConvertTo-Json"]);
#         result = process.communicate()[0]
#         #print(result)
#         #return jsonify ({'members':result })
#         return result

stores = [
    {
        "name":  "Domain Admins",
        "objectClass":  "group"
    },
    {
        "name":  "Enterprise Admins",
        "objectClass":  "group"
    },
    {
        "name":  "Administrator",
        "objectClass":  "user"
    }
]

result_string  = [{"name": "Dupa"}]

class ADGroupManagement(Resource):
    def get(self):
        #process = subprocess.Popen(["powershell","Get-ADGroupMember -Identity Administrators | select name,objectClass | ConvertTo-Json"]);
        #process = subprocess.Popen(["powershell","Get-ADGroupMember -Identity Administrators | select name,objectClass"]);
        #result = process.communicate()[0]
        #result = StringIO()
        #result_string = result.getvalue()
        #return result_string

        process = subprocess.check_output(["powershell","Get-ADGroupMember -Identity Administrators | select name,objectClass | ConvertTo-Json"]);
        #process = subprocess.Popen(["powershell","Get-ADGroupMember -Identity Administrators | select name,objectClass"]);
        #result = process.communicate()[0]
        #result = StringIO()
        #result_string = result.getvalue()
        output_json = json.loads(process)
        return {'members':output_json}, 200 # I dont need to specify


    def post(self, name):
        pass

    def put (self, name):
        pass

    def delete(self, name):
        pass


# process = subprocess.Popen(["powershell","Get-ADGroupMember -Identity Administrators"], stdout=sys.stdout);
# result = process.communicate()[0]
# print(result)

api.add_resource(ADGroupManagement, "/group")
app.run(debug=True)
