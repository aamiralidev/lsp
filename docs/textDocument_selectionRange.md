### Text Document / Selection Range

The `textDocument/selectionRange` request is part of the Language Server Protocol (LSP). It's used to obtain selection ranges for given positions in a text document. Selections are typically used for features like 'Expand/Shrink Selection' in text editors or IDEs.

#### Purpose

The `textDocument/selectionRange` request allows developers to easily increase or decrease the range of their current selection in a structured manner, such as expanding a selection from a variable to its containing method, class, or even the entire file. This can be especially helpful when wanting to refactor or move large pieces of code.

#### Example Scenario

Consider you have your cursor positioned on a variable `total` within a function `calculateTotal` in a file named `billing.js`. You want to expand your selection to encompass the entire function.

#### Request Structure

The request for this command includes the text document identifier and positions for which the selection ranges are needed.

**Request:**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "textDocument/selectionRange",
  "params": {
    "textDocument": {
        "uri": "file:///path/to/billing.js"
    },
    "positions": [
      {
        "line": 10,
        "character": 4
      }
    ]
  }
}
```
In this request:
- `uri` specifies the location of the file.
- `positions` is an array containing one or more positions within the document, each defined by a `line` and `character` number.

#### Response Structure

The response will include a tree of `SelectionRange` instances for each position requested.

**Response:**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": [
    {
      "range": {
        "start": {
          "line": 10,
          "character": 1
        },
        "end": {
          "line": 10,
          "character": 5
        }
      },
      "parent": {
        "range": {
          "start": {
            "line": 9,
            "character": 0
          },
          "end": {
            "line": 12,
            "character": 1
          }
        },
        "parent": {
          "range": {
            "start": {
              "line": 0,
              "character": 0
            },
            "end": {
              "line": 20,
              "character": 1
            }
          },
        }
      }
    }
  ]
}
```

In this response:
- `range` specifies the range of the selection for the given position.
- `parent` is a linked `SelectionRange` that contains the current `range` and expands it, up to encompassing the whole document.

### Summary

The `textDocument/selectionRange` request in LSP enables the user to get a hierarchical selection range for a given position or set of positions. This assists in tasks like code refactoring and navigation by providing context-aware selection expansion and contraction.