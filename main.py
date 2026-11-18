from pathlib import Path
import os
import shutil
def create_folder():
    try:
        name=input("Please tell your folder name :- ")
        p=Path(name)
        p.mkdir()
        print("Folder created successfully")
    except Exception as err:
        print(f"sorry an error occured as {err}")

def read_file_folder():
    p=Path(" ")
    items=list(p.rglob('*'))
    for i ,v in enumerate(items):
        print(f"{i+1}: {v}")

def update_folder():
    try:
        read_file_folder()
        old_name=input("please tell which folder you want to update :- ")
        p=Path(old_name)
        if p.exists() and p.is_dir():
            new_name=input("please tell your new folder name:- ")
            new_p = Path(new_name)
            p.rename(new_p)
            print("your folder name is updated successfully")
        else:
            print("Sorry no such folder exist")
    except Exception as err:
        print(f"An error occured as {err}")
def delete_folder():
    try:
        read_file_folder()
        name=input("please tell which folder you want to delete:- ")
        p=Path(name)
        if p.exists() and p.is_dir():
            shutil.rmtree(p)
            print("folder deleted successfully")
        else:
            print("No such folder exist")
    except Exception as err:
        print(f"There was an error as{err}")

def create_file():
    try:
        read_file_folder()
        name=input("Enter your file name :-")
        p=Path(name)
        if not p.exists():
            with open(name,"w") as fs:
                data=input("Write whatever you want to write in this file :- ")
                fs.write(data)
            print("File created successfully")
        else:
            print("Sorry! File already exist")
    except Exception as err:
        print(f"There was an error as{err}")
def read_file():
    try:
        read_file_folder()
        name =input("Enter the file name:- ")
        p=Path(name)
        if p.exists() and p.is_file():
            with open(name,'r') as  fs:
                content=fs.read()
                print("Your file content is :-")
                print(content)
        else:
            print("No such file exist")
    except Exception as err:
        print(f"There was an error as{err}")
def update_file():
    try:
        read_file_folder()
        name=input("Enter file name :- ")
        p=Path(name)
        if p.exists() and p.is_file():
            print("options")
            print("1. Rename the file")
            print("2. Appending in the file")
            print("3. Overwriting the file content")
            choice=int(input("Tell your chice : "))
            if choice==1:
                new_name=input("Tell new name with extension: ")
                new_p = Path(new_name)
                if not new_p.exists():
                    p.rename(new_p)
                    print("File name successfully changed")
                else:
                    print("Sorry this name file is already exist")
            if choice==2:
                with open(name,'a') as fs:
                    data=input("Enter the text you want to append : ")
                    fs.write(" "+ data)
                print("File updated Successfully")
            if choice==3:
                with open(name,'w') as fs:
                    data=input("Enter the text you want to overwrite : ")
                    fs.write(data)
                print("File changed Successfully")
    except Exception as err:
        print(f"There was an error as{err}")

def delete_file():
    try:
        read_file_folder()
        name=input("Enter file name: ")
        p=Path(name)
        if p.exists and p.is_file():
            p.unlink()
            print("File deleted successfully")
        else:
            print("No such file exist")
    except Exception as err:
        print(f"There was an error as{err}")

while True:
    print("-----Options : -----")

    print("1. Create a folder")
    print("2. Read files and folders")
    print("3. Update the Folder")
    print("4. Delete the folder")
    print("5. Create a file")
    print("6. Read a file")
    print("7. Update a file")
    print("8. Delete a file")
    print("0. Exit")

    choice=int(input("Please Choose your input :- "))

    if choice==1:
        create_folder()
    if choice==2:
        read_file_folder()
    if choice==3:
        update_folder()
    if choice==4:
        delete_folder()
    if choice==5:
        create_file()
    if choice==6:
        read_file()
    if choice==7:
        update_file()
    if choice==8:
        delete_file()
    if choice==0:
        break