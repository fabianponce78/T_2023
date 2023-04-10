USE	[JIRA]
GO
--------------------------------------------------------
if exists(select 1 from sys.views where name='V_JIRA_Resolved_LW' and type='v')
drop view V_JIRA_Resolved_LW;
go
--------------------------------------------------------
create view V_JIRA_Resolved_LW
as
--------------------------------------------------------

SELECT        DT, DT_SPRINT, SPRINT, ParentStory, Issue_Type, Summary, [Key], Assignee, Reporter, Priority, Status, Resolution, Created, Updated, Due_date, parent, Resolved, Status_Category_Changed, Linked_Issues, Parent_Link, DATEPART(ww, 
                         Created) AS Wk_Created, DATEPART(ww, Resolved) AS Wk_Resolved, DATEPART(ww, Resolved) - DATEPART(ww, Created) AS Wk_Created_Resolved
FROM            dbo.V_JIRA_STORIES
WHERE        
(Status = 'Done') 
AND (DATEPART(ww, Resolved) = DATEPART(ww, GETDATE()) - 2) 
AND (YEAR(Resolved) = YEAR(GETDATE()))


--------------------------------------------------------
GO
SELECT * FROM [dbo].[V_JIRA_Resolved_LW]