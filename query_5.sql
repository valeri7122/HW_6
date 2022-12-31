SELECT teacher_name, subject
FROM teachers as t
LEFT JOIN subjects as sub ON t.id = teacher_id
WHERE teacher_name = 'Jacob Becker'