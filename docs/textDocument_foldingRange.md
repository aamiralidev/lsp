### `textDocument/foldingRange` Command in LSP

The `textDocument/foldingRange` request in the Language Server Protocol (LSP) is used to retrieve folding ranges in a given text document. This feature allows developers to collapse (or fold) and expand (or unfold) sections of source code in order to improve readability and easier navigation.

#### Purpose

The `textDocument/foldingRange` command aids developers by allowing them to condense sections of code that they're not currently focusing on, making it easier to navigate the document. This is particularly useful for large files with hundreds or thousands of lines of code.

#### Example Scenario

Imagine you have a file named `main.js` which has hundreds of lines of code. You are currently working on a specific function and you want to collapse all other functions to reduce distractions and improve focus.

#### Request Structure

The request for `textDocument/foldingRange` typically includes the text document identifier.

**Request:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "textDocument/foldingRange",
  "params": {
    "textDocument": {
      "uri": "file:///path/to/main.js"
    }
  }
}
```

In this request:
- `uri` specifies the location of the file.

#### Response Structure

The response will include a list of `FoldingRange` objects, each representing a foldable range in the text document.

**Response:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": [
    {
      "startLine": 2,
      "startCharacter": 2,
      "endLine": 5,
      "endCharacter": 4,
      "kind": "comment"
    },
    {
      "startLine": 7,
      "startCharacter": 4,
      "endLine": 18,
      "endCharacter": 1,
      "kind": "region"
    }
  ]
}
```

In this response:
- `startLine` and `endLine` are the starting and ending line numbers of the folding section.
- `startCharacter` and `endCharacter` are the character positions of the starting and ending lines, respectively.
- `kind` specifies the kind of folding range (comments, regions, imports, etc.).

### Summary

The `textDocument/foldingRange` request in LSP is a valuable tool for developers to reduce clutter and improve the readability of their code. By enabling the folding of code, they can concentrate on the code section that matters most to them at any given time.