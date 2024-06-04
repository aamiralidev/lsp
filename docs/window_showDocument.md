### Window / Show Document

The `window/showDocument` request in the Language Server Protocol (LSP) opens a text document in the client. It returns whether the document was successfully opened or not. 

#### Purpose

The `window/showDocument` command allows the server to request the client to display a document. This command is often used when the server needs the client to navigate to specific documents or locations within those documents for tasks such as code navigation, viewing documentation, and more.

#### Example Scenario

Imagine you are using a language server and it detects an error in a file `utils.js` at line 15. The server could use `window/showDocument` to navigate the client to the precise location of the error.

#### Request Structure

The request for `window/showDocument` includes a text document identifier (URI) and optional selection range. 

**Request:**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "window/showDocument",
  "params": {
    "uri": "file:///path/to/utils.js",
    "external": false,
    "selection": {
      "start": {
        "line": 15,
        "character": 0
      }
    }
  }
}
```

In this request:
- `uri` specifies the location of the file.
- `external` is an optional parameter to allow an external program to handle this request. If true, the client will not show the document itself. The default is false.
- `selection` is another optional parameter to specify a range inside the document that should be selected.

#### Response Structure

The response will include whether or not the operation was successful.

**Response:**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "success": true
  }
}
```

In this response:
- `success` indicates whether the document was successfully opened. In this case, it was successful.

### Summary

The `window/showDocument` request in LSP gives servers the ability to direct clients to open and display specific documents, which is beneficial for tasks like code navigation and error detection. The request contains the URI of the document to be opened, with optional parameters to open the document in an external program and to select a specific range within the document. The response indicates the success of the operation.