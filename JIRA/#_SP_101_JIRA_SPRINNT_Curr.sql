USE [JIRA]
GO
---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------
IF OBJECT_ID('SP_JIRA_SPRINT_Curr', 'P') IS NOT NULL
DROP PROC SP_JIRA_SPRINT_Curr
GO
---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- ==========================================================================================
CREATE PROCEDURE SP_JIRA_SPRINT_Curr
	-- Add the parameters for the stored procedure here
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
    -- Insert statements for procedure here
---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------
 
TRUNCATE TABLE [dbo].[JIRA_SPRINT] 


INSERT INTO [dbo].[JIRA_SPRINT]
           (
		   --[DT]
     --      ,[DT_SPRINT]
     --      ,[SPRINT]
     --      ,[ParentStory]
           --,
		   [Issue_Type]
           ,[Summary]
           ,[Key]
           ,[Assignee]
           ,[Reporter]
           ,[Priority]
           ,[Status]
           ,[Status2]
           ,[Resolution]
           ,[Created]
           ,[Updated]
           ,[Due_date]
           ,[parent]
           ,[Resolved]
           ,[Status_Category_Changed]
           --,[Linked_Issues]
           --,[Parent_Link]
           ,[Time Resolution]
           ,[Wk_Created]
           ,[Wk_Resolved]
           ,[Wk_Created_Resolved])
SELECT       
	--D.DT
	--,	ISNULL(CONVERT(varchar, S.DATE, 23), '') AS DT_SPRINT
	--, 	ISNULL(S.SPRINT, '') AS SPRINT
	--, 	S.ParentStory
	--,
	ISNULL(J.Issue_Type, '') AS Issue_Type
	, ISNULL(J.Summary, '') AS Summary
	, 	ISNULL(J.[Key], '') AS [Key]
	, 
                         ISNULL(J.Assignee, '') AS Assignee, 
						 ISNULL(J.Reporter, '') AS Reporter, 
						 ISNULL(J.Priority, '') AS Priority, 
						 ISNULL(J.Status, '') AS Status, 
	CASE 
	WHEN J.Status = 'Done' THEN 'Done' 
	WHEN J.Status = 'Blocked' THEN 'Blocked' 
	WHEN J.Status = 'in Build' THEN 'Open' 
	WHEN J.Status = 'In Technical Testing' THEN 'Open' 
	WHEN J.Status = 'In Design' THEN 'Open' 
	WHEN J.Status = 'Ready for Analysis' THEN 'Open' 
	WHEN J.Status = 'Ready for Design' THEN 'Open' 
	WHEN J.Status = 'In Functional Testing' THEN 'Open' 
	WHEN J.Status = 'In Design Validation' THEN 'Open' 
	WHEN J.Status = 'Ready for Build'	THEN 'Open' 
	WHEN J.Status = 'Test State' THEN 'Open' 
	ELSE '' END AS Status2
	, ISNULL(J.Resolution, '') AS Resolution
	, ISNULL(CONVERT(varchar, J.Created, 23), '') AS Created
	, ISNULL(CONVERT(varchar, J.Updated, 23), '') AS Updated
	, ISNULL(J.Due_date, '') AS Due_date, ISNULL(J.parent, '') AS parent
	, ISNULL(CONVERT(varchar, J.Resolved, 23), '') AS Resolved
	, ISNULL(CONVERT(varchar, J.Status_Category_Changed, 23), '') AS Status_Category_Changed
	--, ISNULL(J.Linked_Issues, '') AS Linked_Issues
	--, ISNULL(J.Parent_Link, '') AS Parent_Link
	, CASE 
	WHEN [Status] = 'Done' THEN DATEDIFF(d, created, Resolved) 
	ELSE '' END AS [Time Resolution]
	, DATEPART(ww, J.Created) AS Wk_Created
	, DATEPART(ww, J.Resolved) AS Wk_Resolved
	, DATEPART(ww, J.Resolved) - DATEPART(ww, J.Created) AS Wk_Created_Resolved
FROM	dbo.JIRA AS J 
ORDER BY J.Created
--------===========================================--------
--------===========================================--------
declare @resulta1 as nvarchar(1000)
/* Create two variables that would store the values returned by the fetch statement */
DECLARE @Var_Date date
DECLARE @Var_SPRINT nvarchar(25)
DECLARE @Var_ParentStory nvarchar(250)
/* Define the cursor that can be used to access the records of the table,row by row */

DECLARE cur_x cursor for
                  SELECT [DATE],	[SPRINT],	[ParentStory] FROM  [dbo].[SPRINT]	
				  --WHERE ParentStory 	 = 'DBAAS-5814'
				  ORDER BY 	[ParentStory]  , [DATE]
-- Open the cursor
OPEN cur_x
-- Fetch the rows into variables
FETCH cur_x into @Var_Date,@Var_SPRINT,@Var_ParentStory
--Start a loop to display all the rows of the cursor
WHILE(@@fetch_status=0)
BEGIN

--------------++++++++++++++++++++++++++++
--SELECT @Var_Date,@Var_SPRINT,@Var_ParentStory
--Print 'Department Name =' + @DepartmentName + 'Department Head =' + @DepartmentHead
 --SET @resulta1 = 'UPDATE [sys_scorecards].[dbo].[Clientes] SET [rutaPrev] = ''' + @DepartmentName + ''' WHERE id_clientes = ' + @DepartmentHead
 --PRINT @resulta1
 --exec (@resulta1)

 --SELECT * FROM  [dbo].[JIRA_SPRINT] WHERE parent = 	 @Var_ParentStory	AND		Created	 <= @Var_Date
 --AND 	 DT_SPRINT IS NOT NULL

 Update [dbo].[JIRA_SPRINT] SET   
	DT_SPRINT = @Var_Date	,	
	SPRINT	  = @Var_SPRINT	,
	ParentStory	= @Var_ParentStory
	WHERE	parent = 	 @Var_ParentStory	AND	Created	 <=	 @Var_Date
	 AND 	 DT_SPRINT IS NULL
--------------++++++++++++++++++++++++++++
--Fetch the next row from the cursor
FETCH cur_x into @Var_Date,@Var_SPRINT,@Var_ParentStory
END


-- Close the cursor
CLOSE cur_x
-- Deallocate the cursor
DEALLOCATE cur_x
--------===========================================--------
--------===========================================--------
---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------
END
GO


