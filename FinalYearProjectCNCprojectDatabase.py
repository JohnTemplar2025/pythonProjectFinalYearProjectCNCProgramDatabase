from tkinter import*
import sqlite3


root = Tk()
root.title('UB Mechanical Dept. CNC program Library')
root.geometry("600x400")

def creatingDB():
    #conn = sqlite3.connect('CNCProgramLibrary.db')

    #c = conn.cursor()

    #CREATE A TABLE
    #c.execute(""" CREATE TABLE ProgramCode (
    #       Poly_Code TEXT,
    #       Type_of_Machine TEXT,
    #       Number_of_Operations INTEGER,
    #       Complexity TEXT,
    #       Major_defining_Operation_1 TEXT,
    #       Major_defining_Operation_2 TEXT,
    #       Tools TEXT,
    #       Dimensions TEXT,
    #       File_Location BLOB
    #       )""")

    #conn.commit()
    #conn.close()
    return

def submitnewprogram():
    NewEntry = Toplevel()
    NewEntry.title('New Entry of Program')
    NewEntry.geometry("1000x500")

    def submit():
        conn = sqlite3.connect('CNCProgramLibrary.db')

        c = conn.cursor()

        c.execute("INSERT INTO ProgramCode VALUES (:Poly_Code, :Type_of_Machine, :Number_of_Operations, :Complexity, :Major_defining_Operation_1, :Major_defining_Operation_2, :Tools, :Dimensions, :File_Location)",
                  {
                      'Poly_Code': PolyCode.get(),
                      'Type_of_Machine': MachineType.get(),
                      'Number_of_Operations': NumOp.get(),
                      'Complexity': Complexity.get(),
                      'Major_defining_Operation 1': MajorOp1.get(),
                      'Major_defining_Operation 2': MajorOp2.get(),
                      'Tools': Tools.get(),
                      'Dimensions': Dimensions.get(),
                      'File_Location': FileLocation.get()
                  })

        conn.commit()
        conn.close()

        PolyCode.delete(0, END)
        MachineType.set("Select Machine")
        NumOp.delete(0, END)
        Complexity.set("Select complexity")
        MajorOp1.set("Select 1st Major defining Operation")
        MajorOp2.set("Select 2nd Major defining Operation")
        Tools.delete(0, END)
        Dimensions.delete(0, END)
        FileLocation.delete(0, END)

    InstructionsNewEntry = ("Please submit the right information about "
                            "the new program code on the fields provided.\n"
                            + "Note:\n"
                            + "- The Polycode of the program will be automatically generated.\n "
                            + " - For Major defining Operations, "
                              "0-9 are Lathe Operations and 10-19 are Milling Operations.\n"
                            +"- Enter tools with their specs in their respective field,"
                             " if many separate with a comma.\n"
                            +"Thank you")

    MyLabel2 = Label(NewEntry, text=InstructionsNewEntry)
    MyLabel2.grid(row=0, column=2)

    MachineOptions = ["Lathe machine", "Milling Machine"]
    ComplexList = ["Easy", "Medium", "Hard", "Expert"]
    OperationOptions = [
        "0.Simple operation (Linear &circular interpolation)",
        "1.Longitudinal turning cycle (G20) or Face turning cycle (G24)",
        "2.Thread cutting cycle (G21) orThread cutting cycle (G33)",
        "3.Finishing cycle (G72) or Contour turning cycle (G73) or Facing cycle (G74) or Pattern repeating (G75)",
        "4.Deep hole drilling/Face cut-in cycle (G76)",
        "5.Cut-in cycle (X-axis) (G77)",
        "6.Multiple Threading cycle (G78)",
        "7.Drilling cycle (G83)",
        "8.Tapping cycle (G84)",
        "9.Reaming cycle (G85)",
        "10.Simple operation (Linear &circular interpolation)",
        "11.Scale factor mirror (G51)",
        "12.Coordinate system rotation (G68)",
        "13.Chip break drilling cycle (G73) or Withdrawal drilling cycle (G83)",
        "14.Left tapping cycle (G74) or Tapping cycle (G84)",
        "15.Fine drilling cycle (G76)",
        "16.Drilling cycle (G81) or Drilling cycle with spindle stop (G86)",
        "17.Drilling cycle with dwell (G82)",
        "18.Reaming cycle (G85)",
        "19.Back pocket drilling cycle (G87)"]

    MachineType = StringVar()
    MachineType.set("Select Machine")
    MachTypDrop = OptionMenu(NewEntry, MachineType, *MachineOptions)
    MajorOp1 = StringVar()
    MajorOp2 = StringVar()
    MajorOp1.set("Select 1st Major defining Operation")
    MajorOp2.set("Select 2nd Major defining Operation")
    MajOp1Drop = OptionMenu(NewEntry,MajorOp1, *OperationOptions)
    MajOp2Drop = OptionMenu(NewEntry,MajorOp2, *OperationOptions)
    Complexity = StringVar()
    Complexity.set("Select complexity")
    ComDrop = OptionMenu(NewEntry, Complexity, *ComplexList)

    NumOp = Entry(NewEntry, width=30)
    NumOpLabel = Label(NewEntry, text="Number of Operations:")
    Tools = Entry(NewEntry, width=50)
    ToolsLabel = Label(NewEntry, text="Enter tools used:")
    Dimensions = Entry(NewEntry, width=30)
    DimensionsLabel = Label(NewEntry, text="Enter Dimensions of workpiece('X','Y','Z')")
    FileLocation = Entry(NewEntry, width=50)
    FilLocLabel = Label(NewEntry,text="Enter File directory to location of file:")
    PolyCode = Entry(NewEntry, width=30)
    PolyCodeLabel = Label(NewEntry, text="Enter the polycode using the rules stated:")

    MachTypDrop.grid(row=1, column=0, padx=10, pady=10)
    MajOp1Drop.grid(row=2, column=0)
    MajOp2Drop.grid(row=3, column=0)
    ComDrop.grid(row=4, column=0)
    NumOp.grid(row=5, column=1, padx=20)
    NumOpLabel.grid(row=5, column=0)
    Dimensions.grid(row=6, column=1)
    DimensionsLabel.grid(row=6, column=0)
    Tools.grid(row=7, column=1, padx=20)
    ToolsLabel.grid(row=7, column=0)
    FileLocation.grid(row=8, column=1)
    FilLocLabel.grid(row=8, column=0)
    PolyCode.grid(row=9, column=1)
    PolyCodeLabel.grid(row=9, column=0)

    SubmitBtn = Button(NewEntry, text="Submit record", command=submit)
    SubmitBtn.grid(row=10, column=0, columnspan=2, ipadx=20)
    ClosingBtn = Button(NewEntry, text="Close window", command=NewEntry.destroy)
    ClosingBtn.grid(row=11, column=2, columnspan=2, ipadx=30)
