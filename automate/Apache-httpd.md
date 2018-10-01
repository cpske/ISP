## Build Apache Httpd (Web Server) from Source

1. Download the source code.
   * Subversion:
   * Github: https://github.com/apache/httpd
   * Github as ZIP: just choose "Download ZIP". Unzip the file.

3. Read the INSTALL file.  This explains how to compile on different OS.

2. On Linux/Unix, Apache using a configuration tool named APR. Download and add the code into your Httpd source code:
```
svn co http://svn.apache.org/repos/asf/apr/apr/branches/1.5.x srclib/apr
svn co http://svn.apache.org/repos/asf/apr/apr-util/branches/1.5.x srclib/apr-util
```
   Apache also requires `libtool`.  I installed the Debian libtool package but buildconf wouldn't use it.
