# Advanced Databases: XML and Web Data

Hands-on activities for XML, XPath, XQuery, JSON, and Web data management.

## Overview

In this activity, we will use the same course data in different forms to explore:

- XML structure
- XPath queries
- XQuery and FLWOR expressions
- JSON structure
- JSON queries with `jq`
- XML vs. JSON
- Web data and REST APIs

The activity uses GitHub Codespaces. The required tools are already configured in the repository.

---

## 1. Start the Codespace

1. Open this GitHub repository.
2. Click **Code**.
3. Select **Codespaces**.
4. Click **Create codespace on main**.
5. Wait for the Codespace to finish building.

The Codespace automatically installs:

- BaseX for XML, XPath, and XQuery
- `jq` for JSON
- Python for the Web API example
- VS Code XML support

### Verify BaseX

In the terminal, run:

```bash
basex -q"1+2"
```

Expected result:

```text
3
```

The first time BaseX runs, you may also see a message saying that a new configuration file is being created. This is normal.

### Verify jq

```bash
jq --version
```

### Verify Python

```bash
python3 --version
```

---

# Part 1: XML

The file `data/courses.xml` contains course information in XML format.

Open:

```text
data/courses.xml
```

The document contains three courses. For example:

```xml
<course id="CIS680">
    <title>Advanced Databases</title>
    <credits>3</credits>
    <instructor>Dr. Chen</instructor>
</course>
```

Notice the XML structure:

- `courses` is the root element.
- `course` is a repeating element.
- `id` is an attribute of `course`.
- `title`, `credits`, and `instructor` are child elements.

---

# Part 2: XPath

XPath is used to navigate through and select parts of an XML document.

## Query 1: Retrieve all course titles

Run:

```bash
basex -q'doc("data/courses.xml")/courses/course/title'
```

Expected result:

```xml
<title>Advanced Databases</title>
<title>Programming Paradigms</title>
<title>Database Management Systems</title>
```

The XPath:

```text
/courses/course/title
```

follows the XML hierarchy:

```text
courses
   └── course
          └── title
```

---

## Query 2: Filter using an attribute

Retrieve the title of course `CIS680`:

```bash
basex -q'doc("data/courses.xml")/courses/course[@id="CIS680"]/title'
```

Expected result:

```xml
<title>Advanced Databases</title>
```

The predicate:

```text
[@id="CIS680"]
```

means:

> Select a `course` whose `id` attribute is `CIS680`.

---

## Query 3: Filter using a child element

Retrieve the courses taught by Dr. Chen:

```bash
basex -q'doc("data/courses.xml")/courses/course[instructor="Dr. Chen"]/title'
```

Expected result:

```xml
<title>Advanced Databases</title>
<title>Programming Paradigms</title>
```

Compare the two predicates:

```text
[@id="CIS680"]             attribute condition

[instructor="Dr. Chen"]    child-element condition
```

---

# Part 3: XQuery

XPath is useful for selecting XML data. XQuery provides additional capabilities for querying and constructing results.

A common XQuery structure is a **FLWOR expression**:

```text
FOR
LET
WHERE
ORDER BY
RETURN
```

Not every FLWOR expression must use every clause.

## FLWOR Example

Run:

```bash
basex -q'for $c in doc("data/courses.xml")/courses/course where $c/instructor = "Dr. Chen" order by $c/title return $c/title'
```

Expected result:

```xml
<title>Advanced Databases</title>
<title>Programming Paradigms</title>
```

The query can be read as:

```text
for       each course
where     the instructor is Dr. Chen
order by  the course title
return    the title
```

The variable:

```text
$c
```

represents each `course` element being processed.

---

# Part 4: JSON

The file:

```text
data/courses.json
```

contains the same course information represented as JSON.

Open the file and compare it with `courses.xml`.

A course is represented as a JSON object:

```json
{
  "id": "CIS680",
  "title": "Advanced Databases",
  "credits": 3,
  "instructor": "Dr. Chen"
}
```

The courses are stored in an array:

```json
"courses": [
    ...
]
```

---

## Query JSON with jq

`jq` is a command-line tool for working with JSON.

### Query 1: Display the courses array

```bash
jq '.courses' data/courses.json
```

This displays all three course objects.

---

### Query 2: Retrieve all course titles

```bash
jq '.courses[] | .title' data/courses.json
```

Expected result:

```text
"Advanced Databases"
"Programming Paradigms"
"Database Management Systems"
```

