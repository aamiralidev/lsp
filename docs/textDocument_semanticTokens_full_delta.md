### Text Document / Semantic Tokens / Full / Delta

The `textDocument/semanticTokens/full/delta` request in the Language Server Protocol (LSP) is used to retrieve semantic tokens for a text document in a delta format. Semantic tokens provide information about the semantic meaning of symbols in a text document. The delta format provides only the changes in semantic tokens from the last requested state, not the whole set.

#### Purpose

The `textDocument/semanticTokens/full/delta` command reduces the amount of data sent over the network by only returning the changes to semantic tokens since the last `full` request or `full/delta` request, this is useful in scenarios where only a minimal portion of the document has changed.

#### Example Scenario

Suppose your document represents a JavaScript file and you've just edited a small portion of it. Instead of sending the entire semantic token data for the entire document, the client can request delta semantic tokens related to the changed parts only.

#### Request Structure

The request for `textDocument/semanticTokens/full/delta` typically includes the text document identifier and the token Id received in the response of the last `full` or `full/delta` request.

**Request:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "textDocument/semanticTokens/full/delta",
  "params": {
    "textDocument": {
      "uri": "file:///path/to/script.js"
    },
    "previousResultId": "1"
  }
}
```

In this request:
- `uri` specifies the location of the text document.
- `previousResultId` is the token Id received in the latest `full` or `full/delta` request.

#### Response Structure

The response includes an identifier and either the delta semantic tokens or semantic tokens for the entire text document.

**Response:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "resultId": "2",
    "edits": [
      {
        "start": 5,
        "deleteCount": 3,
        "data": [2, 10, 1]
      }
    ]
  }
}
```

In this response:
- `resultId` is a unique identifier for the state of the semantic tokens at the time of the response.
- `edits` represents the delta semantic tokens. Each edit includes:
  - `start` - the index at which the changes in the tokens start.
  - `deleteCount` - the number of tokens to delete starting from the `start` index.
  - `data` - an array representing new tokens to insert starting at the `start` index.

### Summary

The `textDocument/semanticTokens/full/delta` request in LSP is an efficient way to obtain updates to semantic tokens in a text document when only a minimal part of the document has changed, reducing network traffic and enhancing performance for large files or slow networks.