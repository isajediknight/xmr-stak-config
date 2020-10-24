def find_all(a_str, sub):
    """
    Returns the indexes of {sub} where they were found in {a_str}.  The values
    returned from this function should be made into a list() before they can
    be easily used.
    Last Update: 03/01/2017
    By: LB023593
    """

    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += 1

def download_webpage(fully_qualified_url,output_filename,output_absolute_path):
    """
    Saves a webpage to a file
    """
    from os import getcwd
    import urllib.request, urllib.parse, urllib.error
    urllib.request.urlretrieve(fully_qualified_url,output_absolute_path + output_filename)

def get_difficulty(filename_absolute_path):
    readfile = open(filename_absolute_path,'r')
    save_next_line = False
    difficulty = 999999999
    for line in readfile:

        if(save_next_line):
            try:
                start_location = line.find('<div class="value"><span>')
                stop_location = line.find('</')
                string_found = line[start_location+len('<div class="value"><span>'):stop_location].replace(',','')
                difficulty = int(string_found)
            except:
                difficulty = 999999999
            finally:
                break

        if(line.find('Network Difficulty') > -1):
            save_next_line = True

    return difficulty
            
