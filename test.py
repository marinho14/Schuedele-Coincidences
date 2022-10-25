import unittest
import pytest
from string import ascii_lowercase



class Test_coincidences(unittest.TestCase):

    def __read_output(self,txt_file,real_output):
        f     = open(txt_file,'r') 
        txt   =  f.read()
        output     = txt.splitlines()
        f.close() 
        for count,i in enumerate(output):
            output[count]=''.join(sorted(i.lower())).replace(" ","")
        for count,i in enumerate(real_output):
            real_output[count]=''.join(sorted(i.lower())).replace(" ","")
        return output,real_output

    def test_Example_1(self):
        list_bool=[]
        real_output= ['ASTRID-RENE: 2','ASTRID-ANDRES: 3', 'RENE-ANDRES: 2']
        out_ex1,real_out_ex1= self.__read_output("txt_out_files\work_schedule_output.txt",real_output)
        for i in out_ex1:
            if i in real_out_ex1:
                list_bool.append(True)
            else:
                list_bool.append(False)
        self.assertTrue(all(p == True for p in list_bool))
        
    def test_Example_2(self):
        list_bool=[]
        real_output= ['RENE-ASTRID: 3']
        out_ex1,real_out_ex1= self.__read_output("txt_out_files\work_schedule_2_output.txt",real_output)
        for i in out_ex1:
            if i in real_out_ex1:
                list_bool.append(True)
            else:
                list_bool.append(False)
        self.assertTrue(all(p == True for p in list_bool))    

    def test_Example_3(self):
        list_bool=[]
        real_output= ['ASTRID-RENE: 2','ASTRID-ANDRES: 3', 'RENE-ANDRES: 2', 'JUAN-RENE: 2' , 'ASTRID-JUAN: 3', 'JUAN-ANDRES: 3', 'SOFIA-JUAN: 3', 'SOFIA-ANDRES :3', 'SOFIA-ASTRID: 3', 'SOFIA-RENE: 2']
        out_ex1,real_out_ex1= self.__read_output("txt_out_files\work_schedule_3_output.txt",real_output)
        for i in out_ex1:
            if i in real_out_ex1:
                list_bool.append(True)
            else:
                list_bool.append(False)
        self.assertTrue(all(p == True for p in list_bool)) 
        

if __name__ == '__main__':
    unittest.main()
