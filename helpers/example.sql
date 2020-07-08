-- SQLite
SELECT
    name AS taxon,
    program,
    group_concat(span, ", ") AS spans,
    source
FROM program
JOIN taxon USING (program)
WHERE name GLOB "type/non_sequence/dictionary/*"
GROUP BY name, program
