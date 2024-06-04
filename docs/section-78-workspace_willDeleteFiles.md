# Workspace / Will Delete Files

The `workspace/willDeleteFiles` request in the Language Server Protocol (LSP) is a notification sent from the client to the server before files get deleted from the workspace. The server can then perform necessary preparations, such as saving state or cleaning resources related to the files about to be deleted.

## Purpose

The `workspace/willDeleteFiles` command allows the server to prepare for file deletions. This is especially useful when the server maintains states or resources based on workspace files - it allows the server to handle a deletion scenario gracefully without potential discrepancies due to stale file references.

## Example Scenario

Let's say the user decides to delete a file named `oldCode.js` from the workspace. Before the deletion is carried out, the client sends a notification to the server to prepare for this change.

## Request Structure

The request for `workspace/willDeleteFiles` typically includes the files to be deleted.

**Request:**

```json
{
  "jsonrpc": "2.0",
  "method": "workspace/willDeleteFiles",
  "params": {
    "files": [
      {
        "uri": "file:///path/to/oldCode.js"
      }
    ]
  }
}
```

In this request:
- `uri` specifies the location of the file that will be deleted.

## Response Structure

As `workspace/willDeleteFiles` is a notification, the server does not usually send a response. It instead performs the actions it needs (such as internal state management) based on the incoming notification.

## Summary

The `workspace/willDeleteFiles` request in LSP enables the server to prepare for cases where workspace files are about to be deleted. This is crucial for maintaining consistent states and resources on the server end, especially in scenarios where files in the workspace have dependencies or where the server utilizes file-based caching or data representation.