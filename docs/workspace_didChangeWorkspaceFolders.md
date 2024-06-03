### `workspace/didChangeWorkspaceFolders` Command in LSP

The `workspace/didChangeWorkspaceFolders` notification in the Language Server Protocol (LSP) is used to denote changes to the workspace folders. Introduction of this command allows the language server to manage several root folders making it a robust multi-root workspace.

#### Purpose

The `workspace/didChangeWorkspaceFolders` notification helps in communicating changes to the workspace, such as addition or removal of folders, to the server. This enables the server to adapt to these changes for features like IntelliSense, Go to Definition, Find all References et cetera. This supports users working with multi root workspace.

#### Example Scenario

Consider a developer working on a project divided into multiple sub-projects, each residing in its own folder in the workspace. When the developer adds or removes a sub-project folder to/from the workspace, this command is used.

#### Request Structure

Since `workspace/didChangeWorkspaceFolders` is a notification, there aren t any direct responses from the server. However, it s worth noting that the structure of the notification sent to the server includes an object representing the added or removed folders.

**Request:**

```json
{
  "jsonrpc": "2.0",
  "method": "workspace/didChangeWorkspaceFolders",
  "params": {
    "event": {
      "added": [
        {
          "uri": "file:///path/to/workspace/folder1"
        }
      ],
      "removed": [
        {
          "uri": "file:///path/to/workspace/folder2"
        }
      ]
    }
  }
}
```

In this above request:
- `added` is an array of the newly added folders to the workspace.
- `removed` is an array of the removed folders.

#### Response Structure

As previously mentioned, `workspace/didChangeWorkspaceFolders` is a notification, not a request. Therefore, it doesn't get a direct response from the server.

#### Summary

The `workspace/didChangeWorkspaceFolders` notification in LSP allows the server to be aware of workspace changes, enabling it to maintain up-to-date understanding of the workspace's state. This is very useful for scenarios where developers are working with multiple root folder workspaces. It allows the server to provide accurate support for features including logic validation, highlighting, and many more.