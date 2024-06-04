### Text Document / Implementation

The `textDocument/implementation` request in the Language Server Protocol (LSP) is used to get the implementation location(s) of a symbol at a given text document position. This feature allows developers to navigate through a codebase by going directly from interface or abstract classes to their actual implementation.

#### Purpose

The `textDocument/implementation` command can serve multiple purposes such as assisting developers in navigating larger projects by providing an easy way to find all the actual implementations of interfaces, abstract classes or methods. 

#### Example Scenario

Assume you have an interface named `Payment` in the file `paymentInterface.java` and you have three classes that implement this interface: `CashPayment`, `CreditCardPayment`, `MobileWalletPayment`. You want to navigate to all the classes that implement `Payment`.

#### Request Structure

The request for `textDocument/implementation` generally includes the text document identifier and the position of symbol:

**Request:**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "textDocument/implementation",
  "params": {
    "textDocument": {
      "uri": "file:///path/to/paymentInterface.java"
    },
    "position": {
      "line": 16,
      "character": 6
    }
  }
}
```

In this request:
- `uri` specifies the location of the file.
- `position` specifies where the pointer is located inside the document (the interface `Payment`).

#### Response Structure

The response will include a list of locations of actual implementations:

**Response:**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": [
    {
      "uri": "file:///path/to/cashPayment.java",
      "range": {
        "start": {
          "line": 12,
          "character": 0
        },
        "end": {
          "line": 34,
          "character": 6
        }
      }
    },
    {
      "uri": "file:///path/to/creditCardPayment.java",
      "range": {
        "start": {
          "line": 8,
          "character": 0
        },
        "end": {
          "line": 45,
          "character": 5
        }
      }
    },
    {
      "uri": "file:///path/to/mobileWalletPayment.java",
      "range": {
        "start": {
          "line": 10,
          "character": 0
        },
        "end": {
          "line": 50,
          "character": 7
        }
      }
    }
  ]
}
```

In this response:
- `uri` specifies the file where the implementation classes are located.
- `range` denotes the range in the document where the class implementing the interface is defined.

### Summary

The `textDocument/implementation` request in LSP is a useful function for developers to navigate to the implementation details of interfaces or abstract methods in a code base. This helps in better understanding the code and making refactoring tasks more efficient.