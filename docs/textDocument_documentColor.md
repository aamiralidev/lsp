# Text Document / Document Color

The `textDocument/documentColor` request in the Language Server Protocol (LSP) is used to retrieve all color information found in a given text document. This can be particularly useful in web or app development where colors are codified in either RGB, HEX, or other color systems.

## Purpose

The `textDocument/documentColor` command helps developers to quickly identify all color codes used in a stylesheet or in an application code, making it easier to manage and standardize the color theme.

## Example Scenario

Suppose you have a CSS stylesheet file with several color codes scattered throughout the document. Using the `textDocument/documentColor` request, you can fetch all the color instances and their positions in the document.

## Request Structure

The request for `textDocument/documentColor` includes the text document identifier.

**Request:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "textDocument/documentColor",
  "params": {
    "textDocument": {
      "uri": "file:///path/to/style.css"
    }
  }
}
```

In this request:
- `uri` specifies the location of the file.

## Response Structure

The response will include an array of color information items, each containing a range and the color's actual RGBA values.

**Response:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": [
    {
      "range": {
        "start": {
          "line": 10,
          "character": 15
        },
        "end": {
          "line": 10,
          "character": 24
        }
      },
      "color": {
        "red": 1,
        "green": 0,
        "blue": 0,
        "alpha": 1
      }
    },
    {
      "range": {
        "start": {
          "line": 20,
          "character": 15
        },
        "end": {
          "line": 20,
          "character": 24
        }
      },
      "color": {
        "red": 0,
        "green": 0,
        "blue": 1,
        "alpha": 1
      }
    }
  ]
}
```

In this response:
- `range` specifies the range in the document where the color code is defined.
- `color` describes the RGBA values for the color.

## Summary

The `textDocument/documentColor` request in LSP makes it easy for developers to fetch all the color information defined in a text document. It can be a useful tool for managing and maintaining color consistency in web or app development projects.