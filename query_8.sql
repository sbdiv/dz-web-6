SELECT AVG(g.grade) as avg_grade
FROM grades g
JOIN subjects s ON g.subject_id = s.id
WHERE s.teacher_id = <teacher_id>;
