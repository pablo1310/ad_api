
def outcome_to_list(out):
    out_list = out.splitlines()
    out_list = [line.strip("\t") for line in out_list]
    return out_list