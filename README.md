# powerBI_writeDataToSQL
This repo presents a hack how power can be used to write categorized discrete data to SQL via R or Python

## Prerequisites
+ Python 3 installed and set to be ready (environment variables set correctly etc.) 
+ All necessary Python packages installed (use pip3 if packages are missing)
+ a SQL database with active login
+ write permissions on the intended tables
+ Microsoft Account and PowerBI Desktop installed


## PseudoCode - Steps
> Create a table or view from your base data

> Load table into PowerBI for display

> Load table with attributes that should be written to SQL

> Create slicer from attributes table

> create R or Python visual and use attribute from attributes table for "values"

> in the R/Python visual, write a script that connects to a database and writes the selected attribute pulled from the slicer
>> the script has to end with a pseudo plot, otherwise PowerBI will throw an error

## Example specifics
This example contains two different inputs - a *name* variable and a *statement* variable. 

### The complication
If more than 1 variable should be written, timing becomes an issue. Every time a slicer is changed (think: new value is selected) all scripts are executed. So if the variable *name* is selected, all scripts are triggered. This will cause *name* to be written correctly, but *statement* may not, as at the time of execution it was not set yet, so it will be empty when it is written. 

There are many ways to deal with this. 
For instance, at first execution, a dummy line could be created in the target SQL table, its ID retrieved and marked as "locked", to preven concurrent edits. Then, the scripts should only update this this very line. 

The approach chosen for the uploaded example is as follows: 
A dummy table holds a dummy line set to null. When a slicer is set and thus scripts are executed, they update the dummy line. Only when no NULL field is left, does the dummy line get written to the final target table. Concurrent users were not considered for the purpose of the example. 

### Known issues
python specific packages may not work once the report is published. This may depend on the set up of your environment. 
Based on research, R may be a better choice if the report is to be published onlne. 
