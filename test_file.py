import os
from main import NEW_DATE, STR_START,STR_END, get_line_from_file


def check_files():    
    print('Checking files')
    for file in os.listdir("/home/marchi/Documents/files/"):    
        file_path = os.path.join("/home/marchi/Documents/files/", file)     
        if os.path.isdir(file_path):
            continue   
        line = get_line_from_file(file_path)                    
        check_line(line, file_path)
        
        
        
def check_line(line, file_path):    
    if(line[STR_START:STR_END] != NEW_DATE):
        print('Theres a problem with file '+ file_path)
    else:
        print(file_path + ' - Ok!')


if __name__=="__main__":
    check_files()