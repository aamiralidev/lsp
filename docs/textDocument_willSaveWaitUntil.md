# Text Document / Will Save Wait Until

The `textDocument/willSaveWaitUntil` request in the Language Server Protocol (LSP) is utilized when a document is about to be saved and the client requests potential edits from the server to modify the document before it is saved.

## Purpose

The objective of the `textDocument/willSaveWaitUntil` command is to facilitate automated edits or formatting tasks before the document gets saved. This enables developers to maintain clean and formatted code.

## Example Scenario

Assume you are working on a JavaScript module named `app.js` and you're about to save it. However, you want any typos or syntax errors to be automatically corrected before the file gets saved.

## Request Structure

The request for `textDocument/willSaveWaitUntil` generally includes the document's identifier and the reason for the request.

**Request:**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "textDocument/willSaveWaitUntil",
  "params": {
    "textDocument": {
      "uri": "file:///path/to/app.js"
    },
    "reason": 1
  }
}
```

In this request:
- `uri` signifies the location of the document.
- `reason` signifies the situation of the save operation (1 means 'Manual' save).

## Response Structure

The response for this request will include a list of edits that should be applied to the document before it's saved.

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
          "character": 4
        },
        "end": {
          "line": 10,
          "character": 19
        }
      },
      "newText": "correctedFunction()"
    }
  ]
}
```

In this response:
- `range` signifies the location in the document where the edit should be done.
- `newText` represents the text which should replace the range.

## Summary

The `textDocument/willSaveWaitUntil` request in LSP is an essential feature that allows automatic tasks such as formatting or quick-fixes to be executed right before the document gets saved. This ensures the code remains clean and consistent and it prevents minor mistakes from going unnoticed.