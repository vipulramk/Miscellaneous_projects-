# imports

import pandas as pd
import numpy as np
import re

outfiles= ['_Test[0SOC]_Proc[00DCIR_Charge]_Cell[4680_0SoC_Bike_AF_2].csv' ,
'_Test[0SOC]_Proc[00DCIR_Discharge]_Cell[4680_0SoC_Bike_AF_2].csv',
'_Test[0SOC]_Proc[10DCIR_Charge]_Cell[4680_0SoC_Bike_AF_2].csv',
'_Test[0SOC]_Proc[10DCIR_Discharge]_Cell[4680_0SoC_Bike_AF_2].csv',
'_Test[0SOC]_Proc[25DCIR_Charge]_Cell[4680_0SoC_Bike_AF_2].csv',
'_Test[0SOC]_Proc[25DCIR_Discharge]_Cell[4680_0SoC_Bike_AF_2].csv',
'_Test[0SOC]_Proc[45DCIR_Charge]_Cell[4680_0SoC_Bike_AF_2].csv',
'_Test[0SOC]_Proc[45DCIR_Discharge]_Cell[4680_0SoC_Bike_AF_2].csv',
'_Test[0SOC]_Proc[55DCIR_Charge]_Cell[4680_0SoC_Bike_AF_2].csv',
'_Test[0SOC]_Proc[55DCIR_Discharge]_Cell[4680_0SoC_Bike_AF_2].csv',
'_Test[0SOC]_Proc[Neg20DCIR_Charge]_Cell[4680_0SoC_Bike_AF_2].csv',
'_Test[0SOC]_Proc[Neg20DCIR_Discharge]_Cell[4680_0SoC_Bike_AF_2].csv',
'_Test[100SOC]_Proc[00DCIR_Charge]_Cell[4680_100SoC_Bike_AF_2].csv',
'_Test[100SOC]_Proc[00DCIR_Discharge]_Cell[4680_100SoC_Bike_AF_2].csv',
'_Test[100SOC]_Proc[10DCIR_Charge]_Cell[4680_100SoC_Bike_AF_2].csv',
'_Test[100SOC]_Proc[10DCIR_Discharge]_Cell[4680_100SoC_Bike_AF_2].csv',
'_Test[100SOC]_Proc[25DCIR_Charge]_Cell[4680_100SoC_Bike_AF_2].csv',
'_Test[100SOC]_Proc[25DCIR_Discharge]_Cell[4680_100SoC_Bike_AF_2].csv',
'_Test[100SOC]_Proc[45DCIR_Charge]_Cell[4680_100SoC_Bike_AF_2].csv',
'_Test[100SOC]_Proc[45DCIR_Discharge]_Cell[4680_100SoC_Bike_AF_2].csv',
'_Test[100SOC]_Proc[55DCIR_Charge]_Cell[4680_100SoC_Bike_AF_2].csv',
'_Test[100SOC]_Proc[55DCIR_Discharge]_Cell[4680_100SoC_Bike_AF_2].csv',
'_Test[100SOC]_Proc[Neg20DCIR_Charge]_Cell[4680_100SoC_Bike_AF_2].csv',
'_Test[100SOC]_Proc[Neg20DCIR_Discharge]_Cell[4680_100SoC_Bike_AF_2].csv',
'_Test[10SOC]_Proc[00DCIR_Charge]_Cell[4680_10SoC_Bike_AF_2].csv',
'_Test[10SOC]_Proc[00DCIR_Discharge]_Cell[4680_10SoC_Bike_AF_2].csv',
'_Test[10SOC]_Proc[10DCIR_Charge]_Cell[4680_10SoC_Bike_AF_2].csv',
'_Test[10SOC]_Proc[10DCIR_Discharge]_Cell[4680_10SoC_Bike_AF_2].csv',
'_Test[10SOC]_Proc[25DCIR_Charge]_Cell[4680_10SoC_Bike_AF_2].csv',
'_Test[10SOC]_Proc[25DCIR_Discharge]_Cell[4680_10SoC_Bike_AF_2].csv',
'_Test[10SOC]_Proc[45DCIR_Charge]_Cell[4680_10SoC_Bike_AF_2].csv',
'_Test[10SOC]_Proc[45DCIR_Discharge]_Cell[4680_10SoC_Bike_AF_2].csv',
'_Test[10SOC]_Proc[55DCIR_Charge]_Cell[4680_10SoC_Bike_AF_2].csv',
'_Test[10SOC]_Proc[55DCIR_Discharge]_Cell[4680_10SoC_Bike_AF_2].csv',
'_Test[10SOC]_Proc[Neg20DCIR_Charge]_Cell[4680_10SoC_Bike_AF_2].csv',
'_Test[10SOC]_Proc[Neg20DCIR_Discharge]_Cell[4680_10SoC_Bike_AF_2].csv',
'_Test[20SOC]_Proc[00DCIR_Charge]_Cell[4680_20SoC_Bike_AF_2].csv',
'_Test[20SOC]_Proc[00DCIR_Discharge]_Cell[4680_20SoC_Bike_AF_2].csv',
'_Test[20SOC]_Proc[10DCIR_Charge]_Cell[4680_20SoC_Bike_AF_2].csv',
'_Test[20SOC]_Proc[10DCIR_Discharge]_Cell[4680_20SoC_Bike_AF_2].csv',
'_Test[20SOC]_Proc[25DCIR_Charge]_Cell[4680_20SoC_Bike_AF_2].csv',
'_Test[20SOC]_Proc[25DCIR_Discharge]_Cell[4680_20SoC_Bike_AF_2].csv',
'_Test[20SOC]_Proc[45DCIR_Charge]_Cell[4680_20SoC_Bike_AF_2].csv',
'_Test[20SOC]_Proc[45DCIR_Discharge]_Cell[4680_20SoC_Bike_AF_2].csv',
'_Test[20SOC]_Proc[55DCIR_Charge]_Cell[4680_20SoC_Bike_AF_2].csv',
'_Test[20SOC]_Proc[55DCIR_Discharge]_Cell[4680_20SoC_Bike_AF_2].csv',
'_Test[20SOC]_Proc[Neg20DCIR_Charge]_Cell[4680_20SoC_Bike_AF_2].csv',
'_Test[20SOC]_Proc[Neg20DCIR_Discharge]_Cell[4680_20SoC_Bike_AF_2].csv',
'_Test[30SOC]_Proc[00DCIR_Charge]_Cell[4680_30SoC_Bike_AF_2].csv',
'_Test[30SOC]_Proc[00DCIR_Discharge]_Cell[4680_30SoC_Bike_AF_2].csv',
'_Test[30SOC]_Proc[10DCIR_Charge]_Cell[4680_30SoC_Bike_AF_2].csv',
'_Test[30SOC]_Proc[10DCIR_Discharge]_Cell[4680_30SoC_Bike_AF_2].csv',
'_Test[30SOC]_Proc[25DCIR_Charge]_Cell[4680_30SoC_Bike_AF_2].csv',
'_Test[30SOC]_Proc[25DCIR_Discharge]_Cell[4680_30SoC_Bike_AF_2].csv',
'_Test[30SOC]_Proc[45DCIR_Charge]_Cell[4680_30SoC_Bike_AF_2].csv',
'_Test[30SOC]_Proc[45DCIR_Discharge]_Cell[4680_30SoC_Bike_AF_2].csv',
'_Test[30SOC]_Proc[55DCIR_Charge]_Cell[4680_30SoC_Bike_AF_2].csv',
'_Test[30SOC]_Proc[55DCIR_Discharge]_Cell[4680_30SoC_Bike_AF_2].csv',
'_Test[30SOC]_Proc[Neg20DCIR_Charge]_Cell[4680_30SoC_Bike_AF_2].csv',
'_Test[30SOC]_Proc[Neg20DCIR_Discharge]_Cell[4680_30SoC_Bike_AF_2].csv',
'_Test[40SOC]_Proc[00DCIR_Charge]_Cell[4680_40SoC_Bike_AF_2].csv',
'_Test[40SOC]_Proc[00DCIR_Discharge]_Cell[4680_40SoC_Bike_AF_2].csv',
'_Test[40SOC]_Proc[10DCIR_Charge]_Cell[4680_40SoC_Bike_AF_2].csv',
'_Test[40SOC]_Proc[10DCIR_Discharge]_Cell[4680_40SoC_Bike_AF_2].csv',
'_Test[40SOC]_Proc[25DCIR_Charge]_Cell[4680_40SoC_Bike_AF_2].csv',
'_Test[40SOC]_Proc[25DCIR_Discharge]_Cell[4680_40SoC_Bike_AF_2].csv',
'_Test[40SOC]_Proc[45DCIR_Charge]_Cell[4680_40SoC_Bike_AF_2].csv',
'_Test[40SOC]_Proc[45DCIR_Discharge]_Cell[4680_40SoC_Bike_AF_2].csv',
'_Test[40SOC]_Proc[55DCIR_Charge]_Cell[4680_40SoC_Bike_AF_2].csv',
'_Test[40SOC]_Proc[55DCIR_Discharge]_Cell[4680_40SoC_Bike_AF_2].csv',
'_Test[40SOC]_Proc[Neg20DCIR_Charge]_Cell[4680_40SoC_Bike_AF_2].csv',
'_Test[40SOC]_Proc[Neg20DCIR_Discharge]_Cell[4680_40SoC_Bike_AF_2].csv',
'_Test[50SOC]_Proc[00DCIR_Charge]_Cell[4680_50SoC_Bike_AF_2].csv',
'_Test[50SOC]_Proc[00DCIR_Discharge]_Cell[4680_50SoC_Bike_AF_2].csv',
'_Test[50SOC]_Proc[10DCIR_Charge]_Cell[4680_50SoC_Bike_AF_2].csv',
'_Test[50SOC]_Proc[10DCIR_Discharge]_Cell[4680_50SoC_Bike_AF_2].csv',
'_Test[50SOC]_Proc[25DCIR_Charge]_Cell[4680_50SoC_Bike_AF_2].csv',
'_Test[50SOC]_Proc[25DCIR_Discharge]_Cell[4680_50SoC_Bike_AF_2].csv',
'_Test[50SOC]_Proc[45DCIR_Charge]_Cell[4680_50SoC_Bike_AF_2].csv',
'_Test[50SOC]_Proc[45DCIR_Discharge]_Cell[4680_50SoC_Bike_AF_2].csv',
'_Test[50SOC]_Proc[55DCIR_Charge]_Cell[4680_50SoC_Bike_AF_2].csv',
'_Test[50SOC]_Proc[55DCIR_Discharge]_Cell[4680_50SoC_Bike_AF_2].csv',
'_Test[50SOC]_Proc[Neg20DCIR_Charge]_Cell[4680_50SoC_Bike_AF_2].csv',
'_Test[50SOC]_Proc[Neg20DCIR_Discharge]_Cell[4680_50SoC_Bike_AF_2].csv',
'_Test[60SOC]_Proc[00DCIR_Charge]_Cell[4680_60SoC_Bike_AF_2].csv',
'_Test[60SOC]_Proc[00DCIR_Discharge]_Cell[4680_60SoC_Bike_AF_2].csv',
'_Test[60SOC]_Proc[10DCIR_Charge]_Cell[4680_60SoC_Bike_AF_2].csv',
'_Test[60SOC]_Proc[10DCIR_Discharge]_Cell[4680_60SoC_Bike_AF_2].csv',
'_Test[60SOC]_Proc[25DCIR_Charge]_Cell[4680_60SoC_Bike_AF_2].csv',
'_Test[60SOC]_Proc[25DCIR_Discharge]_Cell[4680_60SoC_Bike_AF_2].csv',
'_Test[60SOC]_Proc[45DCIR_Charge]_Cell[4680_60SoC_Bike_AF_2].csv',
'_Test[60SOC]_Proc[45DCIR_Discharge]_Cell[4680_60SoC_Bike_AF_2].csv',
'_Test[60SOC]_Proc[55DCIR_Charge]_Cell[4680_60SoC_Bike_AF_2].csv',
'_Test[60SOC]_Proc[55DCIR_Discharge]_Cell[4680_60SoC_Bike_AF_2].csv',
'_Test[60SOC]_Proc[Neg20DCIR_Charge]_Cell[4680_60SoC_Bike_AF_2].csv',
'_Test[60SOC]_Proc[Neg20DCIR_Discharge]_Cell[4680_60SoC_Bike_AF_2].csv',
'_Test[70SOC]_Proc[00DCIR_Charge]_Cell[4680_70SoC_Bike_AF_2].csv',
'_Test[70SOC]_Proc[00DCIR_Discharge]_Cell[4680_70SoC_Bike_AF_2].csv',
'_Test[70SOC]_Proc[10DCIR_Charge]_Cell[4680_70SoC_Bike_AF_2].csv',
'_Test[70SOC]_Proc[10DCIR_Discharge]_Cell[4680_70SoC_Bike_AF_2].csv',
'_Test[70SOC]_Proc[25DCIR_Charge]_Cell[4680_70SoC_Bike_AF_2].csv',
'_Test[70SOC]_Proc[25DCIR_Discharge]_Cell[4680_70SoC_Bike_AF_2].csv',
'_Test[70SOC]_Proc[45DCIR_Charge]_Cell[4680_70SoC_Bike_AF_2].csv',
'_Test[70SOC]_Proc[45DCIR_Discharge]_Cell[4680_70SoC_Bike_AF_2].csv',
'_Test[70SOC]_Proc[55DCIR_Charge]_Cell[4680_70SoC_Bike_AF_2].csv',
'_Test[70SOC]_Proc[55DCIR_Discharge]_Cell[4680_70SoC_Bike_AF_2].csv',
'_Test[70SOC]_Proc[Neg20DCIR_Charge]_Cell[4680_70SoC_Bike_AF_2].csv',
'_Test[70SOC]_Proc[Neg20DCIR_Discharge]_Cell[4680_70SoC_Bike_AF_2].csv',
'_Test[80SOC]_Proc[00DCIR_Charge]_Cell[4680_80SoC_Bike_AF_2].csv',
'_Test[80SOC]_Proc[00DCIR_Discharge]_Cell[4680_80SoC_Bike_AF_2].csv',
'_Test[80SOC]_Proc[10DCIR_Charge]_Cell[4680_80SoC_Bike_AF_2].csv',
'_Test[80SOC]_Proc[10DCIR_Discharge]_Cell[4680_80SoC_Bike_AF_2].csv',
'_Test[80SOC]_Proc[25DCIR_Charge]_Cell[4680_80SoC_Bike_AF_2].csv',
'_Test[80SOC]_Proc[25DCIR_Discharge]_Cell[4680_80SoC_Bike_AF_2].csv',
'_Test[80SOC]_Proc[45DCIR_Charge]_Cell[4680_80SoC_Bike_AF_2].csv',
'_Test[80SOC]_Proc[45DCIR_Discharge]_Cell[4680_80SoC_Bike_AF_2].csv',
'_Test[80SOC]_Proc[55DCIR_Charge]_Cell[4680_80SoC_Bike_AF_2].csv',
'_Test[80SOC]_Proc[55DCIR_Discharge]_Cell[4680_80SoC_Bike_AF_2].csv',
'_Test[80SOC]_Proc[Neg20DCIR_Charge]_Cell[4680_80SoC_Bike_AF_2].csv',
'_Test[80SOC]_Proc[Neg20DCIR_Discharge]_Cell[4680_80SoC_Bike_AF_2].csv',
'_Test[90SOC]_Proc[00DCIR_Charge]_Cell[4680_90SoC_Bike_AF_2].csv',
'_Test[90SOC]_Proc[00DCIR_Discharge]_Cell[4680_90SoC_Bike_AF_2].csv',
'_Test[90SOC]_Proc[10DCIR_Charge]_Cell[4680_90SoC_Bike_AF_2].csv',
'_Test[90SOC]_Proc[10DCIR_Discharge]_Cell[4680_90SoC_Bike_AF_2].csv',
'_Test[90SOC]_Proc[25DCIR_Charge]_Cell[4680_90SoC_Bike_AF_2].csv',
'_Test[90SOC]_Proc[25DCIR_Discharge]_Cell[4680_90SoC_Bike_AF_2].csv',
'_Test[90SOC]_Proc[45DCIR_Charge]_Cell[4680_90SoC_Bike_AF_2].csv',
'_Test[90SOC]_Proc[45DCIR_Discharge]_Cell[4680_90SoC_Bike_AF_2].csv',
'_Test[90SOC]_Proc[55DCIR_Charge]_Cell[4680_90SoC_Bike_AF_2].csv',
'_Test[90SOC]_Proc[55DCIR_Discharge]_Cell[4680_90SoC_Bike_AF_2].csv',
'_Test[90SOC]_Proc[Neg20DCIR_Charge]_Cell[4680_90SoC_Bike_AF_2].csv' ,
'_Test[90SOC]_Proc[Neg20DCIR_Discharge]_Cell[4680_90SoC_Bike_AF_2].csv' ]

results = {}

def give_file_names(name):
    filename = name
    match = re.search(r"_Test\[(.*?)\]_Proc\[(.*?)\]", filename)

    if match:
        soc = match.group(1)
        temp = match.group(2).split("_")[0]
        C_or_D = match.group(2).split("_")[1]
        return f"{soc}_{temp}_{C_or_D}"
    else:
        print("Filename pattern not found.")
        return None

        
def extract_dcir_value(name):
    db = pd.read_csv(name)
    v1 = db.Volts.iloc[0]
    db1= db[db.Step == 2]
    v3 = db1.Volts.iloc[-1]
    A = db1.Amps.iloc[0]
    DCIR_ohms = abs((v3-v1) /A)
    DCIR_mohms = DCIR_ohms*1000
    return DCIR_mohms

for i in outfiles:
    variable_name = give_file_names(i)
    if variable_name:
        results[variable_name] = extract_dcir_value(i)

print(results)

# Convert dictionary to a DataFrame
df = pd.DataFrame(list(results.items()), columns=['Condition', 'DCIR_mohms'])

# Save DataFrame to a CSV file
df.to_csv('DCIR_results.csv', index=False)