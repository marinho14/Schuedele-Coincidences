# Import the script that contains the class
import scheudele as sch

##Initialize an object, you need to pass the path file that contains the schedules
path= "txt_in_files\work_schedule.txt"
sch = sch.ACME_schuedele(path)

## You can use the metod read_text(), to read the content and display it.
text = sch.read_txt()

## The method table _coincidences returns in a list the schedules coincides of the Employes
coincidences = sch.table_coincides()
print(coincidences)

## The last method you can use, is a method that creates an txt file with the Output.
sch.create_output_file()