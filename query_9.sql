SELECT student_name, subject
FROM estimates
JOIN subjects as sub ON sub.id = subject_id
JOIN students as s ON s.id = student_id
WHERE student_name = 'Kelly Smith'
GROUP BY subject