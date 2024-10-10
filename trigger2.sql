CREATE TRIGGER jSum ON s004.tblOperation
FOR INSERT 
AS
 DECLARE @sum INT
 select @sum = (select fltOperationPrice from 
				INSERTED INNER JOIN s004.tblOperationType 
				on INSERTED.intOperationTypeId =  s004.tblOperationType.intOperationTypeId)
BEGIN
	UPDATE s004.tblWorker
	SET fltSum = fltSum + @sum
	WHERE intWorkerId = (SELECT intWorkerId from INSERTED)
END
