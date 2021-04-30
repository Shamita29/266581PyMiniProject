import pickle
import os


class student(object):
    def __int__(s):
        s.roll=0
        s.name=""
        s.score=0

    def add_rec(s):
        s.roll=int(input("Enter roll no "))
        s.name=input("Enter name ")
        s.name=s.name.upper()
        s.score=float(input("Enter per "))
        
    def disp_rec(s):
        print("roll ",s.roll)
        print("name ",s.name)
        print("score ",s.score)

    def display_rec(s):
        print("%-10s"%s.roll,"%-20s"%s.name,"%-10s"%s.score)
            


def write_record():
    try:
        rec=student()
        file=open("stud.txt","ab")
        rec.add_rec()
        pickle.dump(rec,file)
        file.close()
        print("Record added in file")
        input("Press any key to cont ....")
    except:
        pass


def display_all():
    os.system("cls")
    print(40*"=")
    print("\n             Student Records\n")
    print(40*"=")
    try:
        file=open("stud.txt","rb")
        while True:
            rec=pickle.load(file)
            rec.display_rec()
            
            
    except EOFError:
        file.close()
        print(40*"=")
        input("Press any key to cont ....")
    except IOError:
        print("file could not be opened")
    
        
def search_name():
    os.system("cls")
    try:
        z=0
        n=input("Enter name to search ")
        file=open("stud.txt","rb")
        while True:
            rec=pickle.load(file)
            #print(rec.roll)
            if(rec.name==n.upper()):
                z=1
                rec.disp_rec()
                break
    except EOFError:
        file.close()
        if(z==0):
            print("record is not present")
        
    except IOError:
        print("file could not be opened")   
    input("Press any key to cont ....")    


def delete_roll():
    os.system("cls")
    z=0
    try:
        n=int(input("Enter roll no to delete "))
        file=open("stud.dat","rb")
        temp=open("temp.dat","wb")
        while True:
            rec=pickle.load(file)
            if(rec.roll==n):
                z=1
                print("record to delete found and details are")
                rec.disp_rec()
            else:
                pickle.dump(rec,temp)

    except EOFError:
        file.close()
        temp.close()
        if(z==0):
            print("Record not found")
    except IOError:
        print("File could not be opened")

    os.remove("stud.dat")
    os.rename("temp.dat","stud.dat")
    input("Press any key to cont ....")



while True:
    os.system("cls")
    print(40*"=")
    print("""            Main Menu
            ---------

           1. Add recod
           2. display all records
           3. search by name
           4. delete by rollno
           5. exit
    """)
    print(40*"=")
    ch=int(input("Enter your choice "))
    print(40*"=")
    if(ch==1):
        write_record()
    elif(ch==2):
        display_all()
    elif(ch==3):
        search_name()
    elif(ch==4):
        delete_roll()
    elif(ch==5):
        print("End")
        break
    else:
        print("Invalid choice")