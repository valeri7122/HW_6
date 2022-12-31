SELECT teacher_name, ROUND(AVG(estimate), 1) as avg_estimate
FROM estimates
JOIN teachers as t ON teacher_id = t.id
JOIN subjects as sub ON subject_id = sub.id
GROUP BY teacher_name