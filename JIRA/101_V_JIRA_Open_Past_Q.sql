USE	[JIRA]
GO
--------------------------------------------------------
if exists(select 1 from sys.views where name='V_JIRA_Open_Past_Q' and type='v')
drop view V_JIRA_Open_Past_Q;
go
--------------------------------------------------------
create view V_JIRA_Open_Past_Q
as
--------------------------------------------------------



SELECT			
	TOP (1000) 
	DT, DT_SPRINT, SPRINT, ParentStory, Issue_Type, Summary, 
	[Key], Assignee, Reporter, 
	Priority, Status, Status2, 
	Resolution, Created, 
	ISNULL(CONVERT(varchar, DATEPART(QUARTER, Created), 23), '') AS QUARTER,
	Updated, Due_date, parent, Resolved, 
	ISNULL(CONVERT(varchar, Status_Category_Changed, 23), '') AS Status_Category_Changed, 
	--Linked_Issues, Parent_Link, 
	CASE 
		WHEN [Status] = 'Done' THEN DATEDIFF(d, created, Resolved) 
		ELSE '' 
		END AS [Time Resolution], 
	Wk_Created, 
	Wk_Resolved, 
	Wk_Created_Resolved

FROM            dbo.JIRA_SPRINT
WHERE        (Status NOT IN ('Done')) AND (YEAR(Created) <= YEAR(GETDATE()))

--SELECT        TOP (100) PERCENT D.DT, ISNULL(CONVERT(varchar, S.DATE, 23), '') AS DT_SPRINT, ISNULL(S.SPRINT, '') AS SPRINT, ISNULL(J.Issue_Type, '') AS Issue_Type, ISNULL(J.Summary, '') AS Summary, ISNULL(J.[Key], '') AS [Key], 
--                         ISNULL(J.Assignee, '') AS Assignee, ISNULL(J.Reporter, '') AS Reporter, ISNULL(J.Priority, '') AS Priority, ISNULL(J.Status, '') AS Status, ISNULL(J.Resolution, '') AS Resolution, ISNULL(CONVERT(varchar, J.Created, 23), '') 
--                         AS Created, ISNULL(CONVERT(varchar, DATEPART(QUARTER, J.Created), 23), '') AS QUARTER, ISNULL(CONVERT(varchar, J.Updated, 23), '') AS Updated, ISNULL(J.Due_date, '') AS Due_date, ISNULL(J.parent, '') AS parent, 
--                         ISNULL(CONVERT(varchar, J.Resolved, 23), '') AS Resolved, ISNULL(CONVERT(varchar, J.Status_Category_Changed, 23), '') AS Status_Category_Changed, ISNULL(J.Linked_Issues, '') AS Linked_Issues, ISNULL(J.Parent_Link, 
--                         '') AS Parent_Link, CASE WHEN [Status] = 'Done' THEN DATEDIFF(d, created, Resolved) ELSE '' END AS [Time Resolution]
--FROM            dbo.DT AS D FULL OUTER JOIN
--                         dbo.SPRINT AS S ON D.DT = CONVERT(varchar, S.DATE, 23) FULL OUTER JOIN
--                         dbo.JIRA AS J ON D.DT = CONVERT(varchar, J.Created, 23)
--WHERE        (J.Status NOT IN ('Done')) 
--AND (YEAR(J.Created) <= YEAR(GETDATE())) 
----AND (DATEPART(QUARTER, J.Created) <= DATEPART(QUARTER, GETDATE()) - 1)

--SELECT TOP (1000) [DT]
--      ,[DT_SPRINT]
--      ,[SPRINT]
--      ,[ParentStory]
--      ,[Issue_Type]
--      ,[Summary]
--      ,[Key]
--      ,[Assignee]
--      ,[Reporter]
--      ,[Priority]
--      ,[Status]
--      ,[Status2]
--      ,[Resolution]
--      ,[Created]
--	  ,ISNULL(CONVERT(varchar, DATEPART(QUARTER,  Created), 23), '') AS QUARTER
--      ,[Updated]
--      ,[Due_date]
--      ,[parent]
--      ,[Resolved]
--	  ,ISNULL(CONVERT(varchar, Status_Category_Changed, 23), '') AS Status_Category_Changed 	--
--      --,[Status_Category_Changed]
--      ,[Linked_Issues]
--      ,[Parent_Link]
--      --,[Time Resolution]
--	  ,CASE 
--		WHEN [Status] = 'Done' THEN DATEDIFF(d, created, Resolved) 
--		ELSE '' END AS [Time Resolution]
--      ,[Wk_Created]
--      ,[Wk_Resolved]
--      ,[Wk_Created_Resolved]
--  FROM [JIRA].[dbo].[JIRA_SPRINT]
--  WHERE         (Status NOT IN ('Done')) 
--AND (YEAR(Created) <= YEAR(GETDATE())) 


--------------------------------------------------------
GO
SELECT * FROM [dbo].[V_JIRA_Open_Past_Q]