import pandas
import pyodbc as db
import matplotlib.pyplot as plt
import time

time.sleep(5)


oCon = db.connect('Driver={ODBC Driver 13 for SQL Server}; Server=SERVER; Trusted_Connection=yes;Database=DB')
oCur1 = oCon.cursor()

sql0 = "select coalesce(count(*), 0) as count from z_sandbox.dbo.pbTestWrite_staging where categories is not null and writtenby is not null"
oCur1.execute(sql0)
rRow1 = oCur1.fetchone()

if '0_' in dataset.iloc[0,0]:
    sql2 = "update z_sandbox.dbo.pbTestWrite_staging set writtenby = null"
    oCur1.execute(sql2) 	
    oCon.commit()


if (rRow1[0]) == 0 and '0_' not in dataset.iloc[0,0]:
    variable = dataset.iloc[0,0]
    sQuery1 = f"""
                update z_sandbox.dbo.pbTestWrite_staging set writtenby = '{variable}' where id = 8
            
    """
    oCur1.execute(sQuery1) 	
    oCon.commit()

    oCon = db.connect('Driver={ODBC Driver 13 for SQL Server}; Server=analytics.danfoss.net; Trusted_Connection=yes;Database=analytics')
    oCur1 = oCon.cursor()

    sql0 = "select coalesce(count(*), 0) as count from z_sandbox.dbo.pbTestWrite_staging where categories is not null and writtenby is not null"
    oCur1.execute(sql0)
    rRow1 = oCur1.fetchone()

if rRow1[0] == 1:
    
    sql1a = "select categories, writtenby from z_sandbox.dbo.pbTestWrite_staging"
    oCur1.execute(sql1a) 	
    rRow1a = oCur1.fetchone()

    sCategory, sWritteby = rRow1a[0]. rRow1a[1]
    
    
    sql1b = f"select count(*) from z_sandbox.dbo.pbTestWrite where categories = {sCategory} and writtenby = {sWritteby}"
   
    
    oCur1.execute(sql1a) 	
    rRow1b = oCur1.fetchone()

    if rRow1b[0] == 0:
        sql1 = "insert into z_sandbox.dbo.pbTestWrite (categories, writtenby) select categories, writtenby from z_sandbox.dbo.pbTestWrite_staging"
        oCur1.execute(sql1)
        oCon.commit() 	

    sql2 = "update z_sandbox.dbo.pbTestWrite_staging set writtenby = null, categories = null"
    oCur1.execute(sql2) 	
    oCon.commit()


oCur1.close()
oCon.close()

plt.plot(1,1)
plt.show()