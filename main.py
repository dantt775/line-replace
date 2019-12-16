import os

import test_file

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
NEW_DATE = '20191216'
STR_START = 27
STR_END = 35
FILES_PATH = '/home/marchi/Documents/files/'


def main():    
    file_iterator()
    test_file.check_files()
    

def file_iterator():
    print('getting files names from folder')
    for file in os.listdir(FILES_PATH):    
        file_path = os.path.join(FILES_PATH, file)             
        if os.path.isdir(file_path):
            continue
        line = get_line_from_file(file_path)    
        string_to_replace = get_string_to_replace(line)
        new_line = change_line(line, string_to_replace)        
        write_line_to_file(new_line,file_path)


    
def get_line_from_file(file_path):    
    my_file = os.path.join(THIS_FOLDER, file_path)
    f = open(my_file, "r")
    line = f.read()
    f.close
    return line

def get_string_to_replace(line):
    date_str = line[STR_START:STR_END]
    print(date_str+ ' will be changed to '+ NEW_DATE)
    
    return date_str

def change_line(line, string_to_replace):    
    new_line = line.replace(string_to_replace, NEW_DATE)    
    return new_line


def write_line_to_file(new_line, file_path):    
    my_file = os.path.join(THIS_FOLDER, file_path)
    f = open(my_file, "w")
    f.write(new_line)
    f.close()

if __name__=="__main__":
    main()