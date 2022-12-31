SELECT ROUND(AVG(estimate), 1) as avg_estimate, student_name
FROM estimates
JOIN students as s ON student_id = s.id
GROUP BY student_name
ORDER BY avg_estimate DESC
LIMIT 5