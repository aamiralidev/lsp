### `completionItem/resolve` Command in LSP

The `completionItem/resolve` request in the Language Server Protocol (LSP) is used to process a completion item that was previously unresolved by the `textDocument/completion` command. The purpose of this command is to provide additional details about a completion item that might be more expensive to compute, so are deferred until needed.

#### Purpose

The `completionItem/resolve` command helps in improving the performance of the language server by deferring expensive computations until necessary. This is especially valuable for large code bases where providing full completion items immediately can be resource-intensive.

#### Example Scenario

Imagine you have a code snippet, and you request code completion options. Initial options might not contain all details due to their computational cost. If you select an option, the `completionItem/resolve` command can fill in the additional details.

#### Request Structure

The request for `completionItem/resolve` typically includes the completion item that needs to be resolved.

**Request:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "completionItem/resolve",
  "params": {
    "label": "Console",
    "kind": 5,
    "detail": "Console class",
    "preselect": false,
    "sortText": "0000Console"
  }
}
```

In this request:
- `label` specifies the label of the completion item.
- `kind` denotes the kind of completion item.
- `detail` includes a brief detail about the completion item.
- `preselect` specifies whether this completion item should be preselected.
- `sortText` is used to sort the completion items.

#### Response Structure

The response will include the resolved completion item with additional details.

**Response:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "label": "Console",
    "kind": 5,
    "detail": "Console class",
    "documentation": "Represents the standard input, output, and error streams for console applications. This class cannot be inherited.",
    "preselect": false,
    "sortText": "0000Console"
  }
}
```

In this response:
- All initial properties are returned.
- `documentation` includes the more detailed description about the completion item.

### Summary

The `completionItem/resolve` request in LSP is a valuable tool for improving the performance of the language server by deferring the computation of more detailed information about a completion item until needed.