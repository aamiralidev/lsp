### `documentLink/resolve` Command in LSP

The `documentLink/resolve` request in the Language Server Protocol (LSP) is used to resolve the target of a given document link. Document links are typically underlined sections of text that refer to other documents.

#### Purpose

The `documentLink/resolve` command assists developers in navigation between different parts of the code or documentation by resolving the target of inter-linked documents. This is particularly useful when navigating through large codebases or comprehensive documentation.

#### Example Scenario

Consider a scenario where you have a comment above a function in your code that says “Refer to Issue #123”. ‘Issue #123’ is a hyperlink that links to the issue tracker of the project. The `documentLink/resolve` command can be used to navigate to that issue directly from the code.

#### Request Structure

The request for `documentLink/resolve` only includes the document link that needs to be resolved.

**Request:**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "documentLink/resolve",
  "params": {
    "range": {
      "start": {
        "line": 0,
        "character": 10
      },
      "end": {
        "line": 0,
        "character": 21
      }
    },
    "target": "Issue #123"
  }
}
```

In this example request:
- `range` is the area of the document that the link refers to.
- `target` is the actual text that is linked (in this case 'Issue #123').

#### Response Structure

The response will include the resolved document link with the full URI to the target document.

**Response:**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "range": {
      "start": {
        "line": 0,
        "character": 10
      },
      "end": {
        "line": 0,
        "character": 21
      }
    },
    "target": "http://issue.tracker/issue/123"
  }
}
```

In this example response:
- `range` is the same area of the document that the link refers to (as in the request).
- `target` is now a fully resolved URI that directly links to Issue #123 in the issue tracker.

### Summary

The `documentLink/resolve` request in LSP allows developers to navigate between documents seamlessly, making managing and understanding complex codebases or extensive documentation much easier. It takes a document link from your code or documents and resolves it to a complete URI, which can then be used to navigate to the target of the link.