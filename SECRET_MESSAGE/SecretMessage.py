import os

def rename_files():

    # get file names
    file_list = os.listdir("/Users/johnnyboy9793/UDACITY_FULLSTACK/SECRET_MESSAGE/prank")

    #print (file_list)
    saved_path = os.getcwd()
    print(file_list)
    print("current working directory: " +saved_path)
    os.chdir("/Users/johnnyboy9793/UDACITY_FULLSTACK/SECRET_MESSAGE/prank")
    
    #for each file, rename
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)

rename_files()
