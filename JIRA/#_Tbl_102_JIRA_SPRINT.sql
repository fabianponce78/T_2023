USE [JIRA]
GO
/****************************************************************************************************************/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[JIRA_SPRINT]') AND type in (N'U'))
DROP TABLE [dbo].[JIRA_SPRINT]
GO
/****************************************************************************************************************/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[JIRA_SPRINT](
	[DT] [varchar](30) NULL,
	[DT_SPRINT] [varchar](30)   NULL,
	[SPRINT] [nvarchar](200)   NULL,
	[ParentStory]  [nvarchar](200)   NULL,
	[Issue_Type] [nvarchar](50)  NULL,
	[Summary] [nvarchar](200)   NULL,
	[Key] [nvarchar](50)  NULL,
	[Assignee] [nvarchar](50)  NULL,
	[Reporter] [nvarchar](50)  NULL,
	[Priority] [nvarchar](50)  NULL,
	[Status] [nvarchar](50)  NULL,
	[Status2] [varchar](7)  NULL,
	[Resolution] [nvarchar](50)  NULL,
	[Created] [varchar](30)  NULL,
	[Updated] [varchar](30)  NULL,
	[Due_date] [nvarchar](50)  NULL,
	[parent] [nvarchar](50)  NULL,
	[Resolved] [varchar](30)  NULL,
	[Status_Category_Changed] [varchar](30)  NULL,
	--[Linked_Issues] [nvarchar](50)  NULL,
	--[Parent_Link] [nvarchar](1)  NULL,
	[Time Resolution] [int] NULL,
	[Wk_Created] [int] NULL,
	[Wk_Resolved] [int] NULL,
	[Wk_Created_Resolved] [int] NULL
) ON [PRIMARY]
GO
/****************************************************************************************************************/
SELECT * FROM [dbo].[JIRA_SPRINT]


