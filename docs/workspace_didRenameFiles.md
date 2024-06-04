### Workspace / Did Rename Files

The `workspace/didRenameFiles` notification in the Language Server Protocol (LSP) is used to report renamed files in the workspace. This allows language servers to remain up-to-date with changes in the workspace made by the user, ensuring that any symbols defined in renamed files can still be resolved correctly.

#### Purpose

The `workspace/didRenameFiles` command notifies the language server about changes in the file hierarchy so that it can update symbols and references accordingly. This is particularly useful for accurate code navigation and analysis, also it can help with refactoring efforts by guaranteeing symbol naming consistency even across renamed files.

#### Example Scenario

Imagine that in your workspace you have renamed a TypeScript file from `oldFile.ts` to `newFile.ts`.

#### Notification Structure

The notification for this workspace change includes an array of `changes` where each change item has the old and new file `uri`.

**Notification:**

```json
{
  "jsonrpc": "2.0",
  "method": "workspace/didRenameFiles",
  "params": {
    "changes": [{
      "oldUri": "file:///path/to/oldFile.ts",
      "newUri": "file:///path/to/newFile.ts"
    }]
  }
}
```

In this notification:
- `oldUri` is the file location before the rename.
- `newUri` is the new file location after the rename.

#### Response Structure

There is typically no response for this notification as it is a one-way communication from the client informing the server of the renamed files. If they were to be a response, it would likely be implementation-dependent for a given language server. 

### Summary

The `workspace/didRenameFiles` notification in LSP is a helpful way to ensure that the language server has the most current view of the workspace, which in turn helps provide accurate symbol resolution. Despite being a notification rather than a request/response pair, it is crucial for maintaining accuracy as files get renamed within the workspace.