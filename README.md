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


## ACME CLASS
