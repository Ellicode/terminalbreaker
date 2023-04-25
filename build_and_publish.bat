@echo off
set /P confirm="[35mDo you really want to build and update terminalbreaker's version?[0m [y/n] : "
IF %confirm% EQU "y" (
    echo [35mSTARTING BUILD...[0m
    py -m build
    echo [35mSTARTING UPLOAD...[0m
    py -m twine upload dist/*      
    echo [35mDONE![0m
) ELSE (
    echo [31mCANCELED BY USER[0m
)
