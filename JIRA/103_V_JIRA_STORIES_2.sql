USE	[JIRA]
GO
--------------------------------------------------------
if exists(select 1 from sys.views where name='V_JIRA_STORIES' and type='v')
drop view V_JIRA_STORIES;
go
--------------------------------------------------------
create view V_JIRA_STORIES
as
--------------------------------------------------------

--SELECT        TOP (100) PERCENT 
--D.DT, 
--ISNULL(CONVERT(varchar, S.DATE, 23), '') AS DT_SPRINT, 
--ISNULL(S.SPRINT, '') AS SPRINT, 
--ISNULL(S.[ParentStory], '') AS ParentStory, 
--ISNULL(J.Issue_Type, '') AS Issue_Type, ISNULL(J.Summary, '') AS Summary, ISNULL(J.[Key], '') AS [Key], 
--                         ISNULL(J.Assignee, '') AS Assignee, ISNULL(J.Reporter, '') AS Reporter
--						 , ISNULL(J.Priority, '') AS Priority, ISNULL(J.Status, '') AS Status, 
--                         CASE 
--						 WHEN J.Status = 'Done' THEN 'Done' 
--						 WHEN J.Status = 'Blocked' THEN 'Blocked' 
--						 WHEN J.Status = 'in Build' THEN 'Open' 
--						 WHEN J.Status = 'In Technical Testing' THEN 'Open' 
--						 WHEN J.Status = 'In Design' THEN 'Open' 
--						 WHEN J.Status = 'Ready for Analysis' THEN 'Open' 
--						 WHEN J.Status = 'Ready for Design' THEN 'Open' 
--						 WHEN J.Status = 'In Functional Testing' THEN 'Open' 
--						 WHEN J.Status = 'In Design Validation' THEN 'Open' 
--						 WHEN J.Status = 'Ready for Build' THEN 'Open' 
--						 WHEN J.Status = 'Test State' THEN 'Open' 
--						 ELSE '' END AS Status2, ISNULL(J.Resolution, '') AS Resolution, ISNULL(CONVERT(varchar, J.Created, 23), '') AS Created, ISNULL(CONVERT(varchar, J.Updated, 23), '') 
--                         AS Updated, ISNULL(J.Due_date, '') AS Due_date, ISNULL(J.parent, '') AS parent, ISNULL(CONVERT(varchar, J.Resolved, 23), '') AS Resolved, ISNULL(CONVERT(varchar, J.Status_Category_Changed, 23), '') 
--                         AS Status_Category_Changed, ISNULL(J.Linked_Issues, '') AS Linked_Issues, ISNULL(J.Parent_Link, '') AS Parent_Link, CASE WHEN [Status] = 'Done' THEN DATEDIFF(d, created, Resolved) ELSE '' END AS [Time Resolution], 
--                         DATEPART(ww, J.Created) AS Wk_Created, DATEPART(ww, J.Resolved) AS Wk_Resolved, DATEPART(ww, J.Resolved) - DATEPART(ww, J.Created) AS Wk_Created_Resolved
--FROM            dbo.DT AS D FULL OUTER JOIN
--                         dbo.SPRINT AS S ON D.DT = CONVERT(varchar, S.DATE, 23) FULL OUTER JOIN
--                         dbo.JIRA AS J ON D.DT = CONVERT(varchar, J.Created, 23)
--						 WHERE 	
--						 --S.[ParentStory] =  J.parent
--						 S.[ParentStory] <> ''
SELECT * FROM  [dbo].[JIRA_SPRINT] 


--------------------------------------------------------
GO
SELECT * FROM [dbo].[V_JIRA_STORIES]
order by [Key]