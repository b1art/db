CREATE TRIGGER jCheck3
ON s004.tblOperation
INSTEAD OF INSERT 
AS
DECLARE @intFlatId INT
DECLARE @intOperationTypeId INT
DECLARE @datOperationDate DATE
DECLARE @intWorkerId INT
DECLARE @txtOperationDescription nvarchar(50)

SELECT @intFlatId = (SELECT intFlatId FROM INSERTED)
SELECT @intOperationTypeId = (SELECT intOperationTypeId FROM INSERTED)
SELECT @datOperationDate = (SELECT datOperationDate FROM INSERTED)
SELECT @intWorkerId = (SELECT intWorkerId FROM INSERTED)
SELECT @txtOperationDescription = (SELECT txtOperationDescription FROM INSERTED)


if EXISTS (select 1 from s004.tblOperation 
where (
datOperationDate=(SELECT datOperationDate from INSERTED) 
and
intFlatId=(SELECT intFlatId from INSERTED)
)
) 
	RAISERROR ('jCheck3', 16, 1)
else
	INSERT s004.tblOperation (intFlatId, intOperationTypeId, datOperationDate, intWorkerId, txtOperationDescription)
    VALUES (@intFlatId, @intOperationTypeId, @datOperationDate, @intWorkerId, @txtOperationDescription);
	




