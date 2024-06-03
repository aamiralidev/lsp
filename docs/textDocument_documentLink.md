### `textDocument/documentLink` Request in LSP

The `textDocument/documentLink` request in the Language Server Protocol (LSP) is used to request all the document links from a certain file. The Document Links feature allows a client to request all likely locations within a document that can be used as hyperlinks to other documents.

#### Purpose

The `textDocument/documentLink` request helps developers get access to all the document links in a specific file. This feature aids in navigation between related documents or locations within a document, improving the overall development process.

#### Example Scenario

Imagine you have a Markdown text document and you want to find all the hyperlinks in this document to navigate them quickly.

#### Request Structure

The request for `textDocument/documentLink` includes the text document identifier.

**Request:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "textDocument/documentLink",
  "params": {
    "textDocument": {
      "uri": "file:///path/to/example.md"
    }
  }
}
```
In this request:
- `uri` is the location of the file.

#### Response Structure

The response contains an array of all the document links, which include the range of each link within the document and possibly the target URL.

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
          "character": 10
        },
        "end": {
          "line": 1,
          "character": 20
        }
      },
      "target": "http://example.com"
    },
    {
      "range": {
        "start": {
          "line": 5,
          "character": 0
        },
        "end": {
          "line": 5,
          "character": 12
        }
      },
      "target": "http://example.net"
    }
  ]
}
```
In this response:
- `range` suggest the range where the link is found in the document.
- `target` is the resolved URI of the link if available. This is typically where the link points to.

### Summary

The `textDocument/documentLink` request in LSP is a useful feature for developers to quickly identify all the document links in a certain file for better code navigation. This feature not only improves development speed but also makes the code more comprehensible.