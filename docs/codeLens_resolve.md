# Code Lens / Resolve

The `codeLens/resolve` request in the Language Server Protocol (LSP) is used to compute missing details for a given code lens item. Command resolution is used to avoid computing complex details when they might not be needed (e.g., to improve responsiveness/performance during codeLens computation).

## Purpose

The `codeLens/resolve` command is primarily used to improve performance by allowing the server to initially provide minimal CodeLens data (consisting of range and command, but no command arguments). Then, if a specific CodeLens item is displayed to the user and interaction with it is needed, this command is sent to fetch full command arguments.

## Example Scenario

Imagine you have a JavaScript file and you want to find all dependencies of a function. CodeLens initially provides you the function with an identifier but without details of exactly which dependencies are involved. When you hover over the function name, `codeLens/resolve` is triggered to fetch the detailed information about the dependencies.

## Request Structure

The request for `codeLens/resolve` includes the CodeLens object with minimal information for which full information is required.

**Request:**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "codeLens/resolve",
  "params": {
    "range": {
      "start": {
        "line": 11,
        "character": 2
      },
      "end": {
        "line": 11,
        "character": 15
      }
    },
    "command": {
      "title": "Show Dependencies",
      "command": ""
    },
    "data": {}
  }
}
```

In this request:
- `range` specifies the range in the document where the CodeLens is placed.
- `command` provides the initially calculated command where title is useful to the user even when the command isn't fully resolved, but command doesn't yet contain arguments.

## Response Structure

The response will contain the fully resolved CodeLens item.

**Response:**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "range": {
      "start": {
        "line": 11,
        "character": 2
      },
      "end": {
        "line": 11,
        "character": 15
      }
    },
    "command": {
      "title": "Show Dependencies",
      "command": "extension.showDependencies",
      "arguments": [
        "dependency1", 
        "dependency2"
      ]
    },
    "data": {}
  }
}
```

In this response:
- The `range` remains the same.
- `command` is now fully resolved, providing a concrete command to be executed along with its arguments.

## Summary

The `codeLens/resolve` request in LSP is used for lazily computing detailed CodeLens data. This request is an optimization for responsiveness and performance during CodeLens computation: by allowing minimal data to be initially provided and then resolving the full details only when needed.