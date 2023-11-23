1. Run 'python linkscanner.py' with no command line argument.
   Should print a usage message.

2. Run 'python linkscanner.py https://cpske.github.io/ISP/testpage.html'

```
10 Valid URLs
https://cpske.github.io/ISP/
https://cpske.github.io/ISP/about         (should be listed only once)
https://cpske.github.io/ISP/topics.html
http://cpske.github.io/ISP/images/SDLC.png
http://cpsek.github.io/ISP/testpage.html
https://bit.ly/isp2023-projects
https://docs.python.org/3/library/urllib.parse.html
http://ku.ac.th/
https://www.cpe.ku.ac.th/
https://www.ku.ac.th/assets/images/header/KU_logo_62x62_th.svg

Require Auth (but may return 404 to HEAD request)
https://classroom.googleapis.com/v1/courses
https://api-m.paypal.com/v1/invoicing/invoices

Bad URLs
https://www.yahoooooooooo.com/
https://cpske.github.io/ISP/htt_ps://foo+bar!
```

A HEAD request to classroom.googleapis.com may return a 400 (Bad Request), so its OK to classify that as a Bad URL.

