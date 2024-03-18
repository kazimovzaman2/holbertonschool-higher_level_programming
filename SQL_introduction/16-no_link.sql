-- Score too low
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER by score DESC;