Compare this with the XPath query:

```text
XML/XPath:

/courses/course/title
```

```text
JSON/jq:

.courses[] | .title
```

Both retrieve the titles from hierarchical data.

---

### Query 3: Filter by instructor

```bash
jq '.courses[] | select(.instructor == "Dr. Chen") | .title' data/courses.json
```

Expected result:

```text
"Advanced Databases"
"Programming Paradigms"
```

Compare:

```text
XPath:

course[instructor="Dr. Chen"]/title
```

```text
jq:

.courses[] | select(.instructor == "Dr. Chen") | .title
```

---

# Part 5: XML vs. JSON

The XML and JSON files contain the same information but represent it differently.

For example:

### XML

```xml
<course id="CIS680">
    <title>Advanced Databases</title>
    <credits>3</credits>
    <instructor>Dr. Chen</instructor>
</course>
```

### JSON

```json
{
  "id": "CIS680",
  "title": "Advanced Databases",
  "credits": 3,
  "instructor": "Dr. Chen"
}
```

Notice:

| XML | JSON |
|---|---|
| Elements/tags | Objects and key-value pairs |
| Attributes | Usually represented as object properties |
| Repeated elements | Arrays |
| Hierarchical structure | Hierarchical structure |

Both formats can represent semistructured, hierarchical data.

---

# Part 6: Web Data and REST API

So far, we have read XML and JSON directly from files.

Web applications commonly obtain data through a **Web API** instead.

In this section, we will make the JSON course data available through HTTP.

The repository contains:

```text
api_server.py
```

This small Python program provides a Web API for the course data.

---

## Step 1: Start the API server

In the terminal, run:

```bash
python3 api_server.py
```

You should see:

```text
Course API running at http://localhost:8000
```

Leave this terminal running.

The server is now waiting for HTTP requests.

---

## Step 2: Open a second terminal

Click the **+** button in the Terminal panel to open another terminal.

Do not stop the API server in the first terminal.

---

## Step 3: Request all courses

In the second terminal, run:

```bash
curl http://localhost:8000/api/courses
```

The API returns the three courses as JSON.

Conceptually, this sends the HTTP request:

```text
GET /api/courses
```

Important distinction:

```text
GET /api/courses
```

describes the HTTP method and resource.

The actual terminal command we use to send the request is:

```bash
curl http://localhost:8000/api/courses
```

---

## Step 4: Request one specific course

Run:

```bash
curl http://localhost:8000/api/courses/CIS680
```

Expected result:

```json
{
  "id": "CIS680",
  "title": "Advanced Databases",
  "credits": 3,
  "instructor": "Dr. Chen"
}
```

Conceptually, the request is:

```text
GET /api/courses/CIS680
```

Compare the two resources:

```text
/api/courses          collection of courses

/api/courses/CIS680   one specific course
```

---

# Part 7: Access the API from a Web Browser

When the Python server starts, GitHub Codespaces automatically forwards port `8000`.

1. Click the **Ports** tab.
2. Find port **8000**.
3. Find its **Forwarded Address**.
4. Click the globe icon to open it in a browser.

The root address may display:

```text
404 Not Found
```

This is expected because our API does not define a resource for:

```text
/
```

Add:

```text
/api/courses
```

to the end of the forwarded address.

The browser should now display the same JSON course data returned by `curl`.

This demonstrates that different clients can access the same Web API:

```text
Terminal with curl ─┐
                    ├── GET /api/courses ──> Web API ──> JSON
Web browser ────────┘
```

---

# Summary

In this activity, we followed the same course data through several technologies:

```text
XML
 ↓
XPath
 ↓
XQuery / FLWOR

Same data
 ↓
JSON
 ↓
jq

JSON data
 ↓
Web API
 ↓
HTTP GET
 ↓
curl / Web browser
```

Key ideas:

- **XML** represents hierarchical data using elements and attributes.
- **XPath** navigates and selects XML data.
- **XQuery** provides more powerful XML querying, including FLWOR expressions.
- **JSON** represents hierarchical data using objects, arrays, and key-value pairs.
- **jq** can navigate and filter JSON from the command line.
- A **Web API** makes data available to applications over HTTP.
- A REST-style URL can represent a collection such as `/api/courses` or a specific resource such as `/api/courses/CIS680`.

The same underlying information can therefore be represented, queried, exchanged, and accessed in different ways.
