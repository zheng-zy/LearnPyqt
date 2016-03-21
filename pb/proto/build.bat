@echo off
set FolderName=%cd%
for /f "delims=\" %%a in ('dir /b /a-d /o-d "%FolderName%\*.proto"') do (
cd /d %cd%
protoc2.6.1.exe --python_out=..\  .\%%a
)

