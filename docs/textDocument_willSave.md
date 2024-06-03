### `textDocument/willSave` Command in LSP

The `textDocument/willSave` request in the Language Server Protocol (LSP) is sent from the client to the server before the document is actually saved in the client's IDE or text editor. This gives the server the opportunity to take actions based on the impending save operation.

#### Purpose

The `textDocument/willSave` command is typically used in scenarios where the server needs to perform certain operations right before a document is saved, such as formatting or fixing the code, running linters, or performing other diagnostics.

#### Example Scenario

For instance, before the code document `main.py` is saved, a client would send a `willSave` event to a Python language server, which could then trigger code linting checks or format the document according to the style guide.

#### Request Structure

The request from the client to the server includes the `textDocument` with the `willSave` command.

**Request:**

```json
{
  "jsonrpc": "2.0",
  "method": "textDocument/willSave",
  "params": {
    "textDocument": {
      "uri": "file:///path/to/main.py",
    },
    "reason": 1
  }
}
```

In this request:
- `uri` is the location of the file that's about to be saved.
- `reason` is an indicator for the reason for saving. The possible reasons are defined by `TextDocumentSaveReason`, where `1` means 'manually triggered'.

#### Response Structure

The `willSave` notification does not require a response as it's merely a notification about an upcoming event.

### Summary

The `textDocument/willSave` command in LSP is a notification from the client to the server that a document is about to be saved. The server can use this information to perform certain tasks, such as code formatting or linting, before the document is actually saved. The request includes the document URI and the save trigger reason, and does not require a response.