def viewdatabase():
    ViewDB = Toplevel()
    ViewDB.title('Display Program Database')
    ViewDB.geometry("1000x500")

    DBTitle = Label(ViewDB, text="Program Code Database")
    DBTitle.grid(row=0, column=0)

    def query():
        conn = sqlite3.connect('CNCProgramLibrary.db')

        c = conn.cursor()

        c.execute("SELECT *,oid FROM ProgramCode")
        records = c.fetchall()

        print_records = ''
        for record in records:
            print_records += str(record) + "\n"

        RecordLabel = Label(ViewDB, text=print_records)
        RecordLabel.grid(row=1, column=0)

        conn.commit()
        conn.close()

    DisplayDB = Button(ViewDB, text="Display Records", command=query)
    DisplayDB.grid(row=9, column=0, columnspan=4, padx=10, pady=10)

    ExitViewDB = Button(ViewDB, text="Exit", command=ViewDB.destroy)
    ExitViewDB.grid(row=10, column=0, columnspan=4, padx=10, pady=10)

def searchnedit():
    SearchnEdit = Toplevel()
    SearchnEdit.title('Query Program Code Database')
    SearchnEdit.geometry("1000x500")

    def searchDB():
        conn = sqlite3.connect('CNCProgramLibrary.db')
        c = conn.cursor()

        sql_query = f"SELECT * FROM ProgramCode WHERE SearchColumn LIKE '%SearchEnquiry%'"

        c.execute(sql_query)

        records = c.fetchall()

        print_records = ''
        for record in records:
            print_records += str(record) + "\n"

        DisplayLabel = Label(SearchnEdit, text=print_records)
        DisplayLabel.grid(row=2, column=3)

    SnEText = "Welcome to the Query section:"

    SnETitle = Label(SearchnEdit, text=SnEText)
    SnETitle.grid(row=0, column=0)

    SearchList = [
        "Poly_Code",
        "Type_of_Machine",
        "Number_of_Operations",
        "Complexity",
        "Major_defining_Operation_1",
        "Major_defining_Operation_2",
        "Tools",
        "Dimensions",
        "File_Location"]

    SearchColumn = StringVar()
    SearchColumn.set("Select Column")
    SearchCDrop = OptionMenu(SearchnEdit, SearchColumn, *SearchList)
    SearchCDrop.grid(row=1, column=0, padx=5, pady=5)

    SearchEnquiry = Entry(SearchnEdit, width=20)
    SearchEnquiry.grid(row=2, column=1)
    SEnquirLabel = Label(SearchnEdit, text="Enter what you're looking for:")
    SEnquirLabel.grid(row=2, column=0)

    SearchEnqBtn = Button(SearchnEdit, text="Search", command=searchDB)
    SearchEnqBtn.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    ExitSnE = Button(SearchnEdit, text="Exit", command=SearchnEdit.destroy)
    ExitSnE.grid(row=10, column=0, columnspan=4, padx=10, pady=10)

