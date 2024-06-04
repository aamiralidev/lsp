### Type Hierarchy / Subtypes

The `typeHierarchy/subtypes` request in the Language Server Protocol (LSP) is used to retrieve all the subtypes of a given type. This is part of the Type Hierarchy feature, allowing developers to understand the inheritance relationship of classes in object-oriented programming.

#### Purpose

The `typeHierarchy/subtypes` command helps developers identify all the classes that extend a particular superclass. This assists in code navigation, debugging, and understanding polymorphism, inheritance and encapsulation in the code.

#### Example Scenario

Let's consider a software project in Java, featuring a class called `Vehicle`. You desire to identify all classes that extend `Vehicle`.

#### Request Structure

The request for `typeHierarchy/subtypes` primarily includes the text document identifier and the position within the document where the type is defined.

**Request:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "typeHierarchy/subtypes",
  "params": {
    "textDocument": {
      "uri": "file:///path/to/Vehicle.java"
    },
    "position": {
      "line": 10,
      "character": 4
    }
  }
}
```

In this request:
- `uri` specifies the location of the file.
- `position` pinpoints the position in the document where the `Vehicle` class is defined.

#### Response Structure

The response will feature a list of type hierarchy items, each representing a subtype of the type requested.

**Response:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": [
    {
      "item": {
        "uri": "file:///path/to/Car.java",
        "range": {
          "start": {
            "line": 5,
            "character": 0
          },
          "end": {
            "line": 15,
            "character": 1
          }
        },
        "name": "Car",
        "kind": 5, 
        "detail": "public class Car extends Vehicle"
      }
    },
    {
      "item": {
        "uri": "file:///path/to/Truck.java",
        "range": {
          "start": {
            "line": 6,
            "character": 0
          },
          "end": {
            "line": 16,
            "character": 1
          }
        },
        "name": "Truck",
        "kind": 5, 
        "detail": "public class Truck extends Vehicle"
      }
    }
  ]
}
```

In this response:
- `uri` discloses the file where the subclass (subtype) is located.
- `range` defines the range in the document where the subclass is declared.
- `name` is the name of the subclass.
- `kind` is the kind of symbol (in this case, a class).

### Summary

The `typeHierarchy/subtypes` request in LSP is a valuable tool for developers to trace and understand the subtypes (inheritance hierarchy) of a particular type (class). It assists in understanding the relationship between classes, enabling more effective navigation through the codebase.