### Text Document / On Type Formatting

The `textDocument/onTypeFormatting` request in the Language Server Protocol (LSP) is used to trigger format operations on the content of a text document based on typing.

#### Purpose

The primary purpose of `textDocument/onTypeFormatting` is to assist the coding process by automatically formatting the text code in real-time as a developer types it. This helps maintain clean, consistent, and error-free coding standards and provides a better coding interface.

#### Example Scenario

Imagine you are working in a PHP file and just typed a new line character after a `{`. The expectation is that the cursor should indent automatically to the correct block-level on the new line.

#### Request Structure

The request for `textDocument/onTypeFormatting` typically includes a text document identifier, the position within the document, the character that was typed, and the format options.

**Request:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "textDocument/onTypeFormatting",
  "params": {
    "textDocument": {
      "uri": "file:///path/to/file.php"
    },
    "position": {
      "line": 5,
      "character": 0
    },
    "ch": "\n",
    "options": {
      "tabSize": 4,
      "insertSpaces": true
    }
  }
}
```

In this request:
- `uri` specifies the location of the file.
- `position` specifies the location in the document where the character was typed.
- `ch` is the character that triggered the on-type formatting request (in this case, a newline).
- `options` details the formatting options to apply (`tabSize` and`insertSpaces`).

#### Response Structure

The response includes a list of `TextEdit` items containing the changes to be made to the document.

**Response:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": [
    {
      "range": {
        "start": {
          "line": 5,
          "character": 0
        },
        "end": {
          "line": 5,
          "character": 0
        }
      },
      "newText": "    "
    }
  ]
}
```

In this response:
- `range` specifies the location in the document where the new formatting will apply.
- `newText` is the text that will replace the current text in the specified range (in this case, four spaces for indentation).

### Summary

The `textDocument/onTypeFormatting` request in LSP provides valuable assistance to developers by enabling automatic content formatting as they type. It helps maintain good coding practices and improves readability and accuracy of the code.