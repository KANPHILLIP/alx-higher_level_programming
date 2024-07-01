-- script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)

USE hbtn_0c_0
SELECT city, AVG(temperature) AS avg_temp
FROM temperatures
WHERE MONTH(date) IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
