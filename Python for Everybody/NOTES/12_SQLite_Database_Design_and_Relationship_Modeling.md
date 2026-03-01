
# SQLite Database Design and Relationship Modeling

Focus:

* Relational theory
* Schema design
* Keys and constraints
* Relationship modeling
* Normalization
* Transactions
* Indexing
* Interview-oriented depth

---

# 1. Why Databases Exist

Databases solve:

* Persistent storage
* Structured querying
* Concurrency control
* Data integrity
* Efficient retrieval

Flat files fail when:

* Data grows large
* Relationships exist
* Multiple users access simultaneously

Relational databases provide structured storage using tables.

---

# 2. What Is SQLite?

SQLite is:

* Lightweight
* Serverless
* File-based relational database
* ACID compliant

Unlike MySQL/PostgreSQL:

* No separate server process
* Entire database stored in single file

Used in:

* Mobile apps
* Embedded systems
* Local applications
* Prototyping

---

# 3. Relational Model (Core Theory)

A relational database consists of:

* Tables (relations)
* Rows (tuples)
* Columns (attributes)

Each table represents an entity.

Example:
User table

| id | name | email |

Each row is one user.

Interview Question:
Why is relational model powerful?
Because it enforces structured relationships and supports declarative querying (SQL).

---

# 4. Primary Keys

Primary Key:

* Uniquely identifies each row
* Cannot be NULL
* Must be unique

Example:

CREATE TABLE User (
id INTEGER PRIMARY KEY,
name TEXT
);

In SQLite:
INTEGER PRIMARY KEY becomes auto-increment rowid.

Interview Question:
Why avoid natural keys sometimes?
They may change. Surrogate keys remain stable.

---

# 5. Foreign Keys

Foreign Key establishes relationship between tables.

Example:

CREATE TABLE Post (
id INTEGER PRIMARY KEY,
user_id INTEGER,
FOREIGN KEY (user_id) REFERENCES User(id)
);

This creates one-to-many relationship:
One User → Many Posts

Foreign keys enforce referential integrity.

Must enable in SQLite:
PRAGMA foreign_keys = ON;

---

# 6. Types of Relationships

1. One-to-One
2. One-to-Many
3. Many-to-Many

---

## One-to-Many

User → Posts

User table:
id (PK)

Post table:
user_id (FK)

---

## Many-to-Many

Students ↔ Courses

Solution:
Create junction table.

CREATE TABLE Enrollment (
student_id INTEGER,
course_id INTEGER,
PRIMARY KEY (student_id, course_id),
FOREIGN KEY (student_id) REFERENCES Student(id),
FOREIGN KEY (course_id) REFERENCES Course(id)
);

Junction table stores relationships.

---

# 7. Normalization (Interview Critical)

Normalization reduces redundancy.

1NF:

* Atomic values
* No repeating groups

2NF:

* No partial dependency

3NF:

* No transitive dependency

Example transitive dependency:

Student(id, name, dept_id, dept_name)

Dept_name depends on dept_id, not student.
Should separate into Department table.

Interview Question:
Why normalize?
Avoid duplication, anomalies, inconsistency.

---

# 8. Denormalization

Opposite of normalization.

Used for:

* Performance optimization
* Reducing joins

Tradeoff:
More redundancy, faster reads.

---

# 9. SQL Basics (Essential Commands)

Create table:
CREATE TABLE table_name (...);

Insert:
INSERT INTO table VALUES (...);

Select:
SELECT * FROM table;

Update:
UPDATE table SET column=value WHERE condition;

Delete:
DELETE FROM table WHERE condition;

---

# 10. JOIN Operations

JOIN combines tables.

INNER JOIN:
Returns matching rows.

LEFT JOIN:
Returns all left rows + matching right.

Example:

SELECT User.name, Post.id
FROM User
JOIN Post ON User.id = Post.user_id;

Interview Question:
Difference between INNER and LEFT JOIN?
INNER returns intersection.
LEFT returns all from left, even without match.

---

# 11. Indexing

Index improves query speed.

CREATE INDEX idx_user_email ON User(email);

Index works like:

* B-tree structure
* Faster lookup

Tradeoff:

* Slower inserts
* Extra storage

Interview Question:
Why not index every column?
Increases write cost and storage.

---

# 12. Transactions

Transaction properties (ACID):

A — Atomicity
C — Consistency
I — Isolation
D — Durability

Example:

BEGIN TRANSACTION;
UPDATE Account SET balance = balance - 100 WHERE id=1;
UPDATE Account SET balance = balance + 100 WHERE id=2;
COMMIT;

If error:
ROLLBACK;

Interview Question:
Why transactions matter?
Prevent partial updates and maintain consistency.

---

# 13. Isolation Levels (Conceptual)

Common problems:

* Dirty reads
* Non-repeatable reads
* Phantom reads

SQLite uses SERIALIZABLE by default.

---

# 14. Constraints

NOT NULL
UNIQUE
PRIMARY KEY
FOREIGN KEY
CHECK
DEFAULT

Constraints enforce integrity at database level.
Better than relying only on application logic.

---

# 15. Query Optimization Concepts

Performance factors:

* Index usage
* Query plan
* Avoid SELECT * in production
* Proper WHERE filtering

Use:
EXPLAIN QUERY PLAN

To inspect execution strategy.

---

# 16. Data Modeling Best Practices

1. Define clear entities
2. Choose stable primary keys
3. Normalize until 3NF
4. Add indexes after observing query patterns
5. Enforce constraints

---

# 17. Handling Large Data

* Use pagination (LIMIT, OFFSET)
* Avoid loading entire dataset
* Batch inserts

Example:
SELECT * FROM Post LIMIT 10 OFFSET 20;

---

# 18. Common Interview Questions

1. Difference between primary key and unique?
   Primary key cannot be NULL.
   Unique can allow one NULL (depending on DB).

2. Why use foreign keys?
   To maintain referential integrity.

3. What is normalization?
   Reducing redundancy and dependency.

4. What is ACID?
   Atomicity, Consistency, Isolation, Durability.

5. When use index?
   On frequently searched columns.

6. What is many-to-many relationship?
   Modeled using junction table.

---

# 19. Real-World Data Flow

Application Layer:

* Collect input
* Validate

Database Layer:

* Insert structured data
* Enforce constraints
* Maintain relationships

Analytics Layer:

* Query using JOIN
* Aggregate data

This connects:
OOP + Networking + Data modeling.

---

# Final Understanding

Relational databases store structured data with integrity guarantees.
Primary and foreign keys model relationships.
Normalization prevents redundancy.
Indexes improve performance.
Transactions guarantee consistency.

Mastering relational modeling is essential for backend development, data engineering, and system design interviews.
