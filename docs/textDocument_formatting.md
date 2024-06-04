### Text Document / Formatting

In the Language Server Protocol (LSP), the `textDocument/formatting` request is used to request the whole content of a document to be formatted. It is a helpful feature that helps developers in auto-formatting their code based on predefined rules.

#### Purpose

The purpose of the `textDocument/formatting` command is to return a set of text edits which can be applied to a document, to format it consistently according to a particular set of style rules. This saves developers time they would otherwise spend formatting their code manually, and ensures the code adheres to a uniform style.

#### Example Scenario

For example, if you're working on a JavaScript file called `app.js` and need it formatted according to your project's linting style: two-space indents, single quotes around strings, no trailing spaces, etc. You can use the `textDocument/formatting` command to achieve this.

#### Request Structure

The request for `textDocument/formatting` includes the text document identifier and options specifying the desired formatting style.

**Request:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "textDocument/formatting",
  "params": {
    "textDocument": {
      "uri": "file:///path/to/app.js"
    },
    "options": {
      "tabSize": 2,
      "insertSpaces": true,
      "trimTrailingWhitespace": true,
      "insertFinalNewline": true
    }
  }
}
```

In this request:
- `uri` specifies the location of the file.
- `options` specifies the formatting rules to be applied.

#### Response Structure

The response to this request includes an array of edits to be applied to the document to achieve the desired formatting.

**Response:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": [
    {
      "range": {
        "start": {
          "line": 0,
          "character": 0
        },
        "end": {
          "line": 10,
          "character": 8
        }
      },
      "newText": "'use strict';\n\nfunction hello() {\n  return 'Hello, world!';\n}\n"
    }
  ]
}
```

In this response:
- `range` specifies the area of the document to which the edit applies.
- `newText` contains the formatted text that should replace the text in the specified range.

### Summary

The `textDocument/formatting` request in LSP is a crucial command for developers to maintain consistency and readability in their code. By applying predefined formatting rules, it helps in making the code more understandable and easier to maintain. Developers can effectively utilize this command to focus more on writing code and less on formatting it manually.