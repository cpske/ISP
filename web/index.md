---
title: HTTP and Web Applications
---

The web uses the HTTP protocol for messages, and TCP/IP for transport.
So, it helps to have some understanding of IP, TCP, and HTTP. They are layered protocols - an IP packet contains a TCP packet (segment) which in turn contains an HTTP message.

* Internet Protocol (IP) provides addresses and routing for all traffic on the Internet.
* Transmission Control Protocol (TCP) defines how to maintain a virtual connection or conversation between applications, and adds reliability to IP
* HyperText Transport Protocol (HTTP) defines the format and protocol for communication by web applications and web services.

Presentation: [Introduction to HTTP](HTTP.pdf)    
[HTTP Exercise](HTTP-in-Action.pdf) send and receive HTTP yourself!   
[UC Berkeley Presentation](Intro-web-and-tcp-UCB.pdf) from Edx course on design of long-lasting web apps.

The HTTP exercises require the use of netcat or ncat.

* netcat (nc) is included with Linux and Mac OSX, or add it as a package.
  - for Windows, download netcat from http://netcat.sourceforge.net/
* ncat is a newer reimplementation of netcat that supports TLS/SSL.  It uses the same syntax as netcat, with a few newer options.
  - https://nmap.org/ncat/
  - written by the author of the well-known `nmap` port scanner
* [netcat command summary](netcat_summary_sans.pdf) from SANS Institute

Test that it is working.  In a terminal (shell) window enter:
```
netcat -v -l -p 8000

#  or, if you have ncat installed

ncat -v -l -p 8000
```
then in a web browser, open the URL `http://localhost:8000`.    
You should see some text (HTTP request from web broswer) shown in the netcat window.  
You can close the window or type CTRL-C to kill the netcat process.

## Web Frameworks

A framework provides reusable, customizable software for a particular type of application.
Web Frameworks are the way modern web apps are created; almost no one would try to
write a web app "from scratch", except as a learning project.

**Back-end** frameworks run a a server, handle client requests, manage data, and
contain application logic.  For some apps, a backend framework is all that is needed.

As of 2020, some of the most used frameworks for new applications are:

* Django - Python
* Spring or Spring Boot - Java
* Rails - Ruby
* ASP.net MVC - C# and other .Net languages
* Flask - Python
* Express - Javascript
* Lavarel - PHP

There are (too) many back-end frameworks to list, and search results are biased
in favor of what is *cool* right now.

A **front-end** framework runs on the client, meaning in the web browser, 
to provide a richer user experience and more functionality.
The most popular ones as of 2020, all in Javascript, are:
* React
* Angular and Angular.JS
* Vue.js
These frameworks all require JQuery, which is more a library than a framework.

The Mozilla Develper Network (MDN) has a good series of articles.
[Client-Server Overview](https://developer.mozilla.org/en-US/docs/Learn/Server-side/First_steps/Client-Server_overview) describes HTTP requests and responses, and difference between static and dynamic content.  It then describes what web frameworks do.  They mention Django and Flask for Python.


