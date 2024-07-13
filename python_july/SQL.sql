
-- 1581. Customer Who Visited but Did Not Make Any Transactions
SELECT customer_id, count(customer_id) as count_no_trans 
FROM Visits 
LEFT JOIN Transactions ON Visits.visit_id = Transactions.visit_id 
WHERE Transactions.visit_id IS NULL
group by customer_id;


-- 197. Rising Temperature
SELECT w1.id FROM Weather w1
join Weather w2 
on w1.recordDate = DATE_ADD(w2.recordDate, INTERVAL 1 DAY) 
where w1.temperature > w2.temperature;


-- 577. Employee Bonus
SELECT Employee.name, Bonus.bonus
FROM Employee
LEFT JOIN Bonus ON Employee.empId = Bonus.empId
WHERE Bonus.bonus IS NULL OR Bonus.bonus < 1000;


-- 570. Managers with at Least 5 Direct Reports
SELECT e2.name 
FROM Employee e1 
JOIN Employee e2 on e1.managerId = e2.id 
GROUP BY e1.managerId
HAVING count(*) > 4;

'''
SELECT COUNT(*) FROM ... statement is used to count the total number of rows returned by a query. 
It does not group rows together but rather provides a single count of all rows that match 
the criteria specified in the query.

GROUP BY with HAVING COUNT(*) allows you to group rows that have the same values into summary rows, 
and then apply a condition to those groups.
'''

-- 1934. Confirmation Rate
SELECT s.user_id, 
    ROUND(
        COALESCE(
            SUM(CASE WHEN c.action = "confirmed" THEN 1 ELSE 0 END) / COUNT(c.user_id)
        , 0), 2)
    as confirmation_rate 

FROM Signups AS s 
LEFT JOIN Confirmations AS c on s.user_id = c.user_id 
GROUP BY s.user_id;


-- 1661. Average Time of Process per Machine
SELECT machine_id, 
    ROUND( SUM(CASE WHEN activity_type='start' THEN timestamp*-1 ELSE timestamp END) / COUNT(DISTINCT process_id)
        , 3) AS processing_time

FROM Activity 
GROUP BY machine_id;


-- 1280. Students and Examinations
SELECT s.student_id, s.student_name, sub.subject_name, IFNULL(grouped.attended_exams, 0) as attended_exams 
FROM Students s 
CROSS JOIN Subjects sub
LEFT JOIN 
    (
        SELECT student_id, subject_name, count(*) as attended_exams
        FROM Examinations 
        GROUP BY student_id, subject_name 
    ) grouped
ON s.student_id = grouped.student_id AND sub.subject_name = grouped.subject_name
ORDER BY s.student_id, sub.subject_name;