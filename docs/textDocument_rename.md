### `textDocument/rename` Command in LSP

The `textDocument/rename` request in the Language Server Protocol (LSP) is utilized to rename all occurrences of a symbol found in the text document.

#### Purpose

The primary purpose of the `textDocument/rename` command is to provide a way for developers to refactor their code by renaming a symbol throughout the entire workspace where it's being used. This is extremely useful when a method name needs to be made more descriptive or to adhere to certain coding standards without manually changing it in every place where it is used.

#### Example Scenario

Consider a scenario where you have a function called 'getData' that you want to refactor to 'fetchUserData' for clarity in a JavaScript file.

#### Request Structure

The request for this function typically includes the text document identifier, the position of the symbol (function in this case), and the new name.

**Request:**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "textDocument/rename",
  "params": {
    "textDocument": {
      "uri": "file:///path/to/myFile.js"
    },
    "position": {
      "line": 10,
      "character": 4
    },
    "newName": "fetchUserData"
  }
}
```

In this request:
- `uri` specifies the location of the file.
- `position` specifies the position in the document where the function 'getData' is defined.
- `newName` is the new name for the function being renamed.

#### Response Structure

The response will include a list of changes to apply to the document to implement the rename.

**Response:**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "changes": {
      "file:///path/to/myFile.js": [
        {
          "range": {
            "start": {
              "line": 10,
              "character": 4
            },
            "end": {
              "line": 10,
              "character": 11
            }
          },
          "newText": "fetchUserData"
        }, 
        ... // other instances of 'getData' being renamed
      ]
    }
  }
}
```

In this response:
- `changes` specifies the file and the places where the renaming is to take place in that file.
- `range` specifies the start and end positions of each instance of the symbol being renamed.
- `newText` is the new name for the function.

### Summary

The `textDocument/rename` request in LSP uses the power of the underlying language server to perform a project-wide rename operation. This function provides an efficient way to refactor a symbol's name across multiple files within the workspace, ensuring accuracy and consistency.