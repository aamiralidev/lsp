### `textDocument/documentSymbol` Command in LSP

The `textDocument/documentSymbol` request in the Language Server Protocol (LSP) is used to provide a list of all symbols found inside a given text document. This feature is commonly used in code editors for populating a file's structure or outline view.

#### Purpose

The `textDocument/documentSymbol` command assists developers in quickly understanding the structure of a file, by listing all the symbols in it, like functions, variables, classes, etc. It's essential for code navigation and quick browsing of a document's contents.

#### Example Scenario

Imagine you are editing a file named `main.js` which contains several functions and variables. To get a quick overview of the file structure, the `textDocument/documentSymbol` command can be used.

#### Request Structure

The request for `textDocument/documentSymbol` typically includes the text document identifier.

**Request:**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "textDocument/documentSymbol",
  "params": {
    "textDocument": {
      "uri": "file:///path/to/main.js"
    }
  }
}
```

In the request:
- `uri` specifies the location of the file.

#### Response Structure

The response will include a list of all symbols found in the document, with their names, locations, types, and other details. Each item represents a symbol in the text document.

**Response:**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": [
    {
      "name": "myFunction",
      "kind": 12,
      "range": {
        "start": {
          "line": 20,
          "character": 2
        },
        "end": {
          "line": 45,
          "character": 4
        }
      },
      "selectionRange": {
        "start": {
          "line": 20,
          "character": 2
        },
        "end": {
          "line": 20,
          "character": 12
        }
      }
    },
    {
      "name": "myVar",
      "kind": 13,
      "range": {
        "start": {
          "line": 50,
          "character": 1
        },
        "end": {
          "line": 50,
          "character": 12
        }
      },
      "selectionRange": {
        "start": {
          "line": 50,
          "character": 1
        },
        "end": {
          "line": 50,
          "character": 5
        }
      }
    }
  ]
}
```

In this response:
- `name` is the name of the symbol.
- `kind` specifies the type of symbol (e.g., function, variable).
- `range` designates where the symbol is defined in the document.
- `selectionRange` is the range in which the symbol's name appears in the code.

### Summary

The `textDocument/documentSymbol` request in LSP offers a way to outline relevant symbols in a document, thus aiding developers to quickly navigate and comprehend the structure of a code file.