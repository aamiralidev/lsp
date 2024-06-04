### Text Document / Linked Editing Range

The `textDocument/linkedEditingRange` request in the Language Server Protocol (LSP) is used to find all the text positions that must be changed when renaming a symbol. It enables simultaneous editing of these positions, making refactoring easier.

#### Purpose

The `textDocument/linkedEditingRange` command helps developers rename variables or other types of symbols in the code, keeping the codebase in sync and avoiding errors that may occur due to renaming inconsistencies.

#### Example Scenario

Imagine there is a variable `count` in a file called `index.js`, and you want to rename it to `total`. This action should apply not only to the variable declaration but also everywhere where the variable `count` has been used.

#### Request Structure

The request for `textDocument/linkedEditingRange` includes the text document identifier and the position of the character where the rename operation started.

**Request:**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "textDocument/linkedEditingRange",
  "params": {
    "textDocument": {
      "uri": "file:///path/to/index.js"
    },
    "position": {
      "line": 24,
      "character": 8
    }
  }
}
```

In this request:
- `uri` specifies the location of the file.
- `position` specifies where the character attempting to be renamed is located.

#### Response Structure

The response includes a list of ranges where the symbol trying to be renamed appears.

**Response:**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "ranges": [
      {
        "start": {
          "line": 24,
          "character": 6
        },
        "end": {
          "line": 24,
          "character": 11
        }
      },
      {
        "start": {
          "line": 25,
          "character": 9
        },
        "end": {
          "line": 25,
          "character": 14
        }
      }
    ],
    "wordPattern": "\\bcount\\b"
  }
}
```

In this response:
- `ranges` specifies the start and end positions in the text document where 'count' occurs.
- `wordPattern` is the regular expression that matches the symbol trying to be renamed.

### Summary

The `textDocument/linkedEditingRange` request of LSP is a valuable tool for developers during the refactoring of code. It identifies all appearances of a given symbol in the text document, allowing developers to rename all instances of the symbol simultaneously.