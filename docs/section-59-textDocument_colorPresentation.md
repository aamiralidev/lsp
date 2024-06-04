# Text Document / Color Presentation

The `textDocument/colorPresentation` request in the Language Server Protocol (LSP) is used to obtain a list of different ways a color can be represented in the source code.

## Purpose

The `textDocument/colorPresentation` command is commonly used in integrated development environments (IDE) or text editors to provide color picker features. This command helps developers to select and represent a color in different formats (for example, RGB, HSL, or hexadecimal) as per the programming language or file format.

## Example Scenario

Suppose a developer is editing a CSS file with a color attribute in RGB format. If the developer wishes to change the color, they might use a color picker tool that shows the same color in hex format.

## Request Structure

The request for `textDocument/colorPresentation` includes the text document identifier, the color information, and the range in the document where the color exists.

**Request:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "textDocument/colorPresentation",
  "params": {
    "textDocument": {
      "uri": "file:///path/to/style.css"
    },
    "color": {
      "red": 0.6,
      "green": 0.8,
      "blue": 0.1,
      "alpha": 1.0
    },
    "range": {
      "start": {
        "line": 20,
        "character": 7
      },
      "end": {
        "line": 20,
        "character": 23
      }
    }
  }
}
```

In this request:
- `uri` points to the location of the file.
- `color` is the RGB and alpha information of the color that needs to be presented.
- `range` defines the region in the document where the color is used.

## Response Structure

The response will contain a list of possible presentations for the given color.

**Response:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": [
    {
      "label": "rgb(153, 204, 26)",
      "textEdit": {
        "range": {
          "start": {
            "line": 20,
            "character": 7
          },
          "end": {
            "line": 20,
            "character": 23
          }
        },
        "newText": "rgb(153, 204, 26)"
      }
    },
    {
      "label": "#99CC1A",
      "textEdit": {
        "range": {
          "start": {
            "line": 20,
            "character": 7
          },
          "end": {
            "line": 20,
            "character": 23
          }
        },
        "newText": "#99CC1A"
      }
    }
  ]
}
```

In this response:
- `label` is the string representation of the color in a specific format.
- `textEdit` specifies where and how to replace the original color representation with the new format.

## Summary

In summary, the `textDocument/colorPresentation` request in the LSP provides a way for developers to interactively change color representations in their codebase. This standardizes how colors are represented across different languages and file formats, enhancing the uniformity and readability of the code.