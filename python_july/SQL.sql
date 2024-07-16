
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


-- 1251. Average Selling Price
SELECT p.product_id, 
        ROUND(COALESCE(
            SUM(p.price * u.units) / sum(u.units),0)
            , 2) as average_price

FROM Prices p
LEFT JOIN UnitsSold u on p.product_id = u.product_id 
AND u.purchase_date between p.start_date and p.end_date
Group by p.product_id;


-- 1075. Project Employees I
SELECT project_id, 
        ROUND(
           COALESCE(SUM(experience_years) / COUNT(*) , 0) 
            , 2) AS average_years 
from Project 
JOIN Employee ON Project.employee_id = Employee.employee_id
group by project_id;


-- 1633. Percentage of Users Attended a Contest
SELECT contest_id, 
        ROUND(COALESCE(count(user_id)*100 / (select count(*) FROM Users), 0), 2) as percentage 

FROM Register 
GROUP BY contest_id 
ORDER BY percentage DESC, contest_id ASC;


-- 1211. Queries Quality and Percentage
SELECT query_name, 
        ROUND(COALESCE(sum(rating/position) / count(*), 0), 2) AS quality,
        ROUND(COALESCE(SUM(case when rating<3 then 1 else 0 end) * 100 / count(*),0),2) AS poor_query_percentage 

FROM Queries 
WHERE query_name is not null  
group by query_name;


-- 1193. Monthly Transactions I
select 
    date_format(trans_date, "%Y-%m") as month, 
    country,  
    count(*) as trans_count,  
    sum(case when state = 'approved' then 1 else 0 end) as approved_count, 
    sum(amount) as trans_total_amount, 
    sum(case when state = 'approved' then amount else 0 end) as approved_total_amount
from transactions
group by date_format(trans_date, "%Y-%m"), country;


-- 1174. Immediate Food Delivery II
SELECT 
    ROUND(SUM(CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END) * 100 / COUNT(*), 2) AS immediate_percentage 
FROM 
    (SELECT 
         customer_id, 
         MIN(order_date) AS first_order_date 
     FROM 
         Delivery 
     GROUP BY 
         customer_id
    ) first_orders
JOIN Delivery D ON D.customer_id = first_orders.customer_id AND D.order_date = first_orders.first_order_date;


DATE_ADD(fl.first_login_date, INTERVAL 1 DAY)  -- increment date
DATE_SUB(fl.first_login_date, INTERVAL 1 DAY)  -- decrement date


-- 550. Game Play Analysis IV
with first_login as (
    select player_id, min(event_date) as first_login_date
    from Activity 
    group by player_id
)

select round(sum(datediff(a.event_date, fl.first_login_date)=1) / count(distinct a.player_id), 2) as fraction
from Activity a
join first_login fl
on a.player_id = fl.player_id;


-- 1070. Product Sales Analysis III
select Sales.product_id, first_year, quantity, price 
from Sales 
join (select product_id, min(year) as first_year 
      from Sales 
      group by product_id) as first_year_sales
on Sales.product_id = first_year_sales.product_id and Sales.year = first_year_sales.first_year;


-- 1141. User Activity for the Past 30 Days I
select 
    activity_date as day, 
    count(distinct user_id) as active_users
from activity
where activity_date between '2019-06-28' and '2019-07-27'   
group by activity_date;


-- 2356. Number of Unique Subjects Taught by Each Teacher
select teacher_id, count(distinct subject_id) as cnt 
from teacher
group by teacher_id;


-- 596. Classes More Than 5 Students
select class 
from Courses
group by class
having count(class) >= 5;


-- 1729. Find Followers Count
select user_id, count(follower_id) as followers_count 
from followers 
group by user_id
order by user_id asc;


-- 619. Biggest Single Number
with number_counts as 
    (select n1.num, count(n2.num) as cnt 
     from mynumbers n1 join mynumbers n2 on n1.num = n2.num 
     group by n1.num)

