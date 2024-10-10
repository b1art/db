Select txtWorkerSurname, datOperationDate, txtOperationDescription
From s004.tblOperation
Inner Join s004.tblWorker On s004.tblWorker.intWorkerId = s004.tblOperation.intWorkerId
Where (datOperationDate >'2023-02-27') and (txtWorkerSurname = 'Frolov' or txtWorkerSurname = 'Haritonov')
ORDER BY datOperationDate
