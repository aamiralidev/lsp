# Workspace / Did Change Watched Files

The `workspace/didChangeWatchedFiles` command in the Language Server Protocol (LSP) is used to notify the server when a file has been changed, created, or deleted. This is part of the File Notifications feature, which provides a server with change notifications.

## Purpose

The `workspace/didChangeWatchedFiles` function allows the server to be updated in real-time about any changes that may affect files being watched by the client. This is beneficial for recompiling, reindexing, or reloading any resources associated with changed files.

## Example Scenario

Suppose you are working on a Java project and you have a language server providing services like autocompletion, diagnostics etc. When a specific file that is being watched is edited (like 'main.java'), the `workspace/didChangeWatchedFiles` notification will inform the language server about this change.

## Notification Structure

The notification for `workspace/didChangeWatchedFiles` includes one or more file events (including the URI and type of change).

**Notification:**

```json
{
  "jsonrpc": "2.0",
  "method": "workspace/didChangeWatchedFiles",
  "params": {
    "changes": [
      {
        "uri": "file:///path/to/main.java",
        "type": 2
      }
    ]
  }
}
```

In this notification:
- `uri` specifies the location of the file.
- `type` indicates the type of change that occurred: 1 for created, 2 for changed, 3 for deleted.

## Response Structure

As this is a notification, it does not produce a response. Notifications are meant to provide information, not to get information. 

## Summary

The `workspace/didChangeWatchedFiles` Notification in LSP is a real-time system that notifies the server about any changes made to the files being watched by the client. It provides a way for the server to stay current and handle changes to files as necessary.