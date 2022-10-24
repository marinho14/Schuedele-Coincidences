## Create a class that contains the schuedele of the Employs of acme

class ACME_schuedele: 
    
    ## This is the constructor of the function, read file and initialice some atributes
    def __init__(self, txt_file):
        ## In: 
        ## txt_file: This is the name/path of the file that contains the schuedele
        try:
            self.txt_file = txt_file
            self.f= open(self.txt_file,'r') 
            self.txt=  self.f.read()
        except FileNotFoundError:
            print("The 'docs' directory does not exist")
    
    ## This Privade method, create a atribute that contains a list whit the each line of the txt_file
    def __read_lines(self):
        lines = self.txt.splitlines()
        return lines
    
    ## This Private methof create two atributes that are lists that one contains the Employes and the other contains the schuedele
    def __separate_workers_split(self): 
        self.Employes         = []
        self.Schedules        = []
        Employes_lines   = self.__read_lines()
        for i in Employes_lines: 
            aux=i.replace(' ','').split("=")
            self.Employes.append(aux[0])
            self.Schedules.append(aux[1])
    
    ## This Private method separate in the different time splits all the schuedeles of the Employes
    def __separate_Schedules_split(self):
        self.Schedules_split = []
        self.Schedules_split = [item.split(',') for item in self.Schedules]

   ## This Private method iterate all element in a list, and comparate if each element is in a list in a list of lists
    def __func_iterate_list(self,new_list,index_list):
        Output=[]
        for i in range(index_list+1,len(self.Schedules_split)):
            acum=0
            for j in new_list:
                if(j in self.Schedules_split[i]):
                    acum+=1
            Output.append(str(self.Employes[index_list]+'-'+self.Employes[i]+': '+str(acum)))    
        return Output

    ## This method return the content of the txt file 
    def read_txt(self):
        print(self.txt)
        return self.txt

    ## This method return a list with the coincides of the Employes schuedeles
    def table_coincides(self):
        self.__separate_workers_split()
        self.__separate_Schedules_split()
        index=list(range(0,len(self.Schedules_split)))
        list_list= list(map(self.__func_iterate_list,self.Schedules_split,index))       
        self.coincided=[item for lista in list_list for item in lista]
        return self.coincided
    
    ## This method create a txt file with the coincides.
    def create_output_file(self):
        aux_file=self.txt_file.split("\\")
        print(aux_file)
        self.f1 = open("txt_out_files/"+aux_file[1]+"_output"+".txt", "w")
        for i in self.coincided:
            self.f1.write(i+"\n")
        print ("Txt with the Output response created in "+ self.txt_file+"_output"+".txt")
        