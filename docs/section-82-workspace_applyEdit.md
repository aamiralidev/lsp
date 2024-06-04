# Workspace / Apply Edit

The `workspace/applyEdit` request is a part of the Language Server Protocol (LSP) and it is used to request the application of a workspace edit from the server to the client-side.

## Purpose

The `workspace/applyEdit` request is utilized to enact certain changes from the server-side, such as refactoring, renaming symbols, fixing code issues, and so forth. As a result, the client-side documents are updated consistently and synchronously with changes implemented on the server.

## Example Scenario

For instance, consider a scenario where a function `getUserName` is renamed to `fetchUserName` in a codebase. To reflect this change across all uses of `getUserName` in the client-side codebase, a `workspace/applyEdit` request would be initiated from the server-side.

## Request Structure

The request of `workspace/applyEdit` usually contains the `label` (a description of changes for tracking purposes) and the `edit` (changes to be applied).

**Request:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "workspace/applyEdit",
  "params": {
    "label": "Rename getUserName to fetchUserName",
    "edit": {
      "changes": {
        "file:///path/to/user.js": [
          {
            "range": {
              "start": {
                "line": 12,
                "character": 4
              },
              "end": {
                "line": 12,
                "character": 15
              }
            },
            "newText": "fetchUserName"
          }
        ]
      }
    }
  }
}
```

In this request:
- `label` describes the change(s) to be applied.
- `edit` includes the changes to be made.
- `file:///path/to/user.js` represents the file where the change is to be made.
- `range` specifies the range in the document where the change will be applied.
- `newText` specifies the updated text after the change is applied.

## Response Structure

The response to a `workspace/applyEdit` includes bool `applied` which indicates whether or not the requested edit(s) were applied.


**Response:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "applied": true
  }
}
```

In this response:
- `applied` indicates whether the changes were successfully implemented on the client-side.

## Summary

The `workspace/applyEdit` request within LSP helps in implementing global changes across documents on the client-side. This ensures that all updates made on the server-side are consistently and efficiently reflected in the client's workspace. This aids in code refactoring, symbol renaming and many other code editing practices.