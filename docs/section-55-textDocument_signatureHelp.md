# Text Document / Signature Help

The `textDocument/signatureHelp` request in the Language Server Protocol (LSP) is used to retrieve the signature help for a given function or method call. This feature helps by providing real-time assistance to developers by showing function/method overloads, parameters, and documentation while they write code.

## Purpose

The `textDocument/signatureHelp` command aids developers by showing them the signature of the method or function they are calling. This can include details of the expected parameters, their types, and descriptions helping to prevent errors and enhancing the productivity during coding.

## Example Scenario

Suppose you're coding in a script and you're about to call a function called `findMax` which takes two parameters `a` and `b`. As you type `findMax(` in your code editor, it invokes the `textDocument/signatureHelp` request to provide information about the required parameters.

## Request Structure

The request for `textDocument/signatureHelp` typically includes the text document identifier and the position where the function or method is being called.

**Request:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "textDocument/signatureHelp",
  "params": {
    "textDocument": {
      "uri": "file:///path/to/script.js"
    },
    "position": {
      "line": 10,
      "character": 8
    }
  }
}
```

In this request:
- `uri` specifies the location of the file.
- `position` specifies the position in the document where `findMax(` has been written.

## Response Structure

The response will include a list of signatures and additional information about the invoked function.

**Response:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "signatures": [
      {
        "label": "findMax(a: number, b: number): number",
        "documentation": "Finds the maximum of two numbers",
        "parameters": [
          {
            "label": "a: number",
            "documentation": "First number"
          },
          {
            "label": "b: number",
            "documentation": "Second number"
          }
        ]
      }
    ],
    "activeSignature": 0,
    "activeParameter": 0
  }
}
```

In this response:
- `signatures` is a list of all possible signatures for the method or function.
- `activeSignature` is the index in the signatures array that the language server considers active.
- `activeParameter` is the index of the parameter within the active signature that the language server considers active.

## Summary

The `textDocument/signatureHelp` command in LSP provides a way to assist developers during code writing by showing function or method signatures. This command improves the efficiency and accuracy when writing code, especially for unfamiliar functions or methods.