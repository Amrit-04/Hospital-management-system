import mysql.connector
from tabulate import tabulate
import random
conobj=mysql.connector.connect(host="localhost",user="root",password="amrit123")
if conobj.is_connected():
    print("database connection done successfully")
cur=conobj.cursor()
cur.execute("create database if not exists hospital")
cur.execute("use hospital")

def menu():
    createtables()
    while True:
        print('='*26,"CITY HOSPITAL MANAGEMENT",'='*26)
        print('\t\t\t1. Assign a Room')
        print('\t\t\t2. Book an Appointment')
        print('\t\t\t3. Exit')
        print('='*70)
        ch=int(input('Enter Your Choice:-'))
        if ch==1:
            menuroom()
        elif ch==2:
            menudoc()
        elif ch==3:
            break
        else:
            print('Invalid Input! Please enter a correct choice')

def createtables():
    cur.execute('create table if not exists `Pdetails`(\
        `PatientID` int(3) primary key,\
        `Name` varchar(30) not null,\
        `Age` int(3) not null,\
        `Phone Number` varchar(10) not null)')


    cur.execute('create table if not exists `Bdetails`(\
        `Bill_no` int(3) not null,\
        `PatientID` int(3) primary key,\
        `Check_in` date not null,\
        `Check_out` date not null,\
        `No_of_days` int(3) not null,\
        `No_of_rooms` int(2) not null,\
        `Room_type` varchar(20),\
        `Total` int(10))')


    cur.execute('create table if not exists `Doc_App`(\
        `PatientID` int(4) primary key,\
        `BillID` int(4) not null,\
        `Name` varchar(30),\
        `Age` int(3) not null,\
        `TDate` date not null,\
        `Mobile Number` varchar(10) not null,\
        `Type of doc` varchar(20) not null,\
        `Total` int(10))')

    conobj.commit()
    print("Tables created successfully")


def menuroom():
    while True:
        print('='*26,'CITY HOSPITAL MANAGEMENT','='*26)
        print('\t\t\t1. Register New Patient')
        print('\t\t\t2. Selected Patients Details')
        print('\t\t\t3. All Patirnt Deatils')
        print('\t\t\t4. All Patient Bill Deatails')
        print('\t\t\t5. Exit')
        ch=int(input("Enter Your Choice:-"))
        if ch==1:
            RNP()
        elif ch==2:
            SPD()
        elif ch==3:
            PD()
        elif ch==4:
            APBD()
        elif ch==5:
            break
        else:
            print("PLEASE ENTER A VALID INPUT")



def RNP():
    try:
        pid = random.randint(1, 2000)
        print("Patient ID:",pid)
        name = input("Name: ")
        age = int(input("Age: "))
        pno = input("Mobile Number: ")
        confirm = input(("Do you want to confirm(y/n): "))
        if confirm == "y":
            query = "insert into Pdetails values ('{}','{}','{}','{}')".format(pid, name, age, pno)
            cur.execute(query)
            conobj.commit()
            print("Patient registered sucessfully!!")
            return reg()
        else:
            return reg()
    except Exception as e:
        print(e)


def reg():
    try:
        bno = random.randint(500,1500)
        print('='*26, 'ROOM ASSIGNMENT PAGE','='*26)
        cid = int(input("Please enter your Patient ID: "))
        cin = input("Check-in date(yyyy-mm-dd):")
        cout = input("Check-out date(yyyy-mm-dd):")
        nos = int(input("Enter the number of rooms: "))
        nom = int(input("Enter the number of days: "))
        room = int(input("SELECT THE ROOM TYPE:\n1.Basic:-[100 per night]\n2.Suite:-[500 per night]\n3.ICU:-[250 per night]\nYour Choice: "))
        if room == 1:
            r1 = "Basic"
            t = 100
        elif room == 2:
 
            r1 = "Suite"
            t = 500
        elif room == 3:
            r1 = "ICU"
            t = 250
        total = nos * t * nom + 5
        print("Total Bill: ", total,"--[(registration fee(5) included.]")
        print("Your Bill Number is:-", bno)
        confirm = input(("Do you want to confirm(y/n): "))
        if confirm == "y":
            query = "insert into Bdetails values ('{}','{}','{}','{}','{}','{}','{}','{}')".format(bno,cid, cin,cout, nom, nos, r1, total)
            cur.execute(query)
            conobj.commit()
            print("ASSIGNMENT SUCESSFULL!!")
            return menu()
        else:
            return menuroom()

    except Exception as e:
        print(e)

