# Inlay Hint / Resolve

The `inlayHint/resolve` request in the Language Server Protocol (LSP) is a function used to gather further details about a specific inlay hint. This is part of the Inlay Hints feature which provides inline contextual details that help developers understand the code better.

## Purpose

The `inlayHint/resolve` command is used when developers require more detailed context for a specific inlay hint. This hint can deal with variable types, function parameters, and other code-related concepts.

## Example Scenario

Suppose there is a complex type within a JavaScript file named `analytics.js`. The specifics of this type are currently unclear within your code. The `inlayHint/resolve` command can be used to provide more context for this type, making it easier to understand.

## Request Structure

The request for `inlayHint/resolve` typically includes an InlayHint object, which can be simply a hint identifier.

**Request:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "inlayHint/resolve",
  "params": {
    "hintId": "inh-123"
  }
}
```

In this request:
- `hintId` is an identification for the inlay hint for which additional information is required.

## Response Structure

The response would include the fully resolved InlayHint object with all details filled in.

**Response:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "hintId": "inh-123",
    "kind": "Type",
    "position": {
      "line": 24,
      "character": 12
    },
    "label": "Array<string>"
  }
}
```

In this response:
- `hintId` is the identifier for the resolved inlay hint.
- `kind` refers to the kind of hint, in this scenario, it's a type hint.
- `position` indicates the location in the document where the hint applies.
- `label` provides the details of the hint. In this case, it indicates that the type is an array of strings.

## Summary

The `inlayHint/resolve` request in LSP is a feature that provides developers with more detail about specific inlays. These details make the code easier to understand, which can help with debugging or maintaining the code in the long term.
