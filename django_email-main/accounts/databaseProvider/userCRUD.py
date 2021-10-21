from django.db import connection

def Validate_user(email,password):
    cursor = connection.cursor()
    
    try:
        cursor.execute('SELECT "Email","IsActive","uid" FROM public."User" WHERE public."User"."Email" = %s and public."User"."Password"=%s ',[email,password])
        
        result_set = cursor.fetchall()
        for row in result_set:
            return {"Email":row[0],"IsActive":row[1],"uid":row[2]}
    finally:
        cursor.close()
    return None

def Register_user(email,password,otp):
    cursor = connection.cursor()
    
    try:
        cursor.execute('INSERT INTO public."User"("Email", "Password", otp,"IsActive")	VALUES (%s, %s, %s, %s); ',[email,password,otp,"0"])
        
        connection.commit()
        count = cursor.rowcount
        if count > 0:
            return True
        
    finally:
        cursor.close()
    return False

def Verify_user(email,otp):
    cursor = connection.cursor()
    
    try:
        cursor.execute('SELECT "Email" FROM public."User" WHERE public."User"."Email" = %s and public."User".otp=%s ',[email,otp])
        
        result_set = cursor.fetchall()
        for row in result_set:
            return True
    finally:
        cursor.close()
    return False

def Activate_user(email):
    cursor = connection.cursor()
    
    try:
        cursor.execute('UPDATE public."User" SET "IsActive"=%s WHERE public."User"."Email" = %s ',["1",email])
        
        connection.commit()
        count = cursor.rowcount
        if count > 0:
            return True
    finally:
        cursor.close()
    return False

def Check_user_already_register(email):
    cursor = connection.cursor()
    
    try:
        print("Check_user_already_register")
        cursor.execute('SELECT "Email" FROM public."User" WHERE public."User"."Email" = %s ',[email])
        
        result_set = cursor.fetchall()
        print(result_set)
        for row in result_set:
            return True
    finally:
        cursor.close()
    return False