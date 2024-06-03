### `textDocument/rangeFormatting` Command in LSP

The `textDocument/rangeFormatting` request in the Language Server Protocol (LSP) is used to format a specific range within a text document. This command is part of the formatting feature, allowing developers to improve readability and maintain consistency of code within a specified range.

#### Purpose

The `textDocument/rangeFormatting` command helps developers to automatically format a specific portion of code in their editor. This is useful for ensuring that a piece of code follows specified formatting rules, such as indentation, line spacing, and braces placement.

#### Example Scenario

Imagine you have a file called `main.js`, and you've just written a piece of code from line 10 to 15. Now, you want to format this specific range according to your code style settings.

#### Request Structure

The request for `textDocument/rangeFormatting` typically includes the text document identifier and the range to be formatted.

**Request:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "textDocument/rangeFormatting",
  "params": {
    "textDocument": {
      "uri": "file:///path/to/main.js"
    },
    "range": {
      "start": {
        "line": 10,
        "character": 0
      },
      "end": {
        "line": 15,
        "character": 0
      }
    },
    "options": {
      "tabSize": 2,
      "insertSpaces": true
    }
  }
}
```

In this request:
- `uri` specifies the location of the file.
- `range` defines the range within the document to be formatted.
- `options` specifies the formatting options. In this case, it is specifying the use of spaces for indentation, with a size of two spaces.

#### Response Structure

The response for this command provides an array of text edits which should be applied to the document to format the specified range.

**Response:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": [
    {
      "range": {
        "start": {
          "line": 10,
          "character": 0
        },
        "end": {
          "line": 15,
          "character": 0
        }
      },
      "newText": "formatted code..."
    }
  ]
}
```

In this response:
- `range` is the portion of the text that is going to be replaced.
- `newText` is the new text after modification. This will be the formatted code.

### Summary

The `textDocument/rangeFormatting` request in LSP provides a way for developers to automatically format a specific range of code according to their preferred style. This leads to cleaner, more readable code, and saves developers time by automating the formatting process.