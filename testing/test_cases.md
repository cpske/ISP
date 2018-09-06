## unique(list) tests

| Test case      | Input               | Output             |
|----------------|---------------------|--------------------|
| Empty list     | { }                 | empty list         |
| one value      | { a }               | same as input      |
| many copies    | { a, a, a}          | {a}                |
| many elements with dups | {a,b,c,b,d,b,d,c,e,a,a} | {a,b,c,d,e} |
