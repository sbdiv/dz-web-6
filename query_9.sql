SELECT DISTINCT s.name as subject_name
FROM subjects s
JOIN grades g ON s.id = g.subject_id
WHERE g.student_id = <student_id>;
