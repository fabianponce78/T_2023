USE [JIRA]
GO
---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------
IF OBJECT_ID('SP_BULK', 'P') IS NOT NULL
DROP PROC SP_BULK
GO
---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- ==========================================================================================
CREATE PROCEDURE SP_BULK
	-- Add the parameters for the stored procedure here
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
    -- Insert statements for procedure here
---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------
----------====================================================================
----------====================================================================
TRUNCATE TABLE [JIRA]
TRUNCATE TABLE [SPRINT]
----------------------------------------------------------------
BULK INSERT [JIRA]
FROM 'C:\#_FP_APEX\#_DEV\#_Py_FP\Py_Test\JIRA\OutPut\JIRA.CSV'
WITH (FIRSTROW = 2,
    FIELDTERMINATOR = '|',
    ROWTERMINATOR='\n' );

--SELECT * FROM [JIRA]
----------------------------------------------------------------


BULK INSERT [SPRINT]
FROM 'C:\#_FP_APEX\#_DEV\#_Py_FP\Py_Test\JIRA\OutPut\SPRINT.CSV'
WITH (FIRSTROW = 2,
    FIELDTERMINATOR = '|',
    ROWTERMINATOR='\n' );

--SELECT * FROM [SPRINT]
----------====================================================================
----------====================================================================
IF OBJECT_ID(N'DT', N'U') IS NOT NULL  
   DROP TABLE DT;  

WITH T_CTE AS (
SELECT	DISTINCT		convert(varchar,Created,23)	AS 'DT'	 FROM [JIRA]
UNION
SELECT	DISTINCT	convert(varchar,DATE,23) AS 'DT' FROM [SPRINT]
)
SELECT * INTO DT FROM T_CTE
----------====================================================================
----------====================================================================
EXECUTE SP_JIRA_SPRINT_Curr
---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------
END
GO


