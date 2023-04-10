 $Folders = Get-ChildItem 'C:\#_FP_APEX\#_DEV\#_Tmp_Test\' -Directory -Name -Recurse

<#
 foreach($Folder in $Folders)
 {
    $Folder = Split-Path -Path $Folder -Leaf

    Write-Host $Folder
 }
 #>
 
 
 Write-Output "=============================================================================" 
  
#Get-ChildItem -Path 'C:\#_FP_APEX\#_DEV\#_Tmp_Test\'


$str_Folder = 'C:\#_FP_APEX\#_DEV\#_Tmp_Test\'
$str_OutFile = 'C:\#_FP_APEX\#_DEV\#_Py_FP\Py_Test\Archivos_IO\Output\APEX_OutFile.txt'
$str_OutFile2 = 'C:\#_FP_APEX\#_DEV\#_Py_FP\Py_Test\Archivos_IO\Output\APEX_OutFile2.txt'


#Get-ChildItem -Recurse "C:\#_FP_APEX\#_DEV\#_Tmp_Test\" | Where { ! $_.PSIsContainer } | Select Name,  FullName,Length

#Get-ChildItem -Recurse "C:\#_FP_APEX\#_DEV\#_Tmp_Test\" | Where { ! $_.PSIsContainer } | Select Name, CreationTime, LastWriteTime,  FullName,Length | Out-File -FilePath #C:\#_FP_APEX\#_DEV\#_Py_FP\Py_Test\Archivos_IO\Output\xxx2.txt

Get-ChildItem -Recurse $str_Folder | Where { ! $_.PSIsContainer } | Select FullName,Name, CreationTime, LastWriteTime,  Length | Out-File -FilePath $str_OutFile




#get-childitem -Recurse $str_Folder | sort-object -property name, creationtime, lastwritetime | Out-File -FilePath $str_OutFile2

#get-childitem -Recurse "C:\#_FP_APEX\#_DEV\#_Tmp_Test\" | sort-object -property name, creationtime, lastwritetime | Out-File -FilePath C:\#_FP_APEX\#_DEV\#_Py_FP\Py_Test\Archivos_IO\Output\xxx.txt



 Write-Output "    :) END" 