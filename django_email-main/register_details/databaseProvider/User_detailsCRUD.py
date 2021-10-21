from django.db import connection
from register_details.views import *

def updatedetails(data):
    cursor = connection.cursor()
    
    try:
        updatedata = [data["Firstname"],data["Lastname"],data["Address"],data["City"],data["State"],data["Zip"],data["Company"],data["CompanyAddress"],data["Phoneno"],data["uid"]]
        cursor.execute('UPDATE public."Register_details" SET "Firstname"=%s, "Lastname"=%s, "Address"%s, "City"=%s, "State"=%s, "Zip"=%s, "Company"=%s, "CompanyAddress"=%s, "Phoneno"=%s WHERE public."Register_details"."uid" =%s;',updatedata)

        
        connection.commit()
        count = cursor.rowcount
        if count > 0:
            return True
    finally:
        cursor.close()
    return False

def insertdetails(data):
    cursor = connection.cursor()
    
    try:
        updatedata = [data["uid"],data["Firstname"],data["Lastname"],data["Address"],data["City"],data["State"],data["Zip"],data["Company"],data["CompanyAddress"],data["Phoneno"]]
        cursor.execute('INSERT INTO public."Register_details"("uid","Firstname", "Lastname", "Address", "City", "State", "Zip", "Company", "CompanyAddress", "Phoneno") VALUES ( %s,%s,%s, %s, %s, %s, %s, %s, %s, %s)',updatedata)
        
        connection.commit()
        count = cursor.rowcount
        if count > 0:
            return True
    finally:
        cursor.close()
    return False

def Validate_user_details(uuid):
    cursor = connection.cursor()
    try:
        cursor.execute('SELECT "uid" FROM public."Register_details" WHERE public."Register_details"."uid" = %s  ',[uuid])
        
        result_set = cursor.fetchall()
        for row in result_set:
            return row[0]
    finally:
        cursor.close()
    return None