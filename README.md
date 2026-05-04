# Agentforce-Vibes-Medical-MCP-Server

## Overview

This project implements a **Model Context Protocol (MCP) server** using Python with a **stdio transport layer**. The server is designed to provide structured access to a curated healthcare dataset, including medicine information and a hospital question–answer knowledge base.

The server operates as a local MCP service and can be integrated with MCP-compatible clients such as Salesforce Agentforce (Vibes) to enable intelligent querying and contextual responses.

The system is designed with a clear separation of concerns:

* Application logic implemented in Python
* Static healthcare data embedded within the server
* External knowledge base managed via resource files

---

## Architecture and Design

The MCP server is built using the FastMCP framework and follows a **tool-based interaction model**. It exposes multiple tools and a resource endpoint that can be invoked by MCP clients.

### Key Characteristics

* Transport Type: stdio
* Language: Python
* Framework: FastMCP
* Data Source:

  * In-memory structured medicine dataset (JSON-like Python objects)
  * External text-based knowledge base (patient_qa.txt)

---

## Data Handling

### Medicine Dataset

The medicine data is stored as an in-memory list of dictionaries within the server code. Each record contains detailed attributes such as:

* Name and strength
* Indication and symptoms
* Category and prescription requirements
* Side effects and contraindications
* Drug interactions and alcohol advice
* Stock availability, pricing, and expiry details

This structure enables efficient filtering and retrieval during runtime without requiring external database dependencies.

---

### Hospital Q&A Knowledge Base

The hospital knowledge base is maintained in a separate text file (`patient_qa.txt`) and loaded dynamically at runtime.

* The file contains structured Q&A blocks separated by blank lines
* Each block represents a knowledge unit
* The server reads and processes this file using a custom loader function

This approach allows easy extensibility without modifying the core application logic.

---

## MCP Integration (Agentforce / Vibes)

The server is configured to run as a stdio-based MCP service and can be registered as an external MCP server within an MCP client.

In the context of Salesforce Agentforce (Vibes):

* The MCP client connects to the Python process via stdio
* The server exposes tools and resources
* The client invokes these tools based on user queries
* The server processes requests and returns structured responses

This enables real-time interaction between AI agents and the healthcare dataset.

---

## Available Tools

### list_medicines

Returns a list of all available medicine names.

**Purpose:**
Provides a quick overview of all medicines in the system.

---

### search_medicines

Searches medicines based on name or indication and returns complete details.

**Functionality:**

* Performs case-insensitive matching
* Searches across multiple fields (name and indication)
* Returns full metadata for matched medicines

**Use Case:**
Helps in identifying suitable medicines based on symptoms or keywords.

---

### search_hospital_qa

Searches the hospital knowledge base and returns the most relevant answers.

**Functionality:**

* Splits text into logical blocks
* Matches query keywords against each block
* Scores results based on keyword frequency
* Returns top-ranked responses

**Use Case:**
Provides contextual answers for hospital-related queries.

---

## MCP Resource

### hospital_qa_data

This resource exposes the entire hospital Q&A dataset to the MCP ecosystem.

**Implementation Details:**

* Loaded from external text file
* Served via a resource URI (`hospital://qa-data`)
* Can be accessed by tools or MCP clients directly

**Purpose:**
Separates static knowledge from executable logic, improving maintainability.

---

## Project Structure

```text
ai-medical-mcp-server/
│
├── src/
│   └── medicine_server.py
│
├── data/
│   └── patient_qa.txt
│
├── config/
│   └── mcp_config.json
│
├── README.md
├── requirements.txt
└── .gitignore
```

---



## MCP Client Configuration

Example configuration for connecting this server:

```json
"medicine-mcp-server": {
      "disabled": false,
      "type": "stdio",
      "timeout": 600,
      "command": "python3",
      "args": [
        "/home/codebuilder/dx-project/Medicineserver.py"
      ],
      "description": "Medical MCP Server with medicines and hospital Q&A",
      "autoApprove": [
        "search_hospital_qa",
        "search_medicines",
        "list_medicines"
      ]
    }
```

---

## Conclusion

This project demonstrates how a domain-specific MCP server can be implemented using Python and integrated with AI-driven platforms. It provides a scalable foundation for building healthcare assistants, knowledge systems, and intelligent agent integrations without relying on external APIs or databases.
