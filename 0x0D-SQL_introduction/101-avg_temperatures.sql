-- Displays avg temp by city ordered
-- by temperature descending
SELECT city, AVG(temp)
AS avg_temp
GROUP BY city
ORDER BY avg_temp DESC;
