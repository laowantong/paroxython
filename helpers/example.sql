-- SQLite
SELECT name AS taxon, count(*) AS occurrences
FROM taxon
GROUP BY name
ORDER BY occurrences DESC
LIMIT 50
