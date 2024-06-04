# Workspace / Will Rename Files

The `workspace/willRenameFiles` request in the Language Server Protocol (LSP) is used as a notification sent by the client to the server before the client is renaming one or more files. This allows the server to provide edits that should be applied to the workspace before the given files are renamed.

## Purpose

The purpose of the `workspace/willRenameFiles` command is to provide a mechanism where the server can manipulate changes to the workspace that all occur just before renaming a particular file. This may be used to handle file dependencies or manage references.

## Example Scenario

Consider a scenario where you are renaming a JavaScript file from `oldFile.js` to `newFile.js`. Before doing so, there may be import statements in other files that make reference to `oldFile.js`. The `workspace/willRenameFiles` command will provide a mechanism to update these import statements automatically.

## Request Structure

The request for `workspace/willRenameFiles` typically includes the old Uri and the new Uri that the file will move to.

**Request:**

```json
{
  "jsonrpc": "2.0",
  "method": "workspace/willRenameFiles",
  "params": {
    "files": [
      {
        "oldUri": "file:///path/to/oldFile.js",
        "newUri": "file:///path/to/newFile.js"
      }
    ]
  }
}
```

In this request:
- `oldUri` specifies the current location of the file.
- `newUri` specifies the future location of the file.

## Response Structure

The response will be a `workspaceEdit`, describing changes to documents before the file rename.

**Response:**
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "documentChanges": [
      {
        "textDocument": {
          "uri": "file:///path/to/anotherFile.js",
          "version": 1
        },
        "edits": [
          {
            "range": {
              "start": {
                "line": 1,
                "character": 0
              },
              "end": {
                "line": 1,
                "character": 18
              }
            },
            "newText": "import './newFile.js'"
          }
        ]
      }
    ]
  }
}
```

In this response:
- `documentChanges` contains a list of changes that need to be made.
- `uri` specifies the file where changes need to be made.
- `version` is the version number of the document to which the changes apply.
- `range` specifies the part in the document where changes need to be made.
- `newText` is the content to replace the specified range with.

## Summary

The `workspace/willRenameFiles` request in LSP enables an automated updating mechanism before renaming of file(s) is done to ensure dependencies or references remain intact. This helps to prevent breaks in the code and enhance program integrity.