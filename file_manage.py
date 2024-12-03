import os
print("                               ##FILE MANAGEMENT SYSTEM##")
while True:
    print()
    print()
    print("1: Create file\n2: Delete file\n3: View all files\n4: Read file\n5: Edit file\n6: Exit")
    choice=(input("Enter your choice(1-6) : "))


    if choice=="1":
        filename=input("Enter file name : ")
        try:
            with open(filename,"x") as file:
                print(f"file '{filename}' created successfully")
        except FileExistsError:
            print(f"File '{filename}' already exist")
        except Exception as ex:
            print(f"An error occurred of {ex}")


    elif choice=="2":
        filename=input("Enter file name : ")
        try:
            os.remove(filename)
            print(f"file '{filename}' Deleted successfully!")
        except FileNotFoundError:
            print(f"File '{filename}' does not exist")
        except Exception as ex:
            print(f"An error occurred of {ex}")


    elif choice=="3":
        all_files=os.listdir()
        if not all_files:
            print("No file found!")
        else:
            print("files in directory : ")
            for i in all_files:
                print(i)


    elif choice=="4":
        filename=input("Enter file name : ")
        try:
            with open(filename,"r") as file:
                work=file.read()
                print(f"content in '{filename}' : \n{work} ")
        except FileNotFoundError:
            print(f"File '{filename}' does not exist!")
        except Exception as ex:
            print(f"An error occurred of {ex}!")

    elif choice=="5":
        filename=input("Enter file name : ")
        content=input("Enter content to add : ")
        try:
            with open(filename,"a") as file:
                file.write(content)
                print(f"file '{filename}' updated successfully")
        except Exception as ex:
            print(f"An error occurred of {ex}")

    elif choice=="6":
        print("Closing the app........")
        break
    else:
        print("Invalid input!!!")