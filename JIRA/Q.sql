USE [JIRA]
GO
---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------
--EXECUTE SP_BULK
 
--TRUNCATE TABLE [JIRA]
--TRUNCATE TABLE [SPRINT]
----------------------------------------------------------------
 

--SELECT * FROM [JIRA]
--SELECT * FROM [SPRINT]
--SELECT * FROM [DT]

SELECT D.DT
--, '---' 
, ISNULL(convert(varchar,S.[DATE],23),'') AS 'DT_SPRINT' 
, ISNULL(S.SPRINT,'') AS 'SPRINT'
--, '---' 
, ISNULL(J.[Issue_Type],'') AS 'Issue_Type'
, ISNULL(J.[Summary],'') AS 'Summary'
, ISNULL(J.[Key],'') AS 'Key'
, ISNULL(J.[Assignee],'') AS 'Assignee'      
, ISNULL(J.[Reporter],'') AS 'Reporter'      
, ISNULL(J.[Priority],'') AS 'Priority'      
, ISNULL(J.[Status],'') AS 'Status'
, ISNULL(J.[Resolution],'') AS 'Resolution'      
, ISNULL(convert(varchar,J.Created,23),'') AS 'Created'      
, ISNULL(convert(varchar,J.[Updated],23),'') AS 'Updated'      
, ISNULL(J.[Due_date],'') AS 'Due_date'
, ISNULL(J.[parent],'') AS 'parent'      
, ISNULL(convert(varchar,J.[Resolved],23),'') AS 'Resolved'      
, ISNULL(convert(varchar,J.[Status_Category_Changed],23),'') AS 'Status_Category_Changed'      
, ISNULL(J.[Linked_Issues],'') AS 'Linked_Issues'      
, ISNULL(J.[Parent_Link],'') AS 'Parent_Link'

FROM [DT] AS D
FULL JOIN [SPRINT] AS S ON	D.DT = convert(varchar,S.[DATE],23)
FULL JOIN [JIRA] as J ON D.DT = convert(varchar,J.Created,23) --AND J.[parent] = 'DBAAS-5814'
--WHERE J.[parent] like 'DBAAS-5814'
ORDER BY D.DT

