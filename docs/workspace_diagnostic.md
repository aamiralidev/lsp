### Workspace / Did Change Watched Files

The `workspace/didChangeWatchedFiles` command in the Language Server Protocol (LSP) is used to notify the server about file changes. This is part of the Watched Files feature, which allows the server to keep track of file changes outside the current opened text document. This is useful when file changes could impact the state of the language server, such as configuration files for the project.

#### Purpose

The `workspace/didChangeWatchedFiles` command helps the server to stay aware of file changes that may influence its internal state. For example, if an application configuration file is modified, the language server might have to adjust its settings accordingly.

#### Example Scenario:

Imagine you have a JavaScript project and you change your `babel.config.json` file. This change could potentially impact how your JavaScript files are interpreted by the Language Server.

#### Request Structure

The request for `workspace/didChangeWatchedFiles` typically includes an array of file events, each containing the URI of the file that changed and the type of change.

**Request:**

```json
{
  "jsonrpc": "2.0",
  "method": "workspace/didChangeWatchedFiles",
  "params": {
    "changes": [
      {
        "uri": "file:///path/to/babel.config.json",
        "type": 2
      }
    ]
  }
}
```

In this request:
- `uri` specifies the location of the file that changed.
- `type` is the type of change. The value of 2 indicates that the file was changed. Other possible values are 1 for created and 3 for deleted.

#### Response Structure

This command typically does not have a structured response, as it is a notification to the server. The sole purpose is to inform the server about the changes, and the server acts accordingly based on its own internal logic.

#### Summary

The `workspace/didChangeWatchedFiles` command in LSP is a notification sent to the server about file changes so that the server can react to those changes and adjust its internal state accordingly. This is primarily useful for tracking changes in important configuration files or other files outside the currently opened text document.