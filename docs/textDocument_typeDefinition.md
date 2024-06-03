### `textDocument/typeDefinition` Command in LSP

The `textDocument/typeDefinition` request is a command used in the Language Server Protocol (LSP). The purpose of this command is to retrieve type definition for a given symbol in a specified position of a text document.

#### Purpose

The `textDocument/typeDefinition` command enables developers to navigate to the type definition of an object or a variable in their code base. This can be used for understanding the properties and methods that are related to the object or variable, and for refactoring purposes.

#### Example Scenario

Suppose you have a variable named `myEmployee` in a class `Employee` and you are uncertain of the variable type. You can use the `textDocument/typeDefinition` command to identify the type `Employee` and navigate to its definition.

#### Request Structure

The request for `textDocument/typeDefinition` usually includes the text document identifier and the position within the document where the symbol is located.

**Request:**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "textDocument/typeDefinition",
  "params": {
    "textDocument": {
      "uri": "file:///path/to/employee.js"
    },
    "position": {
      "line": 15,
      "character": 23
    }
  }
}
```

In this request:
- `uri` is the location of the file.
- `position` specifies the location within the document where the symbol `myEmployee` is located.

#### Response Structure

The response will include the location of the type definition for the symbol.

**Response:**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": [
    {
      "uri": "file:///path/to/employee.js",
      "range": {
        "start": {
          "line": 1,
          "character": 7
        },
        "end": {
          "line": 50,
          "character": 1
        }
      }
    }
  ]
}
```

In this response:
- `uri` indicates the location of the file containing the type definition.
- `range` specifies the range in the document where the type definition is found.

### Summary

The `textDocument/typeDefinition` request in LSP is a vital tool for developers to identify and navigate to the type definition of a particular symbol. This command assists in understanding the codebase and provides useful capabilities for code refactoring.