### Call Hierarchy / Incoming Calls

The `callHierarchy/incomingCalls` request is used in the Language Server Protocol (LSP) for obtaining incoming calls targeting a specific method or function. It is part of the call hierarchy functionality to enhance developers' understanding of the invocation of specific methods or functions across different locations in the source code.

#### Purpose

The `callHierarchy/incomingCalls` request can assist developers in pinpointing all parts of the source code where a particular method or function is invoked. It greatly helps in navigating the code, code refactoring, and understanding dependencies in the codebase.

#### Example Scenario

Assume that in your code there's a function called `computeSum` in a file named `mathOperations.js`, and you are trying to identify all instances in the code where `computeSum` is invoked.

#### Request Structure

The request for `callHierarchy/incomingCalls` usually contains the identifier of the text document and the position within the document where the targeted method or function resides.

**Request:**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "callHierarchy/incomingCalls",
  "params": {
    "item": {
      "uri": "file:///path/to/mathOperations.js",
      "range": {
        "start": {
          "line": 5,
          "character": 2
        },
        "end": {
          "line": 5,
          "character": 12
        }
      },
      "name": "computeSum",
      "kind": 12,  // Method kind
      "detail": "int computeSum()",
      "data": {}
    }
  }
}
```

Here, in this request, 
- `uri` denotes the file path.
- `range` specifies the position in the document where the function is defined.`computeSum`.
- `name` is the name of the function.
- `kind` represents the kind of symbol, here it's a method (specified by the number 12).

#### Response Structure

The response contains a list of call hierarchy items, each one of which represents an invocation of the targeted function or method.

**Response:**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": [
    {
      "from": {
        "uri": "file:///path/to/calculate.js",
        "range": {
          "start": {
            "line": 15,
            "character": 7
          },
          "end": {
            "line": 15,
            "character": 20
          }
        },
        "name": "calculate",
        "kind": 12,
        "detail": "void calculate()"
      },
      "fromRanges": [
        {
          "start": {
            "line": 15,
            "character": 10
          },
          "end": {
            "line": 15,
            "character": 23
          }
        }
      ]
    },
    {
      "from": {
        "uri": "file:///path/to/total.js",
        "range": {
          "start": {
            "line": 10,
            "character": 3
          },
          "end": {
            "line": 10,
            "character": 13
          }
        },
        "name": "total",
        "kind": 12,
        "detail": "int total()"
      },
      "fromRanges": [
        {
          "start": {
            "line": 10,
            "character": 7
          },
          "end": {
            "line": 10,
            "character": 17
          }
        }
      ]
    }
  ]
}
```

In this response,
- `from` contains information about the function or method that is making the call.
- `uri` specifies the file path from which the call is made.
- `range` defines the location in the document where the function that invokes the target function is found.
- `fromRanges` illustrates specific locations within the invoking function where the target function gets called.

### Summary

Overall, the `callHierarchy/incomingCalls` command helps developers trace the locations where a particular function or method is invoked, which can greatly assist in code navigation and understanding the overall structure of the project.