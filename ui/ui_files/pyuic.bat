@echo off
setlocal enabledelayedexpansion
set ParentPath=.\
for /f "delims=" %%a in ('dir /b "%ParentPath%\*.ui"') do (
set str=%%a
set var=!str:~0,-3!
cmd /v:on  /c pyuic4 -o ..\!var!_ui.py %%a
)