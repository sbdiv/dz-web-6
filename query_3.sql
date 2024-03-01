SELECT gr.name as group_name, AVG(g.grade) as avg_grade
FROM groups gr
JOIN students s ON gr.id = s.group_id
JOIN grades g ON s.id = g.student_id
WHERE g.subject_id = <subject_id>
GROUP BY gr.name;
