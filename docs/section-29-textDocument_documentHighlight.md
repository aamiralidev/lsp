# Text Document / Document Highlight

The `textDocument/documentHighlight` command in the Language Server Protocol (LSP) is used to request highlights for all occurrences of a symbol within the same open text document.

## Purpose

This command facilitates developers while reading and understanding code by visually unifying all instances of a particular symbol within a text document. It is especially helpful when trying to identify the usage and impact of a variable, function, or other code symbol.

## Example Scenario

Consider a scenario where a developer is reviewing a large JavaScript file and came across a function called `processData()`. The developer wants to quickly identify all instances of this function within the current file to understand its usage and impact.

## Request Structure

The request for `textDocument/documentHighlight` includes the text document identifier and the position of the symbol in the document.

**Request:**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "textDocument/documentHighlight",
  "params": {
    "textDocument": {
      "uri": "file:///path/to/myFile.js"
    },
    "position": {
      "line": 13,
      "character": 7
    }
  }
}
```

In this request:
- `uri` specifies the location of the text file.
- `position` specifies the position in the document where the symbol `processData` is defined.

## Response Structure

The server responds with an array of 'DocumentHighlight' objects, each represents an occurrence of the symbol within the text document.

**Response:**

```json
{
  "jsonrpc": "2.0",
    "id": 2,
    "result": [
        {
            "range": {
                "start": {
                    "line": 13,
                    "character": 7
                },
                "end": {
                    "line": 13,
                    "character": 18
                }
            },
            "kind": 1
        },
        {
            "range": {
                "start": {
                    "line": 23,
                    "character": 15
                },
                "end": {
                    "line": 23,
                    "character": 26
                }
            },
            "kind": 2
        }
    ]
}
```

In this response:
- `range` specifies the range in the document where the symbol is being used.
- `kind` indicates the highlight kind (1 = Text, 2 = Read, 3 = Write). In our example, the function is being defined at the first location (line 13) and used at another (line 23).

## Summary

The `textDocument/documentHighlight` request in LSP locates and highlights all instances of a particular symbol within an open text document. It assists developers in quickly spotting all uses of a symbol, facilitating code reading and understanding.