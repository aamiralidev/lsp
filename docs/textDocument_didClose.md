### `textDocument/didClose` Command in LSP

The `textDocument/didClose` request in the Language Server Protocol (LSP) is sent from a client to a server to notify the server that a text document is no longer in use by the client and the server can free up any resources such as caches related to that document.

#### Purpose

The `textDocument/didClose` command supports efficient resource management on the server-side by allowing the server to stop maintaining state for documents that are no longer open/active in the client, thereby freeing up memory and computation resources.

#### Example Scenario

Imagine you are working on the file `app.js` in a modern code editor and you decide to close the file to focus on another part of your project. The editor, acting as the client, would send a `textDocument/didClose` notification to the server indicating that `app.js` has been closed.

#### Request Structure

The request for `textDocument/didClose` typically contains the descriptor of the text document that has been closed.

**Request:**

```json
{
  "jsonrpc": "2.0",
  "method": "textDocument/didClose",
  "params": {
    "textDocument": {
      "uri": "file:///path/to/app.js"
    }
  }
}
```

In this request:
- `uri` specifies the location of the text document that is no longer in use.

#### Response Structure

Note that `textDocument/didClose` is a notification, therefore it does not require a response from the server.

#### Summary

The `textDocument/didClose` notification in LSP facilitates efficient memory and resource utilization on the server. By notifying the server when a document is no longer in use, the server can clear up associated resources. This is crucial in maintaining high-performance levels, especially when dealing with large projects with many document files.