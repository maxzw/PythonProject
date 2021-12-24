import os.path
from datetime import datetime

class Logbook():
    def __init__(self, path, do_print = False, incl_time = False) -> None:
        self.output_path = path
        self.do_print = do_print
        self.incl_time = incl_time
        
        # removing file if exists
        if os.path.exists(self.output_path):
            print("LOGBOOK WARNING: File already exists, overwriting current file!")
            os.remove(self.output_path)

        # create new file
        file = open(self.output_path, 'x')
        file.close()


    def log(self, text, do_print=True):
        
        # print if required
        if self.do_print or do_print:
            print(text)

        # open file and write line
        file = open(self.output_path, 'a')

        # include date if required
        if self.incl_time:
            dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            text = str(dt) + "\t" + text
        file.write(text+"\n")
        
        file.close()