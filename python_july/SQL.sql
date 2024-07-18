
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


-- 196. Delete Duplicate Emails
with unique_person as (
    select min(id) id
    from Person 
    group by email
)

delete from person where id not in (
    select id from unique_person
);


-- 1527. Patients With a Condition
select patient_id, patient_name, conditions 
from Patients 
where conditions LIKE '% DIAB1%' or
      conditions LIKE 'DIAB1%';


-- 176. Second Highest Salary
select (
    select distinct salary 
    from Employee 
    order by salary desc
    limit 1 offset 1
) as SecondHighestSalary;


-- 1327. List the Products Ordered in a Period
with order_units as (
    select product_id, sum(unit) unit
    from orders 
    where order_date <= '2020-02-29' and order_date >= '2020-02-01'
    group by product_id
    having unit >= 100
)
select p.product_name, order_units.unit 
from products p
join order_units 
on p.product_id = order_units.product_id;


-- 1484. Group Sold Products By The Date
select sell_date, 
       count(distinct product) as num_sold, 
       group_concat(distinct product order by product  separator ',') as products
from activities 
group by sell_date
order by sell_date;


-- 1517. Find Users With Valid E-Mails
SELECT *
FROM Users
WHERE mail REGEXP '^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode(\\?com)?\\.com$';


-- 626. Exchange Seats
select (
    case 
        when id % 2 = 1 and id = (select max(id) from seat) then id 
        when id % 2 = 1 then id+1
        else id-1 
    end
) as id, student 
from seat
order by id;


-- 1341. Movie Rating
(select name as results 
     from Users join MovieRating on Users.user_id = MovieRating.user_id
     group by MovieRating.user_id
     order by count(movie_id) desc, name
     limit 1)

union all

(select title as results 
     from Movies join MovieRating on Movies.movie_id = MovieRating.movie_id
     where created_at <= '2020-02-29' and created_at >= '2020-02-01'
     group by MovieRating.movie_id
     order by avg(rating) desc, title
     limit 1) 


-- 1321. Restaurant Growth
select 
    distinct c.visited_on,
    (select sum(amount)
     from customer 
     where visited_on between date_sub(c.visited_on, interval 6 day) and c.visited_on) as amount,
    
    round(
        (select sum(amount)/7
         from customer 
         where visited_on between date_sub(c.visited_on, interval 6 day) and c.visited_on) 
    , 2) as average_amount

from customer c
where visited_on >= (select date_add(min(visited_on), interval 6 day) from customer);


-- 602. Friend Requests II: Who Has the Most Friends
select  id, count(id) as num 
from (
    select requester_id as id from RequestAccepted 

    union all

    select accepter_id as id from RequestAccepted
) as grouped

group by id
order by num desc
limit 1;


-- 585. Investments in 2016
select round(sum(tiv_2016),2) as tiv_2016
from insurance
where tiv_2015 in 
    (select tiv_2015 
     from insurance 
     group by tiv_2015
     having count(*) > 1)

    and

    (lat, lon) in 
    (select lat, lon from insurance
     group by lat, lon 
     having count(*) = 1); 


-- 185. Department Top Three Salaries
select d.name as Department, 
       e1.name as Employee, 
       e1.salary as Salary
from employee e1 join department d 
on e1.departmentId = d.id
where 3 > (select count(distinct e2.salary)
           from employee e2
           where e2.salary > e1.salary
           and e2.departmentId = e1.departmentId)


-- Use DENSE_RANK() to rank these distinct salaries within each department in descending order.
with unique_ids as (
    select 
        d.name as Department, 
        e.name as Employee, 
        e.salary as Salary, 
        DENSE_RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) AS salary_rank
    from employee e 
    join department d 
    on e.departmentId = d.id
)

select Department, Employee, Salary
from unique_ids
where salary_rank <= 3