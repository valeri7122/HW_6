SELECT student_name, teacher_name, subject
FROM estimates
JOIN students as s ON student_id = s.id
JOIN subjects as sub ON subject_id = sub.id
JOIN teachers as t ON teacher_id = t.id
WHERE student_name = "Robin Koch" AND teacher_name = 'Robert Cameron'
GROUP BY subject 