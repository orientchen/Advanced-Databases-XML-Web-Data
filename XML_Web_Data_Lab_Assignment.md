# Lab Assignment: XML, XQuery, JSON, and Web Data

## Objective

Complete the hands-on activity in the GitHub repository and demonstrate
your understanding of **XML, XPath, XQuery, JSON, and Web APIs**.

## Instructions

Follow **all steps in the repository `README.md`**. Run the examples
yourself in GitHub Codespaces and make sure you understand the commands
and their results.

## Submission

Submit a **short screen recording (about 4--6 minutes)** demonstrating
your completed work.

Your recording should include the following:

### 1. XML and XPath

-   Show `data/courses.xml`.
-   Run at least **two XPath queries** from the README, including one
    query that uses a predicate.
-   Briefly explain what each query retrieves.

### 2. XQuery

-   Run the **FLWOR query** from the README.
-   Briefly explain the purpose of:
    -   `for`
    -   `where`
    -   `order by`
    -   `return`

### 3. JSON

-   Show `data/courses.json`.
-   Run the `jq` queries from the README.
-   Briefly explain what these expressions mean:
    -   `.courses`
    -   `.courses[] | .title`

### 4. Web API

Start the Web API:

``` bash
python3 api_server.py
```

In a second terminal, demonstrate both requests:

``` bash
curl http://localhost:8000/api/courses
```

``` bash
curl http://localhost:8000/api/courses/CIS680
```

Briefly explain the difference between:

-   `/api/courses`
-   `/api/courses/CIS680`

### 5. Browser Access

-   Open port **8000** using the **Ports** tab in GitHub Codespaces.
-   Open the forwarded address in a Web browser.
-   Add `/api/courses` to the address.
-   Show the JSON response in the browser.

### 6. Final Explanation

At the end of your recording, briefly answer:

> **What is one difference between XML and JSON, and how did you query
> each one in this activity?**

## Recording Guidelines

-   Recommended length: **4--6 minutes**
-   Your recording should clearly show the commands you run and their
    results.
-   Briefly explain what you are doing rather than only running
    commands.
-   You do **not** need to show the Codespace installation/build
    process.
-   Follow the README activity before making your final recording.

## Grading --- 10 Points

  Component                                        Points
  ---------------------------------------------- --------
  XML and XPath demonstration                         2.5
  XQuery / FLWOR demonstration and explanation          2
  JSON / `jq` demonstration and explanation             2
  Web API and browser demonstration                   2.5
  Final explanation and recording completeness          1
  **Total**                                        **10**
