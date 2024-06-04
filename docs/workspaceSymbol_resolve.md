# Workspace Symbol / Resolve

The `workspaceSymbol/resolve` request is part of the Language Server Protocol (LSP) used to retrieve detailed information about a specific workspace symbol. The command is used when additional information about a symbol located in a workspace is required.

## Purpose

The `workspaceSymbol/resolve` command is most useful when the client is interested in detailed information about a workspace symbol, such as its kind, location, and container name. This can be particularly helpful for performing renaming operations or understanding different symbols in the code base.

## Example Scenario

Suppose you have a method named `computeSum` in a TypeScript project, and you want to fetch specific information about this method, such as its location, symbol type, and name of the containing object or class.

## Request Structure

The request for `workspaceSymbol/resolve` typically includes the `symbolInformation` object that identifies the symbol for which more information is required.

**Request:**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "workspaceSymbol/resolve",
  "params": {
    "name": "computeSum",
    "kind": 12,
    "location": {
      "uri": "file:///path/to/project.ts",
      "range": {
        "start": {
          "line": 5,
          "character": 5
        },
        "end": {
          "line": 10,
          "character": 6
        }
      }
    },
    "containerName": "MathOperations"
  }
}
```
In this request:
- `name` is the name of the symbol.
- `kind` is the kind of symbol (in this case, a function or a method).
- `location` indicates denotes the file and the range where the symbol is located.
- `containerName` indicates the name of the container (class, object, etc.) holding the symbol.

## Response Structure

The response to the `workspaceSymbol/resolve` request typically includes the fully populated `SymbolInformation` object.

**Response:**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "name": "computeSum",
    "kind": 12,
    "location": {
      "uri": "file:///path/to/project.ts",
      "range": {
        "start": {
          "line": 5,
          "character": 5
        },
        "end": {
          "line": 10,
          "character": 6
        }
      }
    },
    "containerName": "MathOperations",
    "tags": [],
    "detail": "This function computes the sum of two numbers"
  }
}
```
In this response:
- `name`, `kind`, `location`, and `containerName` return the same fields as queried.
- `tags` is an optional field that retrns the symbol tags if any are associated with the symbol.
- `detail` is a field that may provide additional information about the symbol after the `workspaceSymbol/resolve` request.

## Summary

The `workspaceSymbol/resolve` request in LSP enables developers to fetch detailed information about a specific symbol in a workspace, such as its kind, location, and container name. It's used to gather more knowledge about any symbol in the code, aiding in code understanding and simplifying refactoring operations.