### Call Hierarchy / Outgoing Calls

The `callHierarchy/outgoingCalls` request in the Language Server Protocol (LSP) is used to retrieve all outgoing calls from a given function or method. This is part of the Call Hierarchy feature, which allows developers to understand where a particular function or method is calling other parts of the codebase.

#### Purpose

The `callHierarchy/outgoingCalls` command helps developers to pinpoint all the locations or functions/methods which a specific function is calling. It can assist in tracking code flow and understanding dependencies amongst functions/methods, thus facilitating code navigation and debugging process.

#### Example Scenario

Let's assume you have a method named `processOrder` in a file called `orders.js` and you want to identify all the functions that this method calls.

#### Request Structure

The request for `callHierarchy/outgoingCalls` just like in `incomingCalls`, includes the text document identifier and the position where the function/method is defined in that document.

**Request:**

```json
{
  "jsonrpc": "2.0",
  "id": 5,
  "method": "callHierarchy/outgoingCalls",
  "params": {
    "item": {
      "uri": "file:///path/to/orders.js",
      "range": {
        "start": {
          "line": 15,
          "character": 8
        },
        "end": {
          "line": 15,
          "character": 20
        }
      },
      "name": "processOrder",
      "kind": 12,
      "detail": "void processOrder()",
      "data": {}
    }
  }
}
```

In this request:
- `uri` specifies the location of the file.
- `range` specifies the range in the document where the method `processOrder` is defined.
- `name` is the name of the method.
- `kind` indicates the symbol kind (in this case, a method).

#### Response Structure

The response consists of a list of call hierarchy items, each of which represents a call from the specified function or method and gives detailed information of the calls made.

**Response:**

```json
{
  "jsonrpc": "2.0",
  "id": 5,
  "result": [
    {
      "to": {
        "uri": "file:///path/to/inventory.js",
        "range": {
          "start": {
            "line": 30,
            "character": 12
          },
          "end": {
            "line": 30,
            "character": 24
          }
        },
        "name": "checkStock",
        "kind": 12,
        "detail": "void checkStock()"
      },
      "fromRanges": [
        {
          "start": {
            "line": 16,
            "character": 6
          },
          "end": {
            "line": 16,
            "character": 18
          }
        }
      ]
    },
    {
      "to": {
        "uri": "file:///path/to/payment.js",
        "range": {
          "start": {
            "line": 47,
            "character": 6
          },
          "end": {
            "line": 47,
            "character": 20
          }
        },
        "name": "processPayment",
        "kind": 12,
        "detail": "void processPayment()"
      },
      "fromRanges": [
        {
          "start": {
            "line": 20,
            "character": 10
          },
          "end": {
            "line": 20,
            "character": 24
          }
        }
      ]
    }
  ]
}
```

In this response:
- `to` specifies the details of the function or method being called.
- `uri` indicates the file where the function or method resides.
- `range` specifies the range in the document where the called function/method is defined.
- `fromRanges` provides the specific locations within the calling function where the target function(s) are invoked.

### Summary

The `callHierarchy/outgoingCalls` request in LSP is an important feature for developers as it helps trace the code flow by identifying where certain function/method is calling other parts of the codebase. This enhances code navigation, debugging, and overall understanding of the code structure.
