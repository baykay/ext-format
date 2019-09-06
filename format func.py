import os

os.system('clear')
path = input('[+] Enter full path to folder: ')

# getting the user path
def path_prompt():
    if os.path.exists(path):
        print('[*] Valid path')
        prompt_for_ext()
    else:
        print('[!] Invalid path')

# getting the file ext
def prompt_for_ext():
    ext = input('[+] Enter format for example(.mp4,.mp3,.jpg): ')
    if ext:
        chng_dir = os.chdir(path)
        for files in os.listdir(chng_dir):
            os.renames(files, files + ext)
    else:
        print('[!] Please state the file format')

    for renamed_files in os.listdir(os.getcwd()):
        print(renamed_files)

    print('\nCompleted Successfully!!!\n')

path_prompt()
