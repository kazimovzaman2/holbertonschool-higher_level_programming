-- Go to UTF8
SELECT city, AVG(value) as avg_temp
FROM temperature
GROUP BY city
ORDER BY avg_temp DESC;

