SELECT * FROM s004.tblWorker

INSERT s004.tblOperation (intFlatId, intOperationTypeId, datOperationDate, intWorkerId, txtOperationDescription)
    VALUES (1, 1, '20230228', 1, 'test');

SELECT * FROM s004.tblWorker
