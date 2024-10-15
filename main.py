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
    data.append([str(r[0]),str(r[1]),str(r[2]),str(r[3]),int(r[4]),int(r[5]),int(r[6]),int(r[7])])


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
            app=tree.item(item)["values"][7]
            SQL_QUERY_app = f"""
            Select txtOperationTypeName,txtWorkerSurname,txtWorkerName,txtWorkerSecondName,txtOperationDescription
            From s004.tblOperationType
            Inner Join s004.tblOperation On s004.tblOperationType.intOperationTypeId = s004.tblOperation.intOperationTypeId
            inner  join s004.tblWorker on s004.tblOperation.intWorkerId = s004.tblWorker.intWorkerId
            where intFlatId = {app}
            """

            cursor.execute(SQL_QUERY_app)
            operations = cursor.fetchall()

            columns_oper = ("txtOperationTypeName", "txtWorkerSurname", "txtWorkerName", "txtWorkerSecondName", "txtOperationDescription")
            tree_oper = ttk.Treeview(window_app, columns=columns_oper, show="headings")
            tree_oper.pack(fill=BOTH, expand=0, side=BOTTOM)
            tree_oper.heading("txtOperationTypeName", text="Тип работ")
            tree_oper.heading("txtWorkerSurname", text="Фамилия рабочего")
            tree_oper.heading("txtWorkerName", text="Имя рабочего")
            tree_oper.heading("txtWorkerSecondName", text="Отчество рабочего")
            tree_oper.heading("txtOperationDescription", text="Описание")

            data_opers = []
            for oper in operations:
                data_opers.append([str(oper[0]), str(oper[1]), str(oper[2]), str(oper[3]), str(oper[4])])

            for oper in data_opers:
                tree_oper.insert("", END, values=oper)


        intOperationTypeId_field = ttk.Entry(window_app)
        datOperationDate_field = ttk.Entry(window_app)
        intWorkerId_field = ttk.Entry(window_app)
        txtOperationDescription_field = ttk.Entry(window_app)

        Label(window_app, text='Квартира {}'.format(app)).pack(anchor=N)

        Label(window_app, text='ID операции').pack(anchor=W)
        intOperationTypeId_field.pack(anchor=W)
        Label(window_app, text='Дата проведения\nxxxx.xx.xx').pack(anchor=W)
        datOperationDate_field.pack(anchor=W)
        Label(window_app, text='ID рабочего').pack(anchor=W)
        intWorkerId_field.pack(anchor=W)
        Label(window_app, text='Описание работ').pack(anchor=W)
        txtOperationDescription_field.pack(anchor=W)



        def click_addoper():
            flat = app
            owner = intOperationTypeId_field.get()
            date = datOperationDate_field.get()
            print(date.replace(".",""))
            worker = intWorkerId_field.get()
            descr = txtOperationDescription_field.get()

            SQL_QUERY_addoper = f"""
                        INSERT INTO s004.tblOperation (intFlatId, intOperationTypeId, datOperationDate, intWorkerId, txtOperationDescription)
                            VALUES ({flat}, {owner}, '{date}', {worker}, '{descr}');
                        """
            cursor.execute(SQL_QUERY_addoper)

            cursor.execute(SQL_QUERY_app)
            operations = cursor.fetchall()

            data_opers.append([str(operations[-1][0]), str(operations[-1][1]), str(operations[-1][2]), str(operations[-1][3]), str(operations[-1][4])])

            tree_oper.insert("", END, values=data_opers[-1])

        button_addoper = ttk.Button(window_app, text="Добавить работу", command=click_addoper)
        button_addoper.pack(anchor=W, pady=25)



    def click_addapp():
        window_addapps = Tk()
        window_addapps.title("Добавление квартиры")
        window_addapps.geometry("1920x1080")

        adress_field = ttk.Entry(window_addapps)
        intOwnerId_field = ttk.Entry(window_addapps)
        fltArea_field= ttk.Entry(window_addapps)
        intCount_field = ttk.Entry(window_addapps)
        intStorey_field = ttk.Entry(window_addapps)

        Label(window_addapps, text='Адрес').pack(anchor=W)
        adress_field.pack(anchor=NW, padx=8, pady=8)
        Label(window_addapps, text='ID владельца').pack(anchor=W)
        intOwnerId_field.pack(anchor=NW, padx=8, pady=8)
        Label(window_addapps, text='Площадь').pack(anchor=W)
        fltArea_field.pack(anchor=NW, padx=8, pady=8)
        Label(window_addapps, text='Количество жильцов').pack(anchor=W)
        intCount_field.pack(anchor=NW, padx=8, pady=8)
        Label(window_addapps, text='Этаж').pack(anchor=W)
        intStorey_field.pack(anchor=NW, padx=8, pady=8)

        def submit():
            adress = adress_field.get()
            print(adress)
            intOwnerId = intOwnerId_field.get()
            fltArea = fltArea_field.get()
            intCount = intCount_field.get()
            intStorey = intStorey_field.get()

            SQL_QUERY_addapps = f"""
            INSERT s004.tblFlat (txtFlatAddress, intOwnerId, fltArea, intCount, intStorey)
                VALUES ('{adress}', {intOwnerId}, {fltArea}, {intCount}, {intStorey});
            """
            cursor.execute(SQL_QUERY_addapps)
            conn.commit()

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




