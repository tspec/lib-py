from itertools import groupby
import re

def extractSpecDeffromfile(filename: str, token: str) -> list:

    spec_list = []
    with open(filename,'r') as f_input:
        for currentline in f_input:
            if currentline.startswith(token):
                spec_list.append(currentline.strip().removeprefix(token).lower().strip().replace(' ','_'))

    return spec_list

def filterspecdefination(specdef: dict) -> dict:
    fun_dict = {}
    method_args = []
    for key, value in specdef.items():
        filter = re.findall('"([^"]*)"', value) #filter[0]  will be method remaininin args
        fun_dict[key] = filter
    return fun_dict

