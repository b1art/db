from tkinter import *
from tkinter import ttk
import pyodbc

SERVER = '<192.168.112.103>'
DATABASE = '<db22203>'
USERNAME = '<User004>'
PASSWORD = '<User004&!68>'

conn = pyodbc.connect(driver = '{SQL Server}',server = '192.168.112.103' , database = 'db22203', user = 'User004', password = 'User004&!68')


SQL_QUERY_apps = """
Select txtOwnerSurname, txtOwnerName, txtOwnerSecondName, txtFlatAddress, fltArea, intCount, intStorey, intFlatId
From s004.tblFlat
Inner Join s004.tblOwner On s004.tblOwner.intOwnerId = s004.tblFlat.intOwnerId
"""

cursor = conn.cursor()
cursor.execute(SQL_QUERY_apps)
records = cursor.fetchall()
data = []
for r in records:
    data.append([str(r[0]),str(r[1]),str(r[2]),str(r[3]),int(r[4]),int(r[5]),int(r[6])])


# for r in records:
#     print(f"{r.txtWorkerSurname}\t{r.datOperationDate}\t{r.txtOperationDescription}")

window = Tk()
window.title("Main")
window.geometry("500x500")

def click_apps():
    window_apps = Tk()
    window_apps.title("Квартиры")
    window_apps.geometry("1920x1080")

    columns = ("txtOwnerSurname", "txtOwnerName", "txtOwnerSecondName", "txtFlatAddress", "fltArea", "intCount", "intStorey", "intFlatId")
    tree = ttk.Treeview(window_apps, columns=columns, show="headings")
    tree.pack(fill=BOTH, expand=1, side=BOTTOM)

    def OnDoubleClick(event):
        window_app = Tk()
        window_app.title("Квартирa")
        window_app.geometry("1920x1080")

        for item in tree.selection():
            #Label(window_app, text=tuple(tree.item(item)["values"])).pack()
            app=tree.item(item)["values"][6]
            SQL_QUERY_app = f"""
            Select txtOperationTypeName,txtWorkerSurname,txtWorkerName,txtWorkerSecondName,txtOperationDescription
            From s004.tblOperationType
            Inner Join s004.tblOperation On s004.tblOperationType.intOperationTypeId = s004.tblOperation.intOperationTypeId
            inner  join s004.tblWorker on s004.tblOperation.intWorkerId = s004.tblWorker.intWorkerId
            where intFlatId = {app}
            """
            cursor.execute(SQL_QUERY_app)
            operations = cursor.fetchall()
            for oper in operations:
                Label(window_app, text=oper).pack()

        flatid_field = ttk.Entry(window_app)
        intOperationTypeId_field = ttk.Entry(window_app)
        datOperationDate_field = ttk.Entry(window_app)
        intWorkerId_field = ttk.Entry(window_app)
        txtOperationDescription_field = ttk.Entry(window_app)

        flatid_field.pack(anchor=NW, padx=8, pady=8)
        intOperationTypeId_field.pack(anchor=NW, padx=8, pady=8)
        datOperationDate_field.pack(anchor=NW, padx=8, pady=8)
        intWorkerId_field.pack(anchor=NW, padx=8, pady=8)
        txtOperationDescription_field.pack(anchor=NW, padx=8, pady=8)

        def click_addoper():
            flat = flatid_field.get()
            owner = intOperationTypeId_field.get()
            date = datOperationDate_field.get()
            worker = intWorkerId_field.get()
            descr = txtOperationDescription_field.get()

            SQL_QUERY_addoper = f"""
                        INSERT s004.tblOperation (FlatId, intOperationTypeId, datOperationDate, intWorkerId, txtOperationDescription)
                            VALUES ('{flat}', {owner}, {date}, {worker}, {descr});
                        """
            cursor.execute(SQL_QUERY_addoper)

        button_addoper = ttk.Button(window_app, text="Добавить работу", command=click_addoper)
        button_addoper.pack(anchor=NW, expand=1)



    def click_addapp():
        window_addapps = Tk()
        window_addapps.title("Добавление квартиры")
        window_addapps.geometry("1920x1080")

        adress_field = ttk.Entry(window_addapps)
        intOwnerId_field = ttk.Entry(window_addapps)
        fltArea_field= ttk.Entry(window_addapps)
        intCount_field = ttk.Entry(window_addapps)
        intStorey_field = ttk.Entry(window_addapps)

        adress_field.pack(anchor=NW, padx=8, pady=8)
        intOwnerId_field.pack(anchor=NW, padx=8, pady=8)
        fltArea_field.pack(anchor=NW, padx=8, pady=8)
        intCount_field.pack(anchor=NW, padx=8, pady=8)
        intStorey_field.pack(anchor=NW, padx=8, pady=8)

        def submit():
            adress = adress_field.get()
            intOwnerId = intOwnerId_field.get()
            fltArea = fltArea_field.get()
            intCount = intCount_field.get()
            intStorey = intStorey_field.get()

            SQL_QUERY_addapps = f"""
            INSERT s004.tblFlat (txtFlatAddress, intOwnerId, fltArea, intCount, intStorey)
                VALUES ('{adress}', {intOwnerId}, {fltArea}, {intCount}, {intStorey});
            """
            cursor.execute(SQL_QUERY_addapps)

        buttonsubmit = ttk.Button(window_addapps, text="Подтвердить добавление", command=submit)
        buttonsubmit.pack(anchor=NW, expand=1)

    button = ttk.Button(window_apps, text="Добавить квартиру", command=click_addapp)
    button.pack(anchor=NW, expand=1)

    tree.heading("txtOwnerSurname", text="Фамилия")
    tree.heading("txtOwnerName", text="Имя")
    tree.heading("txtOwnerSecondName", text="Отчество")
    tree.heading("txtFlatAddress", text="Адрес")
    tree.heading("fltArea", text="Площадь")
    tree.heading("intCount", text="Количество жильцов")
    tree.heading("intStorey", text="Этаж")
    tree.heading("intFlatId", text="Квартира")
    tree.bind("<Double-1>", OnDoubleClick)

    for flat in data:
        tree.insert("", END, values=flat)

button = ttk.Button(text="Создать окно", command=click_apps)
button.pack(anchor=NW, expand=1)



window.mainloop()




