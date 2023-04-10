USE	[JIRA]
GO
--------------------------------------------------------
if exists(select 1 from sys.views where name='V_JIRA_Wk_Done' and type='v')
drop view V_JIRA_Wk_Done;
go
--------------------------------------------------------
create view V_JIRA_Wk_Done
as
--------------------------------------------------------

SELECT DISTINCT 
Status, 
YEAR(Resolved) AS 'Yr'	,
DATEPART(ww, Resolved) AS Wk, COUNT(*) AS Count
FROM            dbo.V_JIRA_STORIES
WHERE        (Status = 'Done')
GROUP BY Status, YEAR(Resolved),DATEPART(ww, Resolved)


--------------------------------------------------------
GO
SELECT * FROM [dbo].[V_JIRA_Wk_Done]