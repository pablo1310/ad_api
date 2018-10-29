import subprocess, json

def find_spn(name):
    ps_command = "setspn -Q {}".format(name)
    process = subprocess.Popen(["powershell", ps_command], stdout=subprocess.PIPE, encoding="UTF-8")
    out = process.communicate()[0]

    #converting output to list
    out_list = out.splitlines()
    out_list = [line.strip("\t") for line in out_list]
    if (out_list[-1]) == 'Existing SPN found!':
        #extracting account name from list
        extract_account = out_list[1].split(",")
        extract_account = [ elem.strip("CN=|DC=") for elem in extract_account]

        #getting final return
        respons_to_api = {"account": extract_account[0], "spns": out_list[2:-2]}
        return respons_to_api
    else:
        return "Not found", 404

print(find_spn("HTTP/otherservertserver.labo.local"))