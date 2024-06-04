# Text Document / Did Change

The `textDocument/didChange` notification in the Language Server Protocol (LSP) is sent from the client to the server to signal changes to a text document. It's part of the Text Synchronization API, a feature that ensures the server and the client have the same version of the document.

## Purpose

The `textDocument/didChange` command allows the server to maintain an up-to-date version of the text on the client side. This points the server to any changes that have been made to the document, which is crucial in features like real-time error reporting, auto-complete, and more.

## Example Scenario

Imagine you are working on a file named `app.js` in the text editor. You just modified a line of code. The editor sends a `textDocument/didChange` notification to the language server indicating that the document has been updated. This ensures that the language server has the latest version of your code which is used in providing code diagnostics, suggestions, etc.

## Request Structure

The request for `textDocument/didChange` usually includes the text document identifier and a list of changes that occurred.

**Example notification:**

```json
{
  "jsonrpc": "2.0",
  "method": "textDocument/didChange",
  "params": {
    "textDocument": {
      "uri": "file:///path/to/app.js",
      "version": 2
    },
    "contentChanges": [
      {
        "range": {
          "start": {
            "line": 7,
            "character": 12
          },
          "end": {
            "line": 7,
            "character": 18
          }
        },
        "rangeLength": 6,
        "text": "updatedText"
      }
    ]
  }
}
```

In this notification:
- `uri` specifies the location of the file
- `version` is the version number of the document (incremented for each change).
- `contentChanges` is an array describing the changes. 
- `range` specifies the range of text replaced.
- `rangeLength` indicates the length of the replaced range. 
- `text` is the new text that replaced the old one.

## Response Structure

Since `textDocument/didChange` is a notification, it does not expect a response from the server.

## Summary

The `textDocument/didChange` in LSP serves to notify the server about the changes that have happened in a document on the client side. It plays a significant role in maintaining synchronization between the server and the client, which in turn supports many real-time language features like error checking, auto-completion, and more.