---
title: Questions about TCP/IP and HTTP
---

1. What services does the Internet Protocol (IP) provide?
   [ ] Sends packets of data to another IP address with no guarantee of delivery
   [ ] Provides guaranteed delivery of packets from one host to another
   [ ] Maintains a connection between two hosts
   [ ] Enables routing of packets between networks
   [ ] Detects lost ("dropped") packets and requests retransmission
   [ ] Detects out-of-order packets and reorders them so data is delivered to client in same order it was sent

2. What services do the Transmission Control Protocol (TCP) provide?
   [same choices as question 1]

3. A server may be running many applications that accept TCP/IP packets, such as http, mail, or print services.  How does the server know which packets should go to which application (service)?
   [ ] A port number, included in the packet header 
   [ ] Header line of packet data identifies the service
   [ ] Every service (application) gets a unique IP address
   [ ] TOS (type of service) number in the packet header

4. Suppose you ask your browser to display "http://www.yahoo.com/news/".  In the HTTP request that your browser sends to Yahoo, the first line could be which of these?
   [ ] GET  /www.yahoo.com/news/
   [ ] HTTP /www.yahoo.com/news/
   [ ] POST /www.yahoo.com/news/
   [ ] GET /news/  HTTP/1.1
   [ ] GET http://www.yahoo.com/news HTTP/1.1

5. The HTTP protocol has several request *methods*.  Which method would you (or your browser) use to upload a photo to a server?
   [ ] GET
   [ ] PUT
   [ ] POST
   [ ] UPLOAD
   [ ] XFER

6. An HTTP Response includes a status code.  The codes are divided into 6 categories based on the first digit.  For example 2xx codes mean Success.
Which of the following is NOT a category of HTTP status codes?
   [ ] Redirection, resource moved
   [ ] Network Error
   [ ] Informational
   [ ] Informational
   [ ] Server error

---

8. Much of the web is switching from HTTP to the HTTPS protocol.  If you enter "http://www.yahoo.com" in your browser, the Yahoo web server will tell your browser go to "https://www.yahoo.com" instead.  Using only the standard HTTP protocol (no recent extensions like HSTS), how does a web server do this?
   ______________________________________________________________


9. What is the purpose of Domain Name Service (DNS)?
   [ ] verify the identity of web servers
   [ ] translate host names to IP addresses
   [ ] translate IP addresses to host names
   [ ] verify the validity of IP addresses and host names

10. Which of these are standard network services that use TCP/IP.
   [ ] ftp (file transfer protocol)
   [ ] ssh (secure shell)
   [ ] smtp (simple mail transport protocol)
   [ ] gmail (Google mail protocol)
   [ ] html (hypertext markup language)
   [ ] http (hypertext transport protocol)
   [ ] ssl (secure socket layer) and tls (transport layer security)
   [ ] Real Time Streaming Protocol (RTSP) for streaming video
 
