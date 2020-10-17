---
title: Feedback on Code Warm Up Quiz
---

Grading:
| Description | Points |
|-------------|--------|
| Code Correct|    10  |
| Code Quality|     6  |
| Comments    |     4  |


* Changing Method Signature. This is wrong because is forces a change in any ocde that calls this method, including `main`.
```java
public void readfile(String filename) throws FileNotFoundException {
```

* Exit instead of return:

```java
try(FileInputStream in = new FileInputStream(filename);
    ...;
   } {

}
catch(FileNotFoundException ex) {
    System.out.println("File not found "+filename);
    System.exit(0);     // NOT SAME as "return"
}
```

* Reading entire file at once can use lots of memory and unnecessary:
```python
in = open(filename, 'r')
data = in.read().splitlines()
```

* Python not catching FileNotFound error:
```python
def readfile(self, filename):
    in = open(filename, 'r')
```

* Python not closing file when done:
```python
def readfile(self, filename):
    """Read numbers from a file and compute sum and count.

    Arguments:
       filename - name of file to read
    """
    try:
        file = open(filename, 'r')
    except FileNotFoundError:
        print("File not found", filename)
        return
    for line in file:
        # process each line
    # close the file to free resources
    file.close()
```


