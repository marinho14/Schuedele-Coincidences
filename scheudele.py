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
            self.f.close() 
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

    ## This method only compare if one hour is greater or lesser
    def __hour_comparation(self,hour_1,hour_2):
        if((hour_1[0]>hour_2[0]) or (hour_1[0]==hour_2[0] and hour_1[1]>hour_2[1])or (hour_1[0]==hour_2[0] and hour_1[1]==hour_2[1])):
            return True
        return False
    
    ## This method verify if the Employes coincides in any tine
    def __verification_hour(self,h1,h2):
        cond_1 = (self.__hour_comparation(h2[0],h1[0]) and  self.__hour_comparation(h1[1],h2[1]))
        cond_2 = (self.__hour_comparation(h1[0],h2[0]) and  self.__hour_comparation(h2[1],h1[0]))
        cond_3 = (self.__hour_comparation(h2[1],h1[1]) and  self.__hour_comparation(h1[1],h2[0]))   
        if(cond_1 or cond_2 or cond_3):
            return True
        return False

   ## This Private method iterate all element in a list, and comparate if each hour is betwwen inside other
    def __func_iterate_list(self,new_list,index_list):
        Output=[]
        for i in range(index_list+1,len(self.Schedules_split)):
            acum=0
            for j in new_list:
                for k in self.Schedules_split[i]:
                    if(j[0:2]==k[0:2]):
                        schu   =list(map(lambda x: x.split(":"),j[2:len(j)].split('-')))
                        schu_2 =list(map(lambda x: x.split(":"),k[2:len(k)].split('-')))
                        schu   = [[int((j)) for j in i] for i in schu]
                        schu_2 = [[int((j)) for j in i] for i in schu_2]
                        if(self.__verification_hour(schu,schu_2)==True):
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
        aux_file=aux_file[1].split(".")
        self.f1 = open("txt_out_files/"+aux_file[0]+"_output"+".txt", "w")
        for i in self.coincided:
            self.f1.write(i+"\n")
        self.f1.close() 
        print ("Txt with the Output response created in "+ aux_file[0]+"_output"+".txt")

        