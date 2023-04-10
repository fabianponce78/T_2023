USE	[JIRA]
GO
--------------------------------------------------------
if exists(select 1 from sys.views where name='V_JIRA_DONE_Last8d' and type='v')
drop view V_JIRA_DONE_Last8d;
go
--------------------------------------------------------
create view V_JIRA_DONE_Last8d
as
--------------------------------------------------------

SELECT        TOP (1000) DT, DT_SPRINT, SPRINT, Issue_Type, Summary, [Key], Assignee, Reporter, Priority, Status, Resolution, Created, Updated, Due_date, parent, Resolved, Status_Category_Changed, Linked_Issues, Parent_Link, 
                         [Time Resolution]
FROM            dbo.V_JIRA_STORIES
WHERE        (Resolution = 'Done') AND (Resolved >= DATEADD(d, - 7, GETDATE()))

-----[dbo].[V_JIRA_DONE_Last8d]
--------------------------------------------------------