-- script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
USE hbtn_0c_0
SELECT city, AVG(value)
FROM temperatures
ORDER BY temperature DSC;
