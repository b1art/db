ALTER PROCEDURE flatInf
	@intFlatId int
as

DECLARE @txtOwnerSurname nvarchar(50)
DECLARE @txtOwnerName nvarchar(50)
DECLARE @txtOwnerSecondName nvarchar(50)
DECLARE @intCountOperations int

SELECT @txtOwnerSurname = (SELECT txtOwnerSurname FROM 
s004.tblFLat INNER JOIN s004.tblOwner ON s004.tblFlat.intOwnerId = s004.tblOwner.intOwnerId
where s004.tblFlat.intFlatId = @intFlatId
)

SELECT @txtOwnerName = (SELECT txtOwnerName FROM 
s004.tblFLat INNER JOIN s004.tblOwner ON s004.tblFlat.intOwnerId = s004.tblOwner.intOwnerId
where s004.tblFlat.intFlatId = @intFlatId
)

SELECT @txtOwnerSecondName = (SELECT txtOwnerSecondName FROM 
s004.tblFLat INNER JOIN s004.tblOwner ON s004.tblFlat.intOwnerId = s004.tblOwner.intOwnerId
where s004.tblFlat.intFlatId = @intFlatId
)

SELECT @intCountOperations = (SELECT COUNT(*) FROM 
s004.tblFLat INNER JOIN s004.tblOperation ON s004.tblOperation.intFlatId = s004.tblFLat.intFlatId
where s004.tblFlat.intFlatId = @intFlatId)



BEGIN
	CREATE TABLE flatInfTbl
	(
		txtOwnerSurname nvarchar(50),
		txtOwnerName nvarchar(50),
		txtOwnerSecondName nvarchar(50),
		intFlatId int,
		intCountOperations int
	);

	INSERT flatInfTbl (txtOwnerSurName, txtOwnerName, txtOwnerSecondName, intFlatId, intCountOperations)
    VALUES (@txtOwnerSurName, @txtOwnerName, @txtOwnerSecondName, @intFlatId, @intCountOperations);

	SELECT * FROM flatInfTbl
	DROP TABLE flatInfTbl
END
