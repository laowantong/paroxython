-- SQLite
select
    name as label,
    group_concat(span, ", ") as spans,
    source
from program
join label using (program)
where name GLOB "*accumulate*"
group by name, program
