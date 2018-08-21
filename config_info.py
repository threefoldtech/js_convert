# global config module.  this is a very basic program so complex classes
# etc. really aren't needed

check_camel_case = True
action_camel_case = False

camel_case_file_name = 'camelcase_fns.txt'
exclude_camel_case_file_name = 'camelcase_exclude.txt'

camel_case_fn_list = []
exclude_camel_case_fn_list = []

def write_camel_case_file_list():
    with open(camel_case_file_name, "w") as f:
        for line in camel_case_fn_list:
            f.write("%s\n" % line)

def write_exclude_camel_case_file_list():
    with open(exclude_camel_case_file_name, "w") as f:
        for line in exclude_camel_case_fn_list:
            f.write("%s\n" % line)

def read_exclude_camel_case_file_list():
    try:
        with open(exclude_camel_case_file_name) as f:
            for line in f.readlines():
                exclude_camel_case_fn_list.append(line.strip())
    except IOError: # don't do anything if file doesn't exist
        pass

def read_camel_case_file_list():
    try:
        with open(camel_case_file_name) as f:
            for line in f.readlines():
                camel_case_fn_list.append(line.strip())
    except IOError: # don't do anything if file doesn't exist
        pass

def load():
    read_camel_case_file_list()
    read_exclude_camel_case_file_list()

def save():
    write_camel_case_file_list()
    write_exclude_camel_case_file_list()
