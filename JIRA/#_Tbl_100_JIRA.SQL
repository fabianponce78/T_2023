USE [JIRA]
GO

/****************************************************************************************************************/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[JIRA]') AND type in (N'U'))
DROP TABLE [dbo].[JIRA]
GO
/****************************************************************************************************************/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[JIRA](
	[Issue_Type] [nvarchar](50) NULL,
	[Summary] [nvarchar](200) NULL,
	[Key] [nvarchar](50) NULL,
	[Assignee] [nvarchar](50) NULL,
	[Reporter] [nvarchar](50) NULL,
	[Priority] [nvarchar](50) NULL,
	[Status] [nvarchar](50) NULL,
	[Resolution] [nvarchar](50) NULL,
	[Created] [datetime2](7) NULL,
	[Updated] [datetime2](7) NULL,
	[Due_date] [nvarchar](50) NULL,
	[parent] [nvarchar](50) NULL,
	[Resolved] [datetime2](7) NULL,
	[Status_Category_Changed] [datetime2](7) NULL,
	--[Linked_Issues] [nvarchar](50) NULL,
	--[Parent_Link] [nvarchar](1) NULL
) ON [PRIMARY]
GO
/****************************************************************************************************************/
SELECT * FROM [dbo].[JIRA]