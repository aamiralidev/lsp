# Text Document / Declaration

The `textDocument/declaration` request in the Language Server Protocol (LSP) is used to navigate to the declaration of a symbol (variable, function, class, etc.) from its usage.

## Purpose

The `textDocument/declaration` command mainly focuses on navigating from a symbol's usage to its formal declaration. It is particularly valuable in aiding developers understand and navigate large codebases more efficiently.

## Example Scenario

Assume we have a function `calculateSum` that has been defined in the project and used in several locations. We want to navigate to the declaration of `calculateSum` from one of its usage instance.

## Request Structure

The request for `textDocument/declaration` usually includes the text document identifier and the position within the document where the symbol is being used.

**Request:**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "textDocument/declaration",
  "params": {
    "textDocument": {
      "uri": "file:///path/to/application.js"
    },
    "position": {
      "line": 65,
      "character": 7
    }
  }
}
```

In this request:
- `textDocument` specifies the uri of the file where the symbol is used.
- `position` indicates where the symbol is referenced within the file.

## Response Structure

The response for `textDocument/declaration` will identify the location where the symbol was formally declared.

**Response:**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": [
    {
      "uri": "file:///path/to/mathUtils.js",
      "range": {
        "start": {
          "line": 22,
          "character": 4
        },
        "end": {
          "line": 27,
          "character": 5
        }
      }
    }
  ]
}
```

In this response:
- `uri` specifies the location of the file where the symbol is declared.
- `range` determines the specific location within the file where the symbol is declared.

## Summary

The `textDocument/declaration` request in LSP is a useful mechanism for providing features like 'Go to Definition' in Integrated Development Environments (IDEs), making it easier for developers to navigate and understand large codebases.