# Schuedele-Coincidences

## How to run the code? 

To run the code, copy and paste the following commands into your terminal, these commands vary if you are in a linux or windows environment.

### Windows

```shell
git clone https://github.com/marinho14/Schuedele-Coincidences
cd Schuedele-Coincidences
py main.py
```

### Linux

```shell
git clone https://github.com/marinho14/Schuedele-Coincidences
cd Schuedele-Coincidences
python main.py
```

After executing the code you should have an output like the following

```console
RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00- 21:00
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
['RENE-ASTRID: 2', 'RENE-ANDRES: 2', 'ASTRID-ANDRES: 3']
Txt with the Output response created in txt_in_files\work_schedule.txt_output.txt
```
At the end a text file with the matches will be created in the following folder, named after the same input file with "_output".

- [.txt Output files](txt_out_files)

## Variables that you can change

The script you need to change to input different input files is the file:

- [main.py](main.py)


By default all input files are located in the following folder,for a correct operation, it is recommended to put all the txt files inside this folder, if not, you must change the path variable that is mentioned below

- [.txt Input files](txt_in_files)

In this script you will find a line of code that defines the path of the file, if you want to enter another .txt input file, you just have to go to main.py and change this variable.



```python
    path= "txt_in_files\work_schedule_2.txt"
```

## Principal Idea
The main idea of ​​the solution is to make several iterations of comparisons, the idea is to compare each time slot of each employee, with the complete schedule of the rest of the employees, each time a SLOT coincides with a time slot of the other employee's schedule. one will be added to the counter that counts the comparisons between them.

<p align="center" > 
   <img src=Images/Explication.jpg>
</p>


To compare if two were at the same time in the office, first the day was compared, if the day coincided, it was proceeded to see if the hours coincided, for that different comparison conditions were generated between the hours of the employees

## ACME CLASS

For the solution of this exercise, a class was created that has several methods to calculate the coincidences of schedules between ACME employees. The class is in this script.

- [Class](scheudele.py)

Below is a class diagram of the solution, if you want to go into detail, please read the comments in the script, as they describe the function of each method and its use in the code

<p align="center" > 
   <img src=Images/Class.png>
</p>

## TESTS

To test the code, a Unittest was performed in python, the script is as follows:

- [Test](test.py)

In this script, the Test_coincidences class was created, a method was created to read the content of the [output files](txt_out_files) that are generated when running the [main.py](main.py) code, in addition to this method, 3 equal test methods were created to test the correct operation of this, the structure of the methods is as follows. 


```python

    def test_Example_n(self): ##You can replace n with the number of the test
        list_bool=[]
        real_output= ['ASTRID-RENE: 2','ASTRID-ANDRES: 3', 'RENE-ANDRES: 2'] ## Here you can write the right output.
        out_ex1,real_out_ex1= self.__read_output("path",real_output) ## Here the code read the output of the main.py
        for i in out_ex1:  ## Iterates the Out of the code to compare with the real output
            if i in real_out_ex1:
                list_bool.append(True)
            else:
                list_bool.append(False)
        self.assertTrue(all(p == True for p in list_bool)) ## If every match its ok the assert pass
```

When running the test script, an output like the following should be displayed on the screen.

```console
...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```