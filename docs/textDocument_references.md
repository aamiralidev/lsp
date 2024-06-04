### Text Document / References

The `textDocument/references` request in the Language Server Protocol (LSP) is used to find all references to a specific location within a piece of code. These references might be functions, variables, modules, or any construct within the code that may be referred to elsewhere.

#### Purpose

The `textDocument/references` command allows developers to find all points in the codebase where a particular element, such as a variable or method, is referred. This feature is often used for code navigation, renaming, and when doing impact analysis to understand the significance of changing a specific part of the code.

#### Example Scenario

Suppose you have a variable named `discountRate` defined in the file `checkout.js`, and you want to find all the places where `discountRate` is used or referenced.

#### Request Structure

The request for `textDocument/references` generally contains an `id`, `method` name, and `params` which include the text document's location and position of the variable within the document.

**Request:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "textDocument/references",
  "params": {
    "textDocument": {
      "uri": "file:///path/to/checkout.js"
    },
    "position": {
      "line": 22,
      "character": 10
    },
    "context": {
      "includeDeclaration": true
    }
  }
}
```

In this request:
- `uri` specifies the location of `checkout.js`.
- `position` is where `discountRate` is defined within the file.
- `includeDeclaration` when set to true, the search includes the declaration of the element; when false, it skips this.

#### Response Structure

The response consists of an array of `Location` objects each having a URI and a range pointing to the reference position.

**Response:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": [
    {
      "uri": "file:///path/to/checkout.js",
      "range": {
        "start": {
          "line": 30,
          "character": 10
        },
        "end": {
          "line": 30,
          "character": 22
        }
      }
    },
    {
      "uri": "file:///path/to/payments.js",
      "range": {
        "start": {
          "line": 45,
          "character": 15
        },
        "end": {
          "line": 45,
          "character": 27
        }
      }
    }
  ]
}
```

In this response:
- `uri` is the file containing a reference to `discountRate`.
- `range` describes where `discountRate` is referenced within the file.

### Summary

The `textDocument/references` request in LSP is fundamental for code navigation, code impact analysis, and refactoring. It helps developers find all the usages of a particular code element across the codebase.