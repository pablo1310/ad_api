import subprocess, json
from helper_methods import outcome_to_list

def create_spn(name,account):
    ps_command = "setspn -D {} {}".format(name, account)
    process = subprocess.Popen(["powershell", ps_command], stdout=subprocess.PIPE,stderr=subprocess.PIPE, encoding="UTF-8")
    out,err = process.communicate()
    if process.returncode == 1:
        back_to_api = outcome_to_list(err)
        return {"message":back_to_api[-1]}

    else:
        back_to_api = outcome_to_list(out)
        print(back_to_api)
        return {"message": back_to_api[-1]}


print(create_spn("WSMAN/createspns.labo.local", "testspn"))