# Workspace / Did Delete Files

The `workspace/didDeleteFiles` notification in the Language Server Protocol (LSP) is used to alert the Language Server about the deletion of a file or several files in the workspace. This allows the Language Server to update its internal representation of the workspace and avoid potential errors caused by referring to deleted files.

## Purpose

The `workspace/didDeleteFiles` command informs the Language Server when files or directories are deleted from the workspace. This notification enables the server to react correctly, for instance by clearing any cached information related to the deleted files, or by invalidating diagnostics related to these files.

## Example Scenario

Imagine you have an open project in your editor, and you delete a JavaScript file, `oldFunction.js`, directly from the filesystem (for example, using the system's file explorer).

## Request Structure

The `workspace/didDeleteFiles` notification includes an array of files that were deleted.

**Request:**

```json
{
  "jsonrpc": "2.0",
  "method": "workspace/didDeleteFiles",
  "params": {
    "changes": [{
      "uri": "file:///path/to/oldFunction.js"
    }]
  }
}
```

In this request:
- `uri` specifies the location of the deleted file.

## Response Structure

Being a notification, `workspace/didDeleteFiles` does not have a response.

### Summary

The `workspace/didDeleteFiles` notification in LSP ensures that the Language Server maintains an accurate model of the workspace by being informed when files or directories are deleted. This aids in avoiding potential errors caused by the server referencing files that no longer exist.