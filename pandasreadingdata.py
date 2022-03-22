import numpy as np 
import numpy as nan # Numpy for remove nan value 
import pandas as pd
Dictheader = {}
Qr_prepdata = {}
Qr_readydata = {}
remove_patient_nan = []
patientdata_edit = [] 
array_patient_info = [[],[],[],[],[],[]]
array_patient_edit = [[],[],[],[],[],[]]

patient_data = pd.read_csv('/media/kornbotdev/8D60-165C/รายชื่อสำหรับ test ระบบ.csv')

listcolumns = list(patient_data.columns.values)
for i in range(0,len(listcolumns)):
         patientdata = patient_data.loc[:,listcolumns[i]].tolist()
         #print(patientdata[0],type(patientdata[0]))
         remove_patient_nan.append(patientdata)
#Convert nan to string to remove the nan 
for r in range(0,len(remove_patient_nan)):
             for k in range(1,len(remove_patient_nan[r])):
                      array_patient_info[r].append(str(remove_patient_nan[r][k]))
hn_number = array_patient_info[0]                     
#print(array_patient_info)
for r in range(0,len(array_patient_info)):
             for k in range(1,len(remove_patient_nan[r])):
                      array_patient_edit[r].append(str(remove_patient_nan[r][k]))
print(array_patient_edit)
for r in range(0,len(array_patient_edit)):
           Dictheader[listcolumns[r]] = array_patient_edit[r] #Getting the dictionary create inside the list 
print(Dictheader) 
Check_list = len(Dictheader.get(listcolumns[0])) 
for ir in range(0,Check_list):
          Patient_name = Dictheader.get(listcolumns[1])[ir] +"\t" +Dictheader.get(listcolumns[2])[ir]+"\t"+Dictheader.get(listcolumns[3])[ir]
          Qr_prepdata[Dictheader.get(listcolumns[0])[ir]] = [Patient_name,Dictheader.get(listcolumns[4])[ir],Dictheader.get(listcolumns[5])[ir]]
          
print(Qr_prepdata)
print(list(Qr_prepdata))
for id in list(Qr_prepdata): #getting the name of the patient list in the header 
      print(id)
      print(Qr_prepdata.get(id))