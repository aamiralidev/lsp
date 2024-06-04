# Text Document / Did Save

The `textDocument/didSave` notification in the Language Server Protocol (LSP) is sent from the client to the server to inform the server when a document is saved.

## Purpose

The `textDocument/didSave` command signals the language server that a document has been saved. This enables the server to trigger tasks that are necessary after a save operation, such as cleaning up temporary structures or performing static code analysis.

## Example Scenario

Consider a situation where the developer is working on a file called `main.js`. After writing some new code in this file, they save the changes. At this moment, the client dispatches a `textDocument/didSave` notification to the server.

## Request Structure

The `textDocument/didSave` does not expect a request in the standard sense but sends a notification message. The client includes a `text` parameter when the `includeText` save option is true.

**Notification:**

```json
{
  "jsonrpc": "2.0",
  "method": "textDocument/didSave",
  "params": {
    "textDocument": {
      "uri": "file:///path/to/main.js",
      "version": 2
    },
    "text": "console.log('Hello, World!');"
  }
}
```

In this notification:
- `uri` specifies the location of the document that was saved.
- `version` is the version number of the document.
- `text` contains the content of the saved file, but it is only included if the client has the `includeText` save option enabled.

## Response Structure

As the `textDocument/didSave` method is a notification, it does not have a response structure.

## Summary

The `textDocument/didSave` notification in LSP plays a crucial role in the interaction between the client and server. It notifies the server every time a document is saved, thereby enabling the server to perform actions that are triggered by the save operation. This notification enhances code consistency by ensuring that the server is always updated with the latest state of the document.