def PD():
    print('='*26, 'CITTY HOSPITAL MANAGEMENT', '='*26)
    query = 'select* from Pdetails'
    cur.execute(query)
    data = cur.fetchall()
    print(tabulate(data, headers=['PatientID', 'Name', 'Age','Mob.Number'], tablefmt='fancy_grid'))

def APBD():
    print('='*26, 'CITTY HOSPITAL MANAGEMENT', '='*26)
    query = 'select* from Bdetails'
    cur.execute(query)
    data = cur.fetchall()
    print(tabulate(data, headers=['Billno', 'PatientID', 'Check In', 'Check Out', 'No. Of Days','No. Of Rooms','Type Of Room','Total'], tablefmt='fancy_grid'))

def SPD():
    print('='*26, 'CITY HOSPITAL MANAGEMENT', '='*26)
    a = input("Press P to return or press Enter to continue: ")
    if a =="p":
        return menuroom()
    cid = int(input("Enter the Patient ID to see their data: "))
    query = "select* from Pdetails where PatientID=('{}')".format(cid)
    cur.execute(query)
    records = cur.fetchall()
    print(tabulate(records, headers=['PatientID', 'Name', 'Age','M.Number'], tablefmt="fancy_grid"))
    return SPD()

def menudoc():
    while True:
        print('='*26, 'CITTY HOSPITAL MANAGEMENT','='*26)
        print('\t\t\t1. Types of Doctors')
        print('\t\t\t2. Book an Appointment')
        print('\t\t\t3. Bill Details')
        print('\t\t\t4. Exit')
        ch = int(input('Enter Your Choice:-'))
        if ch == 1:
            tod()
        elif ch == 2:
            boa()
        elif ch == 3:
            bild()
        elif ch == 4:
            break
 
        else:
            print('PLEASE ENTER A VALID INPUT')

def tod():
    print('='*26, 'CITTY HOSPITAL MANAGEMENT','='*26)
    print('\t\t\tHere is the list of types of doctors in this Hospital:--')
    print('\t\t\t1. Dermatologist - Specializes in conditions involving the skin, hair, and nails. (Price - 10 per appointment)')
    print("\t\t\t2. Orthodontist - Speciality in Teeth and Jaws. (Price = 15 per appointment)")
    print('\t\t\t3. Neurologist - Speciality in diseases of the brain and spinal cord, peripheral nervesand muscles (Price - 25 per appointment')
    return menudoc()


def boa():
    try:
        bilno = random.randint(100,1500)
        print('='*26, 'ROOM ASSIGNMENT PAGE','='*26)
        cid = int(input("Please enter Patient ID: "))
        name = input("Name: ")
        age = int(input("Age: "))
        pno = input("Mobile Number: ")
        cdate= input("Enter Todays date(yyyy-mm-dd):")
        doctyp = int(input("SELECT THE DOCTOR TYPE:\n1.Dermatologist:-[10 per visit]\n2.Orthodontist:-[15 per visit]\n3.Neurologist:-[25 per visit]\nYour Choice: "))
        if doctyp == 1:
            r1 = "Dermatologist"
            t = 10
        elif doctyp == 2:
            r1 = "Orthodontist"
            t = 15
        elif doctyp == 3:
            r1 = "Neurologist"
            t = 25
        total = t+1
        print("Total Bill: ", total,"--[registration fee(1) included.]")
        print("Your Bill Number is:-", bilno)
        confirm = input(("Do you want to confirm(y/n): "))
        if confirm == "y":
            query = "insert into Doc_App values ('{}','{}','{}','{}','{}','{}','{}','{}')".format(cid, bilno,name,age,cdate,pno,r1,total)
            cur.execute(query)
            conobj.commit()
            print("APPOINTMENT SUCESSFULL!!")
            print("Please wait in the waiting area for your turn. Your name will be called.")
            return menu()
        else:
            return menudoc()

    except Exception as e:
        print(e)

def bild():
    print('='*26, 'CITY HOSPITAL MANAGEMENT', '='*26)
    a = input("Press P to return or press Enter to continue: ")
    if a =="p":
        return menuroom()
    cid = int(input("Enter the Patient ID to see their data: "))
    query = "select* from Doc_App where PatientID=('{}')".format(cid)
    cur.execute(query)
    records = cur.fetchall()
    print(tabulate(records, headers=['PatientID','BillNo.', 'Name', 'Age','M.Number','Doctor','Total'], tablefmt="fancy_grid"))
    return bild()
menu()




    

    
