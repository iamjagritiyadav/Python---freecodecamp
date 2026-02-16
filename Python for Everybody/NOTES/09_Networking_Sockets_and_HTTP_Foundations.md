# Networking, Sockets & HTTP Foundations

This section connects Python with the real world.

Here we move beyond local execution and understand:

* How computers communicate over networks
* What TCP/IP actually does
* How sockets work internally
* How HTTP requests are structured
* Bytes vs text in networking
* How urllib abstracts lower-level networking
* Safe HTML parsing principles

This is foundational for web scraping, APIs, backend systems, and distributed applications.

---

# 1. How the Internet Actually Works (High-Level Model)

All network communication follows a client-server model.

Client:

* Initiates request
* Waits for response

Server:

* Listens on a port
* Processes incoming request
* Sends response

Communication happens using layered protocols.

---

# 2. TCP/IP Model (Conceptual Breakdown)

Networking is layered.

Important layers for us:

1. Application Layer → HTTP
2. Transport Layer → TCP
3. Internet Layer → IP
4. Link Layer → Physical transfer

When you request a webpage:

1. Your system resolves domain via DNS.
2. Establishes TCP connection.
3. Sends HTTP request.
4. Receives HTTP response.
5. Closes connection.

---

# 3. What Is a Socket?

A socket is an endpoint for communication between two machines.

Think of it as:

"A file-like interface for network communication."

In Python:

```python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

AF_INET → IPv4
SOCK_STREAM → TCP

---

# 4. TCP Handshake (Connection Establishment)

TCP uses a three-way handshake:

1. Client → SYN
2. Server → SYN-ACK
3. Client → ACK

After handshake:

Reliable bidirectional communication established.

TCP guarantees:

* Ordered delivery
* No packet loss (retransmission)
* Error checking

---

# 5. Writing a Raw HTTP Request (socket1.py Logic)

Example minimal HTTP request:

```
GET / HTTP/1.1
Host: example.com

```

Important:

* HTTP is text-based protocol.
* Lines separated by CRLF (\r\n).
* Blank line ends header section.

In Python (conceptually):

```python
s.connect(("example.com", 80))
cmd = "GET / HTTP/1.1\r\nHost: example.com\r\n\r\n"
s.send(cmd.encode())
```

Notice:

* We must encode string to bytes.

---

# 6. Bytes vs Strings in Networking

Network communication operates in bytes.

Even if HTTP looks like text, it is transmitted as bytes.

Example:

```python
response = s.recv(512)
```

`recv()` returns bytes.

To convert to string:

```python
response.decode('utf-8')
```

Failing to decode properly causes errors.

---

# 7. HTTP Response Structure

Typical response:

```
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1234

<html>...</html>
```

Two sections:

1. Headers
2. Body (after blank line)

When scraping:

* You often need only body.

---

# 8. Streaming Data from Socket

You must repeatedly call:

```python
while True:
    data = s.recv(512)
    if not data:
        break
```

Because:

* TCP delivers data in chunks.
* You do not know total size beforehand.

---

# 9. urllib – Higher Level Abstraction

`urllib` hides socket-level complexity.

Example:

```python
from urllib.request import urlopen
f = urlopen("http://example.com")
for line in f:
    print(line.decode())
```

Internally it:

* Handles DNS
* Establishes TCP
* Builds HTTP request
* Parses headers
* Returns file-like object

Much safer and cleaner.

---

# 10. Character Encoding in Web Responses

Web servers may send different encodings:

* UTF-8
* ISO-8859-1

Always decode using correct encoding.

Sometimes Content-Type header specifies encoding.

---

# 11. Parsing HTML – Important Warning

HTML is not regular text.

Using regex to parse HTML is dangerous.

Why?

* Nested structure
* Attributes
* Variations in formatting

Better approach:

Use HTML parsers (e.g., BeautifulSoup conceptually).

But understanding raw structure is important.

---

# 12. Link Extraction Logic (urllinks.py Concept)

Typical strategy:

1. Fetch page
2. Parse HTML
3. Extract <a href="...">
4. Follow links

This becomes web crawling.

---

# 13. Network Errors & Robustness

Common issues:

* Timeout
* Connection refused
* DNS failure
* Partial data

Always handle exceptions when doing network operations.

---

# 14. Security Considerations

Never trust:

* External data
* Server responses
* User input

Validate everything.

Avoid blindly executing downloaded content.

---

# 15. Performance Considerations

* Avoid opening too many connections
* Respect rate limits
* Close sockets properly
* Reuse connections when possible

---

# 16. Networking in Data Pipelines

Typical scraping pipeline:

1. Connect to server
2. Send HTTP request
3. Receive response
4. Decode bytes
5. Extract structured data
6. Store in dictionary/list
7. Save to database

This connects networking with previous topics.

---

# Summary

* Networking uses layered protocol model.
* Sockets provide low-level communication endpoint.
* HTTP is text protocol sent over TCP.
* Networking operates on bytes, not strings.
* urllib abstracts complexity.
* HTML parsing must be done carefully.

Understanding sockets and HTTP builds foundation for APIs, scraping, and distributed systems.
