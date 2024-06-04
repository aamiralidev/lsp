### Text Document / Hover

The `textDocument/hover` request in the Language Server Protocol (LSP) is used to request hover information for a given text position within a document. It typically fetches things like documentation or brief descriptions about symbols in the code.

#### Purpose

The `textDocument/hover` command provides a way to help developers understand the purpose of a particular piece of code without having to navigate away from their current position. This information often includes function signatures, types, short descriptions, or relevant documentation.

#### Example Scenario

Imagine you are a developer working in an IDE, you are reading through a section of code and come across a function called `calculateSum()`. You can't remember what this function does. Here the `textDocument/hover` feature can provide you with a brief description of the `calculateSum` function when you hover over it with your mouse.

#### Request Structure

The request for `textDocument/hover` typically includes the text document identifier and the position within the document.

**Request:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "textDocument/hover",
  "params": {
    "textDocument": {
      "uri": "file:///path/to/billing.js"
    },
    "position": {
      "line": 10,
      "character": 4
    },
  }
}
```

In this request:
- `uri` specifies the location of the file.
- `position` specifies the location within the document where the cursor is hovering.

#### Response Structure

The response will include the range and the contents of the hover, which can be either a `MarkupContent` or a `MarkedStrings`.

**Response:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "contents": {
      "kind": "markdown",
      "value": "Function `calculateSum`\n\nCalculates the sum of two numbers."
    },
    "range": {
      "start": {
        "line": 10,
        "character": 4
      },
      "end": {
        "line": 10,
        "character": 16
      }
    }
  }
}
```

In this response:
- `contents` provides the documentation or description of the function or term in question.
- `range` represents the range where the hover request was made within the document.

### Summary

The `textDocument/hover` request in LSP is primarily used to request information about a symbol or piece of code in a document. This proves useful as developers navigate their codebase, providing instant access to valuable details without the need to seek out external resources. This feature enhances productivity and code comprehension.
