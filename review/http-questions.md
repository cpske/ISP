---
title: Questions about TCP/IP and HTTP
---

1. What services does the Internet Protocol (IP) provide? (select all correct answers)
   - [ ] Sends packets of data to another IP address with no guarantee of delivery
   - [ ] Provides guaranteed delivery of packets from one host to another
   - [ ] Maintains a connection between two hosts
   - [ ] Enables routing of packets between networks
   - [ ] Detects lost ("dropped") packets and requests retransmission
   - [ ] Detects out-of-order packets and reorders them so data is delivered to client in same order it was sent

2. What services does the Transmission Control Protocol (TCP) provide?
   - [ ] Sends packets of data to another IP address with no guarantee of delivery
   - [ ] Provides guaranteed delivery of packets from one host to another
   - [ ] Maintains a connection between two hosts
   - [ ] Enables routing of packets between networks
   - [ ] Detects lost ("dropped") packets and requests retransmission
   - [ ] Detects out-of-order packets and reorders them so data is delivered to client in same order it was sent

3. A server may be running many applications that accept TCP/IP packets, such as http, mail, and print services.  When a TCP/IP packet arrives, how does the server know which service should handle the packet?
   - [ ] A port number, included in the packet header 
   - [ ] Header line of packet data identifies the service
   - [ ] Every service (application) gets a unique IP address
   - [ ] TOS (type of service) number in the packet header

4. Suppose you ask your browser to display "http://www.yahoo.com/news/".  In the HTTP request that your browser sends to Yahoo, the first line could be which of these?
   - [ ] GET  /www.yahoo.com/news/
   - [ ] HTTP /www.yahoo.com/news/
   - [ ] POST /www.yahoo.com/news/
   - [ ] GET /news/  HTTP/1.1
   - [ ] GET http://www.yahoo.com/news HTTP/1.1

5. The HTTP protocol has several request *methods*.  Which method would a web app use to upload a photo to a server?
   - [ ] GET
   - [ ] PUT
   - [ ] POST
   - [ ] UPLOAD
   - [ ] SEND

6. An HTTP Response includes a status code.  The codes are divided into 5 categories based on the first digit (1xx, 2xx, etc).
Which of the following is **NOT** a type of HTTP status codes?
   - [ ] Redirect, resource moved
   - [ ] Network Error
   - [ ] Informational
   - [ ] Client Error (Page Not Found, Access Denied)
   - [ ] Server Error

7. What are the names of each of the HTTP status code categories:
   - 1xx `_____________________________________`
   - 2xx `_____________________________________`
   - 3xx `_____________________________________`
   - 4xx `_____________________________________`
   - 5xx `_____________________________________`

8. Much of the web has switched from HTTP to the HTTPS protocol.  If you enter "http://www.yahoo.com" in your browser, the Yahoo web server will tell your browser go to "https://www.yahoo.com" instead.     
   Using only the standard HTTP protocol (no recent extensions like HSTS), how can a web server do this?
   `_____________________________ _____________________________`


10. What is the purpose of Domain Name Service (DNS)?
   - [ ] verify the identity of web servers
   - [ ] translate host names to IP addresses
   - [ ] translate IP addresses to host names
   - [ ] verify the validity of IP addresses and host names


11. Which of these are standard network services that use TCP/IP.
   - [ ] ftp (file transfer protocol)
   - [ ] ssh (secure shell)
   - [ ] smtp (simple mail transport protocol)
   - [ ] gmail (Google mail protocol)
   - [ ] html (hypertext markup language)
   - [ ] http (hypertext transport protocol)
   - [ ] ssl (secure socket layer) and tls (transport layer security)
   - [ ] Real Time Streaming Protocol (RTSP) for streaming video
 
12. Which of the following can be specified using HTTP **header lines**:
    - [ ] Content Length
    - [ ] Content Type (html, text, json, jpeg, etc.)
    - [ ] Destination host name
    - [ ] Sender host name
    - [ ] Acceptable types for the response
    - [ ] Cookies
    - [ ] Priority
    - [ ] Redirect URL