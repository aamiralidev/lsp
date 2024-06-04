# Type Hierarchy / Supertypes

The `typeHierarchy/supertypes` request in the Language Server Protocol (LSP) is used to retrieve the supertypes for a given class or interface. This feature is part of the Type Hierarchy, which helps developers understand the structure of object-oriented code.

## Purpose

The `typeHierarchy/supertypes` command aids developers in understanding the inheritance hierarchy of a specific class or interface. It returns all the classes or interfaces from which the specified one is derived or implements, helping in code navigation and understanding of code relationships.

## Example Scenario

Suppose you have a class named `Bike` in a file called `transport.js`. You want to find all the classes from which `Bike` extends or implements to better understand its capabilities and restrictions.

## Request Structure

The request for `typeHierarchy/supertypes` typically includes a TextDocumentIdentifier for the file and the position within the document where the class or interface is defined.

**Request:**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "typeHierarchy/supertypes",
  "params": {
    "textDocument": {
      "uri": "file:///path/to/transport.js"
    },
    "position": {
      "line": 5,
      "character": 8
    }
  }
}
```
In this request:
- `uri` specifies the location of the file.
- `position` specifies the position in the document where the class `Bike` is defined.

## Response Structure

The response will include a list of TypeHierarchyItems, each representing a superclass or interface implemented by the specified class or interface.

**Response:**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "result":  [
    {
      "uri": "file:///path/to/vehicle.js",
      "range": {
        "start": {
          "line": 10,
          "character": 6
        },
        "end": {
          "line": 15,
          "character": 1
        }
      },
      "name": "Vehicle",
      "kind": 7  // Class kind
    },
    {
      "uri": "file:///path/to/movable.js",
      "range": {
        "start": {
          "line": 0,
          "character": 6
        },
        "end": {
          "line": 4,
          "character": 1
        }
      },
      "name": "Movable",
      "kind": 8  // Interface kind
    }
  ]
}
```

In this response:
- `uri` specifies the file location of the superclass or interface.
- `range` specifies the range in the document where the superclass or interface is defined.
- `name` is the name of the superclass or interface.
- `kind` shows the kind of symbol (Class or Interface, in this case).

## Summary

The `typeHierarchy/supertypes` request in LSP is an essential tool for developers working with object-oriented programming languages. It helps them understand the inheritance structure of classes and the relationships among interfaces, providing a clearer view of the code architecture.
