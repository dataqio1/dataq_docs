# Data Quality Test Cases - Best Practices Guide

## Data Quality Test Cases - Best Practices Guide

### Introduction

Writing effective data quality test cases is crucial for maintaining data integrity and enabling quick issue resolution. This guide provides best practices with clear examples to help you create actionable and informative test cases.

### Core Principle: Always Return Failed Records

> **Golden Rule:** Your test cases should return the actual records that failed validation, not just counts or boolean results.

#### ✅ **GOOD Example**

```sql
-- Returns all records with invalid ages for inspection
SELECT customer_id, first_name, last_name, age, registration_date
FROM customers 
WHERE age < 0 OR age > 150;
```

**Benefits:**

* See exactly which records are problematic
* Get count of failed records automatically
* Can investigate root causes immediately
* Easy to create fix scripts

#### ❌ **BAD Example**

```sql
-- Only returns a count - no actionable information
SELECT COUNT(*) 
FROM customers 
WHERE age < 0 OR age > 150;
```

**Problems:**

* Cannot identify which records failed
* No way to investigate specific issues
* Requires additional queries to find problems

***

### Best Practice Categories

### 1. Null Value Validation

#### ✅ **GOOD: Identify Records with Missing Critical Data**

```sql
-- Returns records missing required information
SELECT order_id, customer_id, order_date, total_amount, status
FROM orders 
WHERE customer_id IS NULL 
   OR order_date IS NULL 
   OR total_amount IS NULL;
```

**Sample Output:**

| order\_id | customer\_id | order\_date | total\_amount | status  |
| --------- | ------------ | ----------- | ------------- | ------- |
| ORD-001   | NULL         | 2024-01-15  | 99.99         | pending |
| ORD-002   | CUST-123     | NULL        | 149.50        | shipped |

#### ❌ **BAD: Using Boolean Logic**

```sql
-- Returns TRUE/FALSE - not helpful for fixing issues
SELECT 
  CASE WHEN COUNT(*) > 0 THEN 'FAIL' ELSE 'PASS' END as test_result
FROM orders 
WHERE customer_id IS NULL OR order_date IS NULL;
```

### 2. Data Type and Format Validation

#### ✅ **GOOD: Show Invalid Email Formats**

```sql
-- Returns records with malformed email addresses
SELECT user_id, username, email, registration_date
FROM users 
WHERE email NOT REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
   OR email IS NULL;
```

**Sample Output:**

| user\_id | username  | email           | registration\_date |
| -------- | --------- | --------------- | ------------------ |
| U001     | johndoe   | invalid-email   | 2024-01-10         |
| U002     | janesmith | jane@incomplete | 2024-01-12         |

#### ❌ **BAD: Count-Based Validation**

```sql
-- Provides no insight into what emails are invalid
SELECT COUNT(*) as invalid_emails
FROM users 
WHERE email NOT REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$';
```

### 3. Range and Boundary Validation

#### ✅ **GOOD: Identify Out-of-Range Values**

```sql
-- Shows products with unrealistic prices
SELECT product_id, product_name, category, price, last_updated
FROM products 
WHERE price <= 0 
   OR price > 100000
   OR price IS NULL;
```

**Sample Output:**

| product\_id | product\_name | category    | price  | last\_updated |
| ----------- | ------------- | ----------- | ------ | ------------- |
| P001        | Laptop Pro    | Electronics | -99.99 | 2024-01-15    |
| P002        | Gold Watch    | Jewelry     | 999999 | 2024-01-10    |

#### ✅ **GOOD: Date Range Validation**

```sql
-- Finds impossible or suspicious dates
SELECT employee_id, first_name, last_name, birth_date, hire_date
FROM employees 
WHERE birth_date > CURRENT_DATE
   OR hire_date > CURRENT_DATE
   OR DATEDIFF(hire_date, birth_date) < 16*365; -- Hired before age 16
```

### 4. Referential Integrity Checks

#### ✅ **GOOD: Find Orphaned Records**

```sql
-- Shows orders without valid customers
SELECT o.order_id, o.customer_id, o.order_date, o.total_amount
FROM orders o
LEFT JOIN customers c ON o.customer_id = c.customer_id
WHERE c.customer_id IS NULL;
```

**Sample Output:**

| order\_id | customer\_id | order\_date | total\_amount |
| --------- | ------------ | ----------- | ------------- |
| ORD-999   | CUST-INVALID | 2024-01-15  | 299.99        |

#### ✅ **GOOD: Find Missing Parent Records**

```sql
-- Shows order items without corresponding orders
SELECT oi.item_id, oi.order_id, oi.product_id, oi.quantity
FROM order_items oi
LEFT JOIN orders o ON oi.order_id = o.order_id
WHERE o.order_id IS NULL;
```

### 5. Duplicate Detection

#### ✅ **GOOD: Show Duplicate Records with Details**

```sql
-- Shows all duplicate email records for investigation
SELECT user_id, email, username, registration_date, status
FROM users u1
WHERE EXISTS (
    SELECT 1 FROM users u2 
    WHERE u1.email = u2.email 
    AND u1.user_id != u2.user_id
)
ORDER BY email, registration_date;
```

**Sample Output:**

