### Text Document / Inline Values

The `textDocument/inlineValues` request in the Language Server Protocol (LSP) is used to retrieve inline values for a given source code. Inline values in this context refer to the computed values of variables or expressions at a specific position in the source code.

#### Purpose

The `textDocument/inlineValues` command is mainly used during debug sessions to help developers have a clearer understanding of the evaluated expressions or variable values in their source code as they are stepping through it, without the need to watch or hover over the variables one by one.

#### Example Scenario

Imagine you are debugging a function called `calculateSquare` in a source file named `squareCalculator.py`, and you want to know the value of a variable `x` at a certain position within the function.

#### Request Structure

The request for `textDocument/inlineValues` typically includes the text document identifier and the range within the document for which inline values are required.

**Request:**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "textDocument/inlineValues",
  "params": {
    "textDocument": {
      "uri": "file:///path/to/squareCalculator.py"
    },
    "range": {
      "start": {
        "line": 0,
        "character": 0
      },
      "end": {
        "line": 50,
        "character": 0
      }
    }
  }
}
```

In this request:
- `uri` specifies the location of the file.
- `range` specifies the range in the document for which inline values are needed.

#### Response Structure

The response will contain an array of `InlineValue` results that indicate where inline values are displayed and what those values are.

**Response:**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": [
    {
      "id": "1",
      "name": "x",
      "value": "6",
      "range": {
        "start": {
          "line": 10,
          "character": 5
        },
        "end": {
          "line": 10,
          "character": 7
        }
      }
    }
  ]
}
```

In this response:
- `id` is an identifier unique within the scope of a module.
- `name` is the heading to use for the value in the user interface.
- `value` is the string representation of the variable value.
- `range` specifies the range in the document where the inline value is displayed.

### Summary

The `textDocument/inlineValues` request in LSP is very useful during debugging sessions as it enables developers to directly inspect the value of variables or expressions at a given position in the code, enhancing their ability to understand and troubleshoot their code.