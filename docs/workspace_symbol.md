### `workspace/symbol` Command in LSP

The `workspace/symbol` request in the Language Server Protocol (LSP) is used to search for all the symbols in the entire workspace. Symbols can include functions, classes, variables, or type definitions. This is particularly useful for navigation and moving around large code bases.

#### Purpose

The `workspace/symbol` command is designed to help developers find the location of specific symbols in their codebase. It helps to navigate to related sections of their project quickly. This command is particularly useful when working with larger projects where manual navigation between different code files would be time-consuming and inefficient.

#### Example Scenario

Suppose you are developing a large e-commerce application and you need to find all the instances of the symbol `Product` which could be a class, interface, or function scattered across multiple files in your project.

#### Request Structure

The `workspace/symbol` request includes a `query` parameter that allows you to specify the name of the symbol you are looking for.

**Request:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "workspace/symbol",
  "params": {
    "query": "Product"
  }
}
```

In this request:
- `query` is the name of the symbol that you need to find in the workspace.

#### Response Structure

The response to the `workspace/symbol` request is an array of `SymbolInformation` objects each of which represents a usage of the symbol you searched for.

**Response:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": [
    {
      "name": "Product",
      "kind": 6, // Class kind
      "location": {
        "uri": "file:///path/to/cart.js",
        "range": {
          "start": { "line": 8, "character": 4 },
          "end": { "line": 50, "character": 1 }
        }
      },
      "containerName": "Cart"
    },
    {
      "name": "Product",
      "kind": 6, // Class kind
      "location": {
        "uri": "file:///path/to/productCatalog.js",
        "range": {
          "start": { "line": 12, "character": 8 },
          "end": { "line": 48, "character": 1 }
        }
      },
      "containerName": "ProductCatalog"
    }
  ]
}
```

In this response:
- `name` is the name of the symbol.
- `kind` denotes the type of the symbol which is a class in this case.
- `location` contains information about where the symbol is located. `uri` indicates the file, and `range` indicates the start and end positions of the symbol in the file.
- `containerName` is the name of the container in which the symbol is found.

### Summary

The `workspace/symbol` request in LSP is a valuable feature for developers to quickly find and navigate to specific symbols within a large code base. It improves code navigation and understanding of the relationships between different components of a project.