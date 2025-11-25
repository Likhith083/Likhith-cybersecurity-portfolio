# **Apply Filters to SQL Queries: Security Incident Investigation**

### **Project Description**

To demonstrate my ability to investigate security incidents using SQL, I simulated a realistic compromised environment. I created a database containing employee records and log-in attempts, populated with diverse data to mimic a real corporate network. My goal was to act as a security analyst investigating suspicious activity. I used SQL filters to isolate specific login anomalies, identifying potential breaches based on time, location, and department access. This project validates my proficiency in using AND, OR, and NOT operators to filter large datasets for threat hunting.

![][image1]

### 

### **Retrieve after hours failed login attempts**

I began by investigating potential unauthorized access attempts that occurred outside of standard business hours. I needed to identify all failed logins that happened after 6:00 PM (18:00).

**![][image2]**

* **Query:**  
* SQL

SELECT \* FROM log\_in\_attempts  
WHERE login\_time \> '18:00' AND success \= 0;

*   
*   
* **Explanation:** I selected all data from the log\_in\_attempts table. I used the WHERE clause with the AND operator to enforce two conditions: the login\_time had to be greater than '18:00', and the success status had to be 0 (indicating failure). This query successfully isolated suspicious attempts made late at night.

### 

### **Retrieve login attempts on specific dates**

A specific security event was flagged on May 9th, 2022\. To understand the scope, I needed to pull all login activity from that day and the day prior (May 8th).

**![][image3]**

* **Query:**  
* SQL

SELECT \* FROM log\_in\_attempts  
WHERE login\_date \= '2022-05-09' OR login\_date \= '2022-05-08';

*   
*   
* **Explanation:** I used the OR operator in my WHERE clause. This told the database to return records if the date matched *either* May 9th *or* May 8th. This broadened my search window to capture the full context of the event.

### 

### **Retrieve login attempts outside of Mexico**

The organization is based in Mexico, so login attempts originating from other countries are treated as suspicious. I needed to filter the logs to show only international traffic.

**![][image4]**

* **Query:**  
* SQL

SELECT \* FROM log\_in\_attempts  
WHERE country NOT LIKE 'MEX%';

*   
*   
* **Explanation:** I used NOT LIKE combined with the wildcard %. The pattern 'MEX%' matches any country starting with "MEX" (like MEX or MEXICO). By adding NOT, I inverted the filter, effectively asking the database to "show me everything that is *not* Mexico." This revealed connections from the USA, Brazil, and Russia.

### 

### **Retrieve employees in Marketing (East Building)**

I needed to perform security updates on machines belonging to the Marketing team, but specifically only those located in the East Building.

**![][image5]**

* **Query:**  
* SQL

SELECT \* FROM employees  
WHERE department \= 'Marketing' AND office LIKE 'East%';

*   
*   
* **Explanation:** I combined an exact match (department \= 'Marketing') with a pattern match (office LIKE 'East%'). The AND operator ensured that only employees satisfying *both* criteria were returned, filtering out Marketing staff in the West building.

### 

### **Retrieve employees in Finance or Sales**

A separate patch was required for all employees in the Finance and Sales departments.

**![][image6]**

* **Query:**  
* SQL

SELECT \* FROM employees  
WHERE department \= 'Finance' OR department \= 'Sales';

*   
*   
* **Explanation:** I used the OR operator to retrieve records where the department was either 'Finance' or 'Sales'. This allowed me to generate a single list of targets for the security patch without running two separate queries.

### 

### **Retrieve all employees not in IT**

Finally, I needed to exclude the Information Technology team from a general policy update, as they had already received it.

**![][image7]**

* **Query:**  
* SQL

SELECT \* FROM employees  
WHERE NOT department \= 'Information Technology';

*   
*   
* **Explanation:** I used the NOT operator to exclude a specific value. The query returned every employee in the database *except* those in the IT department, ensuring the update was applied to the correct general population.

### **Summary**

In this project, I built a SQL environment to simulate a security investigation. I demonstrated how to use AND to be precise (Marketing in East Building), OR to be inclusive (Finance or Sales), and NOT to exclude specific data (Not Mexico, Not IT). These filters are essential for Security Analysts to parse through massive log files and quickly identify threats or isolate user groups for incident response.
