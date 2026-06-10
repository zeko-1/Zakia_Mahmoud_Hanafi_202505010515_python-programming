## **Activity 1: Identify the Components:**
### What are the Input?
**Answer:**
-Age(To check if age is 13 or older)
-Accompanied by Adult(If age is less than 13 then this input )
-Vaild Ticket(To check the validation of the ticket)
### What is the process?
**Answer:**
```
First check the age if it's 13 or older 
if age < 13 then check if accompanied by adult or not
secound to check whether the ticket is vaild or not

```
## What is the output?
**Answer:**
```
output1: You are allowed to Enter : Enjoy your movie
output2: You are not allowed to Enter
```
## **Activity 2: Design the Algorithm:**
---

### The Flow

![alt text](<Screenshot 2026-06-10 122523.png>)
![alt text](<Screenshot 2026-06-10 122528.png>)

### The Truth Table

| Age ≥ 13 | With Adult | Has Ticket | Entry Allowed |
|-----------|------------|------------|---------------|
| True      | True       | True       | True          |
| True      | False      | True       | True          |
| False     | True       | True       | True          |
| False     | False      | True       | False         |                                                                                                                                           
### Design an Algorithm ##
**Answer:**

Step 1: Start

Step 2: Input data

-Get user’s age → age
-Check if user is accompanied by an adult → accompanied_by_adult (Yes/No)
-heck if user has a valid ticket → valid_ticket (Yes/No)


Step 3: Check ticket first

-If valid_ticket = No
  → Print “Denied (No valid ticket)”
  → End


Step 4: Check age or adult condition

-If age >= 13
    → condition = True
-Else if accompanied_by_adult = Yes
    → condition = True
-Else
    → condition = False


Step 5: Final decision

-If condition = True
    → Print “Allowed to enter”
-Else
    → Print “Denied”


Step 6: End

### Pseudocode ###
START

INPUT age
INPUT accompanied_by_adult
INPUT valid_ticket

IF valid_ticket == No THEN
    PRINT "Denied (No valid ticket)"
ELSE
    IF age >= 13 OR accompanied_by_adult == Yes THEN
        PRINT "Allowed to enter"
    ELSE
        PRINT "Denied"
    ENDIF
ENDIF

END

