-- Go to UTF8
SELECT city, AVG(value) as avg_temp
FROM temperatures
WHERE month = 1 or month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;

