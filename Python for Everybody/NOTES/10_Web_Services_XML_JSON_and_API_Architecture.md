# Web Services, XML, JSON & APIs

## 1. What Is a Web Service?

A web service is a machine-to-machine communication system over a network, typically using HTTP.

Key idea:
Humans consume HTML.
Machines consume structured data (JSON/XML).

A web service:

* Listens for HTTP requests
* Processes input
* Returns structured response

Used in:

* Backend systems
* Microservices
* ML pipelines
* Payment gateways
* Mobile apps

---

## 2. Core Architecture: Client–Server Model

Client:

* Initiates request
* Waits for response

Server:

* Listens on port
* Processes request
* Sends response

Communication is stateless in most modern systems (REST).

Stateless means:
Each request contains all information needed.
Server does not remember previous request context.

Interview Question:
Why is stateless architecture scalable?
Because no session memory is required on server, enabling horizontal scaling.

---

## 3. HTTP Refresher (Critical for Interviews)

HTTP is:

* Application layer protocol
* Text-based
* Runs over TCP

HTTP Request Structure:

METHOD /path HTTP/1.1
Host: example.com
Header: value

[Optional body]

Important HTTP Methods:
GET → Retrieve resource
POST → Create resource
PUT → Replace resource
PATCH → Partial update
DELETE → Remove resource

Interview Trap:
Difference between PUT and PATCH?
PUT replaces entire resource.
PATCH updates partial fields.

---

## 4. Data Serialization

Serialization = Converting structured memory data into transferable format.

Example Flow:
Python dict → JSON string → Sent via HTTP → Parsed back to dict

Why needed?
Because network only transfers bytes.

Opposite process = Deserialization.

Interview Question:
Why not send Python dictionary directly?
Because internal memory representation is language-specific and not standardized.

---

## 5. XML (Deep Understanding)

XML is:

* Hierarchical
* Tag-based
* Self-descriptive
* Extensible

Example:

<user id="101">
    <name>Jagriti</name>
    <age>20</age>
</user>

Properties:

* Supports attributes
* Supports namespaces
* Supports schema validation (XSD)
* Verbose

Advantages:

* Strict structure
* Strong validation

Disadvantages:

* Large payload size
* Slower parsing
* Harder to read

Used in:

* SOAP APIs
* Enterprise systems
* Banking integrations

---

## 6. XML Parsing Internals

XML is parsed into a tree structure.

DOM (Document Object Model):
Loads entire XML into memory.

SAX (Simple API for XML):
Event-driven parsing.
Lower memory usage.

Python ElementTree:

* Parses into tree
* Allows traversal

Interview Question:
Why is SAX more memory efficient?
Because it does not load full document into memory.

---

## 7. JSON (Deep Understanding)

JSON is:

* Lightweight
* Key-value structured
* Language independent
* Based on JavaScript object syntax

Example:

{
"user": {
"name": "Jagriti",
"age": 20,
"skills": ["Python", "ML"]
}
}

Mapping to Python:
Object → dict
Array → list
String → str
Number → int/float
Boolean → bool
Null → None

Interview Question:
Why is JSON preferred over XML?
Smaller size, faster parsing, direct mapping to native structures.

---

## 8. JSON Parsing Risks

Common mistakes:

* Assuming key always exists
* Ignoring nested structure
* Not validating types

Safer access:
info.get("key")

Why?
Prevents KeyError.

---

## 9. REST Architecture (Interview Core)

REST = Representational State Transfer

Principles:

1. Stateless
2. Client-server separation
3. Uniform interface
4. Resource-based URLs
5. Uses HTTP methods properly

Example Resource URL:
/users/101

Good API Design:
GET /users
GET /users/101
POST /users
DELETE /users/101

Interview Question:
Why is REST scalable?
Stateless + cacheable responses + layered architecture.

---

## 10. HTTP Status Codes (Must Memorize)

1xx → Informational
2xx → Success
200 → OK
201 → Created
204 → No content

3xx → Redirection

4xx → Client error
400 → Bad request
401 → Unauthorized
403 → Forbidden
404 → Not found
429 → Too many requests

5xx → Server error
500 → Internal error
503 → Service unavailable

Interview Question:
Difference between 401 and 403?
401 = authentication required.
403 = authenticated but not allowed.

---

## 11. API Authentication Mechanisms

1. API Keys
2. Bearer Tokens (JWT)
3. OAuth

JWT (JSON Web Token):

* Header
* Payload
* Signature

Why signature?
To prevent tampering.

Never store API keys in:

* Public repos
* Client-side code

---

## 12. Rate Limiting

Servers limit number of requests.

Why?

* Prevent abuse
* Ensure fairness
* Protect infrastructure

Common limit response:
429 Too Many Requests

Interview Question:
How do you handle rate limiting?

* Exponential backoff
* Retry after delay
* Respect Retry-After header

---

## 13. Error Handling Strategy

Robust API consumer must:

1. Check HTTP status
2. Validate JSON structure
3. Handle missing fields
4. Catch network errors
5. Implement retries

Never assume:
Response always correct.

---

## 14. Performance Considerations

1. Minimize API calls
2. Use caching
3. Use pagination
4. Compress payloads (gzip)
5. Use connection pooling

Why pagination?
Avoid large memory usage and timeout issues.

---

## 15. Security Concepts

1. Validate all external data
2. Avoid injection vulnerabilities
3. Use HTTPS
4. Protect secrets
5. Avoid exposing internal structure

Interview Question:
Why is HTTPS mandatory for APIs?
Encrypts data in transit using TLS.

---

## 16. Real-World Integration Pipeline

Complete pipeline:

1. DNS resolution
2. TCP handshake
3. Send HTTP request
4. Receive response (bytes)
5. Decode
6. Deserialize JSON/XML
7. Extract fields
8. Validate
9. Store in DB
10. Process for analytics/ML

This connects:
Networking + Data Structures + Databases + Security.

---

## 17. Common Interview Questions Summary

1. Difference between REST and SOAP?
   SOAP uses XML, strict protocol.
   REST uses HTTP, flexible, lightweight.

2. Why is JSON faster than XML?
   Less verbose + easier parsing.

3. What makes REST stateless?
   Server does not store client session.

4. How do you secure APIs?
   HTTPS + Authentication + Rate limiting.

5. What happens if JSON structure changes?
   Your parser may break. Must validate.

---

## Final Understanding

Web services enable machine communication.
Data must be serialized.
JSON dominates modern APIs.
REST defines architectural principles.
Security and robustness are critical.
Understanding this layer is mandatory for backend, ML systems, cloud engineering, and system design interviews.
