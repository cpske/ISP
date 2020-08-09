---
title: Programming Warm-up
---

## Instructions

You can do this assignment in either Java or Python.
In either language, write good quality code, including
documentation in code. 

1. Clone the starter code from Github.
2. Write a class name Counter that reads data from one or more files.  
3. The Counter class's `readfile` method sums data values read from a file and counts how many values have been read.
3. Each line in a data file is either 
   - blank line (skip blank lines)
   - comment line starting with '#' (skip comment lines)
   - data line containing a single number
4. Use the Main class (Java) or main.py (Python) to run your class. `main` uses command line arguments as name(s) of data file(s) to read.
5. Use the Java or Python language standard naming and coding convention. (*This should be something you always do.*) 
6. Push your source code to Github.

Java: 
```shell
cmd> java Main sample.txt
Total of 5 values is xxx.xx
```

Python: 
```shell
cmd> python main.py sample.txt
Total of 5 values is xxx.xx
```

`rainfall.txt` contains monthly rainfall data for Bangkok.

### Java

Class `Counter` should contain these methods:

<table border="1">
<tr valign="top">
<td markdown="span" width="30%">
readfile(String filename)
</td>
<td markdown="span">
Reads data values from a file and add them to the sum and count.<br/> 
If the file doesn't exist then print "File not found: *filename*" and return.
</td>
</tr>
<tr valign="top">
<td markdown="span">
int getCount()
</td>
<td>
Return the number of values read so far.
</td>
</tr>
<tr valign="top">
<td markdown="span">
double getTotal()
</td>
<td>
Return the total of values read so far.
</td>
</tr>
</table>

### Python

Class `Counter` should contain one method and two properties:

<table border="1">
<tr valign="top">
<td markdown="span" width="30%">
readfile(filename: str)
</td>
<td markdown="span">
Reads data values from a file and add them to the total and count.<br/> 
If the file doesn't exist then print "File not found: *filename*" and return.
</td>
</tr>
<tr valign="top">
<td markdown="span">
count
</td>
<td>
A read-only property for the count of values read.
</td>
</tr>
<tr valign="top">
<td markdown="span">
total
</td>
<td>
A read-only property for the sum of values read.
</td>
</tr>
</table>

You can define a property as a method with the `@property` annotation.
