SELECT ROUND(AVG(estimate), 1) as avg_estimate, subject, group_number
FROM estimates
JOIN students as s ON student_id = s.id
JOIN groups as g ON group_id = g.id
JOIN subjects as sub ON subject_id = sub.id  
GROUP BY subject, group_number