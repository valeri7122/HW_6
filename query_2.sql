SELECT ROUND(AVG(estimate), 1) as avg_estimate, subject, student_name
FROM estimates
JOIN students as s ON student_id = s.id
JOIN subjects as sub ON subject_id = sub.id  
GROUP BY subject, student_name
ORDER BY avg_estimate DESC, student_name
LIMIT 1