@echo off
setlocal
set file=C:\Users\david\Documents\Bath University\assessment_project\budgets.csv

(echo Date, category,amount
echo 01-04-2025,salary,1500
echo 01-04-2025,food,-3.50
echo 02-04-2025,food,-25.00
echo 03-04-2025,transport, -40.00
echo 04-04-2025,Entertainment,-12.99
echo 05-04-2025,food,-8.75
echo 06-04-2025.transport,-2.50
echo 07-04-2025,Entertainment,-10.00 )> "%file%"
pause

echo CSV file has been created.
pause