### `textDocument/definition` Command in LSP

The `textDocument/definition` request in the Language Server Protocol (LSP) is used to obtain the location(s) that define the symbol denoted by the text under the cursor.

#### Purpose

The command enables developers to quickly navigate to the definition location of a symbol directly from their IDE or text editor. This can be crucial for understanding, navigating and debugging code.

#### Example Scenario

Suppose you are working on a JavaScript file and you encounter a function `processData()`. To understand what this function does, you'd need to navigate to its definition.

#### Request Structure

The request for `textDocument/definition` typically includes the text document identifier and the position (where the cursor is) within the document.

**Request:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "textDocument/definition",
  "params": {
    "textDocument": {
      "uri": "file:///path/to/data.js"
    },
    "position": {
      "line": 14,
      "character": 15
    }
  }
}
```

In this request:
- `uri` specifies the location of the file.
- `position` specifies the location within the document where the cursor is.

#### Response Structure

The response will include a list of locations, each representing a definition of the symbol.

**Response:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": [
    {
      "uri": "file:///path/to/data.js",
      "range": {
        "start": {
          "line": 5,
          "character": 8
        },
        "end": {
          "line": 7,
          "character": 1
        }
      }
    }
  ]
}
```

In this response:
- `uri` indicates the file where the definition is.
- `range` specifies the range in the document where the definition is.

### Summary

The `textDocument/definition` request in LSP allows developers to easily navigate to the definition of a symbol directly from their editor. This boosts productivity by reducing the time spent searching for definitions manually.