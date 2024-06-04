### Workspace / Workspace Folders

The `workspace/workspaceFolders` request in the Language Server Protocol (LSP) is used to fetch all the root workspace folders in a language client.

#### Purpose

The `workspace/workspaceFolders` command helps provide the necessary context from the workspace for a language server, enabling features like file indexing, global search, and cross-referencing across files and projects.

#### Example Scenario

Imagine you are working on a project which contains several smaller modules, each in a separate root folder contained within a master project workspace. You would use `workspace/workspaceFolders` to list all these root folders.

#### Request Structure

As the command is about fetching information, no special parameters are typically required.

**Request:**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "workspace/workspaceFolders"
}
```

The request is straightforward without requiring any specific parameters.

#### Response Structure 

The response contains an array of WorkspaceFolder objects each having a unique URI, name and an optional value.

**Response:**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": [
    { 
      "uri": "file:///path/to/workspace1",
      "name": "Workspace1",
      "index": 0
    },
    {
      "uri": "file:///path/to/workspace2",
      "name": "Workspace2",
      "index": 1
    }
  ]
}
```

In this response:
- `uri` specifies the location of the workspace.
- `name` is the name of the workspace.
- `index` is the order of the workspace folder in the workspace array of the client.

### Summary

The `workspace/workspaceFolders` command in LSP is essential in multi-root workspace contexts, helping language servers understand the structure and layout of the project. This aids in better file indexing, search, and symbol exploration across modules within a workspace.