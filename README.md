# Mortal Fibonacci Rabbits

## OVERVIEW
This program computes the total number of rabbit pairs alive after `n` months, given that every pair dies after living exactly `m` months and every mature pair produces one new pair each month.
It is a solution to the **"Mortal Fibonacci Rabbits"** Rosalind problem **(ID: FIBD)**. The tool is simple, efficient, and ideal for practicing recurrence relations, dictionaries, and file handling in Python.

---

## FEATURES
- Reads `n` (number of months) and `m` (rabbit lifespan in months) from a file (`rosalind_fibd.txt`)
- Computes the surviving rabbit population using a Fibonacci-style recurrence that subtracts pairs that die of old age each month
- Clean, well-commented code with proper functions and type hints

---

## ⚠️ IMPORTANT NOTE
> <u>**!!!Please put the input file with name rosalind_fibd.txt in the same folder as the code, otherwise you will receive an Error File Not Found!!!**</u>

---

## EXAMPLE
**Input** (rosalind_fibd.txt):
```
6 3
```
**Output:**
```
4
```

---

## HOW IT WORKS
1. The program reads `n` and `m` from the input file
2. It tracks the number of pairs alive at the end of each month in a `history` dictionary, starting with `history[0] = history[1] = history[2] = 1`
3. For each month `i` from 3 to `n`, it adds last month's pairs plus the new pairs born to pairs that were already mature two months ago, then subtracts whichever pairs turn age `m` and die that month
4. Finally, it prints the total number of surviving rabbit pairs after `n` months

**Worked example** (n=6, m=3):
```
Month:   0  1  2  3  4  5  6
Pairs:   1  1  1  2  2  3  4
```
- Month 3: 1 (month 2) + 1 (month 1) - 0 died = 2
- Month 4: 2 (month 3) + 1 (month 2) - 1 died (the original pair reaches age 3) = 2
- Month 5: 2 (month 4) + 2 (month 3) - 1 died = 3
- Month 6: 3 (month 5) + 2 (month 4) - 1 died = 4

---

## TECHNOLOGIES USED
- **Python**
- **TXT File**
