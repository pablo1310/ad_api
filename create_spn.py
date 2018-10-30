import subprocess, json
from helper_methods import outcome_to_list

def create_spn(name,account):
    ps_command = "setspn -S {} {}".format(name, account)
    process = subprocess.Popen(["powershell", ps_command], stdout=subprocess.PIPE,stderr=subprocess.PIPE, encoding="UTF-8")
    # even if duplicate then err = []
    out = process.communicate()[0]
    out_list = outcome_to_list(out)
    if process.returncode == 1:
        # [1] if duplicate
        if (out_list[-1]) == 'Duplicate SPN found, aborting operation!':
            return {"message": out_list[-1]}
        # [2] if not duplicate then account not found
        return "Not found", 404
    respond_to_api = {"account": account, "spn": out_list[3:]}
    return respond_to_api, 200


print(create_spn("WSMAN/abbaspns.labo.local", "testspn"))