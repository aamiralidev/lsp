# Text Document / Prepare Call Hierarchy

The `textDocument/prepareCallHierarchy` request in the Language Server Protocol (LSP) is used to prepare a call hierarchy for a function or method located at a specified text document position. This involves gathering information for a Call Hierarchy Item that can be used for subsequent `call_hierarchy/incomingCalls` or `call_hierarchy/outgoingCalls` requests.

## Purpose

The `textDocument/prepareCallHierarchy` command prepares necessary details for developers to retrieve call hierarchy for a particular function or method, which include incoming and outgoing calls. This is vital for code navigation, refactoring, and comprehending control flow or dependencies in the codebase.

## Example Scenario

Suppose there's a function called `processData` in a file named `dataProcessor.py`. A developer wants to analyze a call hierarchy for this function to understand its ties within the code.

## Request Structure

The request for `textDocument/prepareCallHierarchy` includes the text document identifier and the position within the document where the function or method is defined.

**Request:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "textDocument/prepareCallHierarchy",
  "params": {
    "textDocument": {
      "uri": "file:///path/to/dataProcessor.py"
    },
    "position": {
      "line": 10,
      "character": 2
    }
  }
}
```

In this request:
- `uri` specifies the pathway to the file.
- `position` defines the location in the document where the `processData` function is located.

## Response Structure

The response includes metadata for the function or method used to fetch incoming and outgoing calls later on.

**Response:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": [
    {
      "uri": "file:///path/to/dataProcessor.py",
      "range": {
        "start": {
          "line": 10,
          "character": 2
        },
        "end": {
          "line": 15,
          "character": 4
        }
      },
      "name": "processData",
      "kind": 12,  // Method kind
      "detail": "void processData()"
    }
  ]
}
```

In this response:
- `uri` defines the file in which the function or method is defined.
- `range` identifies the range within the document where the method or function is defined.
- `name` is the label representing the item.
- `kind` is the type of symbol (a method in this scenario).

## Summary

The `textDocument/prepareCallHierarchy` request assists developers to set the stage for subsequent call hierarchy analyses by furnishing necessary metadata about a specific function or method. This LSP command allows for improved code navigation and deeper comprehension of code dependencies.