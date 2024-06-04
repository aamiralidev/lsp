### Text Document / Inlay Hint

The `textDocument/inlayHint` request in the Language Server Protocol (LSP) is used to provide inline hints for certain constructs or expressions in the code, such as types, parameter names, or values. These hints are usually available in richer text editors or IDEs and provide additional, context-specific information directly in the source text. This is a part of the Inlay Hints feature.

#### Purpose

The `textDocument/inlayHint` command assists developers in understanding their code better by providing hints about the types, parameter names, and values. These hints help make the code more readable and maintainable, particularly when the codebase grows larger or when working with unfamiliar or complex constructs.

#### Example Scenario

Imagine you're working on a function named `calculate` in TypeScript and it accepts three parameters: `a`, `b` and `func`. These parameters are not explicitly typed and it's hard to immediately discern what type `func` should be. An inlay hint for the parameter `func` can inspect the function usage and suggest the appropriate types.

#### Request Structure

The request for `textDocument/inlayHint` would typically include the text document identifier (`uri`).

**Request:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "textDocument/inlayHint",
  "params": {
    "textDocument": {
      "uri": "file:///path/to/code.ts"
    }
  }
}
```

In this request:
- `uri` specifies the location of the file.

#### Response Structure

The response will include a list of inlay hints, each hint would have the position, kind and text.

**Response:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": [
    {
        "range": {
            "start": {
                "line": 1,
                "character": 13
            },
            "end": {
                "line": 1,
                "character": 17
            }
        },
        "kind": "Type",
        "text": ": number"
    },
    {
        "range": {
            "start": {
                "line": 2,
                "character": 13
            },
            "end": {
                "line": 2,
                "character": 17
            }
        },
        "kind": "Parameter",
        "text": "b: number"
    },
    {
        "range": {
            "start": {
                "line": 4,
                "character": 23
            },
            "end": {
                "line": 4,
                "character": 27
            }
        },
        "kind": "Type",
        "text": ": (n1: number, n2: number) => number"
    }
  ]
}
```

In this response:
- `range` provides the location of the hint in the text document.
- `kind` indicates the kind of hint.
- `text` provides the actual hint text.

### Summary

The `textDocument/inlayHint` request in LSP is used to fetch inline contextual hints for types, parameters and values within a specified document. It enhances developers' productivity by increasing code readability and understanding.