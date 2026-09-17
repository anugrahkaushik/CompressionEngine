with open(input("Enter the first file path: ").strip().strip("'").strip('"'),'rb') as file1:
    with open(input("Enter the second file path: ").strip().strip("'").strip('"'),'rb') as file2:
        if file1.read()!=file2.read():
                print("Different")
        else:
            print("Same")