| user\_id | email          | username | registration\_date | status  |
| -------- | -------------- | -------- | ------------------ | ------- |
| U001     | john@email.com | johndoe1 | 2024-01-10         | active  |
| U005     | john@email.com | johndoe2 | 2024-01-15         | pending |

#### ❌ **BAD: Only Count Duplicates**

```sql
-- Tells you there are duplicates but not which ones
SELECT email, COUNT(*) as duplicate_count
FROM users 
GROUP BY email 
HAVING COUNT(*) > 1;
```

### 6. Cross-Table Consistency

#### ✅ **GOOD: Validate Calculated Fields**

```sql
-- Shows orders where line item totals don't match order total
WITH order_totals AS (
    SELECT 
        order_id,
        SUM(quantity * unit_price) as calculated_total
    FROM order_items 
    GROUP BY order_id
)
SELECT 
    o.order_id,
    o.total_amount as recorded_total,
    ot.calculated_total,
    (o.total_amount - ot.calculated_total) as difference
FROM orders o
JOIN order_totals ot ON o.order_id = ot.order_id
WHERE ABS(o.total_amount - ot.calculated_total) > 0.01;
```

### 7. Text and String Validation

#### ✅ **GOOD: Find Invalid Characters or Formats**

```sql
-- Shows product names with special characters or formatting issues
SELECT product_id, product_name, category
FROM products 
WHERE product_name REGEXP '[^A-Za-z0-9 \-\(\)]'  -- Invalid characters
   OR LENGTH(product_name) < 3                    -- Too short
   OR product_name LIKE '% %'                     -- Multiple spaces
   OR product_name LIKE ' %'                      -- Leading space
   OR product_name LIKE '% ';                     -- Trailing space
```

#### ✅ **GOOD: Phone Number Format Validation**

```sql
-- Shows improperly formatted phone numbers
SELECT customer_id, first_name, last_name, phone_number
FROM customers 
WHERE phone_number IS NOT NULL
  AND phone_number NOT REGEXP '^[\+]?[1-9]?[0-9]{7,15}$';
```

### 8. Temporal Logic Validation

#### ✅ **GOOD: Check Date Sequence Logic**

```sql
-- Shows orders where ship date is before order date
SELECT order_id, order_date, ship_date, status, customer_id
FROM orders 
WHERE ship_date < order_date
   OR (status = 'shipped' AND ship_date IS NULL)
   OR (status = 'pending' AND ship_date IS NOT NULL);
```

### 9. Statistical Outlier Detection

#### ✅ **GOOD: Identify Statistical Anomalies**

```sql
-- Shows orders with amounts significantly above normal range
WITH order_stats AS (
    SELECT 
        AVG(total_amount) as avg_amount,
        STDDEV(total_amount) as std_amount
    FROM orders 
    WHERE order_date >= DATE_SUB(CURRENT_DATE, INTERVAL 30 DAY)
)
SELECT 
    o.order_id, 
    o.customer_id, 
    o.total_amount,
    o.order_date,
    ROUND((o.total_amount - os.avg_amount) / os.std_amount, 2) as std_deviations
FROM orders o
CROSS JOIN order_stats os
WHERE o.total_amount > (os.avg_amount + 3 * os.std_amount)  -- 3 standard deviations
ORDER BY o.total_amount DESC;
```

### Writing Effective Test Case Descriptions

#### Template for Test Case Documentation

```markdown
**Test Case:** [Descriptive Name]
**Purpose:** [What data quality issue this detects]
**Expected Result:** No records returned (all data is valid)
**Action Required:** [What to do when records are found]

**SQL Query:**
[Your SQL here]

**Sample Invalid Data:**
[Example of what bad data looks like]
```

#### Example Documentation

```markdown
**Test Case:** Invalid Customer Ages
**Purpose:** Detect customers with impossible age values (negative or over 150)
**Expected Result:** No records returned (all ages are realistic)
**Action Required:** Review data entry process and correct invalid ages

**SQL Query:**
SELECT customer_id, first_name, last_name, age, registration_date
FROM customers 
WHERE age < 0 OR age > 150;

**Sample Invalid Data:**
- Age = -5 (data entry error)
- Age = 999 (system error or test data)
```

### Performance Considerations

#### Use Appropriate Indexing

```sql
-- Ensure indexes exist on frequently tested columns
CREATE INDEX idx_customers_age ON customers(age);
CREATE INDEX idx_orders_dates ON orders(order_date, ship_date);
```

#### Limit Large Dataset Queries

```sql
-- For very large tables, consider adding LIMIT for initial testing
SELECT customer_id, email, registration_date
FROM customers 
WHERE email NOT REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
LIMIT 100;  -- Remove LIMIT for production monitoring
```

### Summary Checklist

✅ **Do:**

* Return actual failed records, not just counts
* Include enough context columns for investigation
* Use descriptive column names
* Document expected results and actions
* Test edge cases and boundary conditions
* Include sample data in documentation

❌ **Don't:**

* Use aggregate functions that hide details
* Write boolean-only tests
* Ignore performance implications
* Skip documentation
* Test only obvious cases
* Use overly complex queries that are hard to maintain

***

_Remember: The goal of data quality testing is not just to detect issues, but to provide actionable information that enables quick resolution and prevents future problems._

