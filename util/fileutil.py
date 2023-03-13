import os

def read(file_name) ->str:
    with open(os.path.join(os.getcwd(),"data",file_name), encoding="UTF-8") as f:
        return f.read()
