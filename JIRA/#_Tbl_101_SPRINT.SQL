USE [JIRA]
GO

/****************************************************************************************************************/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[SPRINT]') AND type in (N'U'))
DROP TABLE [dbo].[SPRINT]
GO
/****************************************************************************************************************/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[SPRINT](
	[DATE] [datetime2](7) NULL,
	[SPRINT] [nvarchar](200) NULL,
	[ParentStory] [nvarchar](200) NULL
) ON [PRIMARY]
GO

/****************************************************************************************************************/
SELECT * FROM [dbo].[SPRINT]