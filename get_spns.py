import subprocess
import json

def get_account_spns(domain, name):
    ps_command = 'setspn -L {}\\{} | ConvertTo-Json'.format(domain, name)
    #ps_command = f'setspn -L {domain}\\{name} | ConvertTo-Json'
    process = subprocess.Popen(["powershell", ps_command], stdout=subprocess.PIPE, encoding="UTF-8")
    out = process.communicate()[0]
    # converting output from subprocess.Open (which is string) to list
    out_list = json.loads(out)
    out_list = [elem.strip("\t") for elem in out_list]
    final = {"message": out_list[0], "spns": out_list[1:]}
    #back_to_api = json.dumps(final)
    return final



print(get_account_spns("labo","testspn"))