select coalesce(
    (select num
     from number_counts 
     where cnt = 1 
     order by num desc
     limit 1), null) as num;


-- 1045. Customers Who Bought All Products
select customer_id from customer 
group by customer_id 
having count(distinct product_key) = (select count(product_key) from product);


-- 1978. Employees Whose Manager Left the Company
select e1.employee_id 
from employees e1 
left join employees e2 on e1.manager_id = e2.employee_id 
where e1.salary < 30000 and e1.manager_id is not null and e2.employee_id is null
order by e1.employee_id;


-- 1731. The Number of Employees Which Report to Each Employee
select e1.reports_to as employee_id, 
       e2.name, 
       count(e1.employee_id) as reports_count,
       round(sum(e1.age) / count(e1.employee_id), 0) as average_age
from Employees e1 
join employees e2 
on e1.reports_to = e2.employee_id
group by e1.reports_to
order by employee_id;


-- 610. Triangle Judgement
select x, y, z,
       (case when x < y+z and y < x+z and z < x+y then 'Yes' else 'No' end) as triangle
from triangle;


-- 1789. Primary Department for Each Employee
select employee_id, department_id 
from employee 
where primary_flag='Y' or 
      employee_id in 
      (select employee_id
       from employee 
       group by employee_id 
       having count(department_id)=1);


-- window functions
-- LAG function is used to access data from a previous row in the same result set without the need for a self-join.
-- LEAD function is used to access data from a subsequent row in the same result set without the need for a self-join.
-- LEAD(column_name, offset, default_value) OVER (PARTITION BY partition_column ORDER BY order_column)

-- column_name: The column from which to retrieve data.
-- offset: The number of rows forward from the current row (default is 1 if omitted).
-- default_value: A value to return if the specified offset goes out of the bounds of the partition (optional).
-- PARTITION BY: Divides the result set into partitions to which the function is applied (optional).
-- ORDER BY: Specifies the logical order in which the operation is performed.


-- 180. Consecutive Numbers
with consecutive as (
    select num,
       id, 
       lead(num, 1) over(order by id) num1,
       lead(num, 2) over(order by id) num2, 
       lead(id, 1) over(order by id) id1,
       lead(id, 2) over(order by id) id2
    from logs)

select distinct num as ConsecutiveNums 
from consecutive 
where num=num1 and num=num2 and id1=id+1 and id2=id+2;


-- 1164. Product Price at a Given Date
select distinct product_id, 10 as price 
from products 
group by product_id
having min(change_date) > '2019-08-16'

union

select p.product_id, p.new_price as price
from products p
join (select product_id, max(change_date) as latest_date
      from products 
      where change_date <= '2019-08-16'
      group by product_id) p2 
on p.product_id = p2.product_id and p.change_date = p2.latest_date;


-- 1204. Last Person to Fit in the Bus
select q1.person_name 
from queue q1 
join queue q2 on q1.turn >= q2.turn 
group by q1.turn 
having sum(q2.weight) <= 1000
order by sum(q2.weight) desc
limit 1;


-- 1907. Count Salary Categories
with categories as (select account_id, 
    (case when income < 20000 then 'Low Salary' else 
         case when income > 50000 then 'High Salary' else 'Average Salary' end
     end) category
from accounts),

category_counts as (
    select category, count(account_id) as accounts_count
    from categories 
    group by category),

all_categories AS (
    SELECT 'Low Salary' AS category
    UNION ALL
    SELECT 'Average Salary'
    UNION ALL
    SELECT 'High Salary'
)

select ac.category, coalesce(cc.accounts_count, 0) as accounts_count
from all_categories ac
left join category_counts cc 
on ac.category = cc.category;


-- 1667. Fix Names in a Table
select user_id, 
        concat(upper(left(name, 1)), lower(substring(name, 2))) as name 
from Users
order by user_id;