def searchndelete():
    SearchnDelete = Toplevel()
    SearchnDelete.title('Search and Delete')
    SearchnDelete.geometry("1000x500")

    SnDText = "Welcome to the Search and Delete page:"

    SnDTitle = Label(SearchnDelete, text=SnDText)
    SnDTitle.grid(row=0, column=0)

    ExitSnD = Button(SearchnDelete, text="Exit", command=SearchnDelete.destroy)
    ExitSnD.grid(row=10, column=0, columnspan=4, padx=10, pady=10)

welcomingremarks = ("Welcome to the CNC program libray,\n " +
                    "You'll find all lathe and milling programs in the database.\n" +
                    "Please select which function you would like to perform:")

MyLabel1 = Label(root, text=welcomingremarks)
MyLabel1.grid(row=0, column=5,)

NewEntryButton = Button(root, text="Enter a new program", command=submitnewprogram)
NewEntryButton.grid(row=2, column=1, columnspan=2, padx=10, pady=10)
ViewDatabaseButton = Button(root, text="Display the whole database", command=viewdatabase)
ViewDatabaseButton.grid(row=3, column=1, columnspan=2, padx=10, pady=10)
QueryNDisplay = Button(root, text="Search & display program/s")
QueryNDisplay.grid(row=4, column=1, columnspan=2, padx=10, pady=10)
EditProgram = Button(root, text="Search & edit a program", command=searchnedit)
EditProgram.grid(row=5,column=1, columnspan=2, padx=10, pady=10)
DeleteProgram = Button(root, text="Search & delete a program", command=searchndelete)
DeleteProgram.grid(row=6, column=1, columnspan=2, padx=10, pady=10)
ExitProgram = Button(root, text="Exit Program Library", command=root.quit)
ExitProgram.grid(row=7, column=1, columnspan=6)

root.mainloop()


