import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


'''
csv_to_sql helper function
Adds quotes around TEXT data before putting it in INSERT INTO
List and type_list must be same length
'''
def stringify_vals(val_list, type_list):
    retstr = ""
    ctr = 0
    for i,j in zip(val_list,type_list):
        if j == "TEXT":
            retstr += "'" + i + "'"
        else:
            retstr += i
        ctr += 1
        if ctr < len(val_list):
            retstr += ","
    print retstr
    return retstr

'''
csv_to_sql helper function
Maps dict key (aka db field header) to type. Make sure you put in the types
in the correct order!
Keys and type_list must be same length
'''
def map_type(keys, type_list):
    retstr = ""
    ctr = 0
    for i,j in zip(keys, type_list):
        retstr += i + " " + j
        ctr += 1
        if ctr < len(keys):
            retstr += ","
    return retstr

'''
Builds a csv into a table in sqlite
'''
def csv_to_sql(table_name, path_to_csvfile, type_list):

    dictReader = csv.DictReader(open(path_to_csvfile))
    keys = dictReader.fieldnames
    print keys
    
    # collect keys
    if len(keys) != len(type_list):
        raise IndexError("Number of Types does not match number of Fields.")
    th = map_type(keys,type_list)
        
    # create table
    c.execute( "CREATE TABLE " + table_name + " (" + th + ");" )

    # inserting values
    for i in dictReader:
        values = []
        print i 
        for key in keys:
            val = i[key]
            values.append(val)
            
        if len(values) != len(type_list):
            raise IndexError("Number of Types does not match number of Values.")
        c_values = stringify_vals(values, type_list)
        print c_values
        c.execute("INSERT INTO " + table_name + " VALUES (" + c_values + ");" )
         


# RUNNNING .......
if __name__ == "__main__":
    db_name = "discobandit.db"
    db = sqlite3.connect(db_name)  #open if f exists, otherwise create
    c = db.cursor() #facilitate db ops
    
    csv_to_sql("peeps", "data/peeps.csv", ["TEXT", "INTEGER", "INTEGER"] )
    csv_to_sql("courses", "data/courses.csv", ["TEXT", "INTEGER", "INTEGER"] )
    
    db.commit() # save changes
    db.close() # close database

