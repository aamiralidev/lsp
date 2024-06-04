### Text Document / Completion

The `textDocument/completion` request in the Language Server Protocol (LSP) is used to retrieve completion items at a given position in a text document. Completion items are suggestions provided directly by language servers for autocompletion.

#### Purpose

The `textDocument/completion` command aids developers with code completion, making coding faster and less prone to typos and other common errors. It serves as a suggestion mechanism for developers when coding in various languages.

#### Example Scenario

Imagine you are coding in a JavaScript file called `app.js` and you started typing `cons`. The `textDocument/completion` request can help you by suggesting `console`, `const`, `constructor` and settings related to them as possible completions.

#### Request Structure

The request for `textDocument/completion` includes the text document identifier and the position within the document where autocompletion suggestions are required.

**Request:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "textDocument/completion",
  "params": {
    "textDocument": {
      "uri": "file:///path/to/app.js"
    },
    "position": {
      "line": 1,
      "character": 4
    }
  }
}
```

In this request:
- `uri` identifies the file in which autocompletion suggestions are required.
- `position` specifies the location in the document where the suggestions are required.

#### Response Structure

The response will include a list of completion items, each with details such as label, kind, detail, insert text etc.

**Response:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": [
    {
      "label": "console",
      "kind": 5,
      "detail": "console",
      "documentation": "The Console object provides access to the browser's debugging console.",
      "insertText": "console",
      "insertTextFormat": 1
    },
    {
      "label": "const",
      "kind": 15,
      "detail": "const",
      "documentation": "The const statement creates a read-only reference to a value.",
      "insertText": "const ",
      "insertTextFormat": 1
    },
    {
      "label": "constructor",
      "kind": 21,
      "detail": "constructor",
      "documentation": "The constructor method is a special method for creating and initializing an object.",
      "insertText": "constructor",
      "insertTextFormat": 1
    }
  ]
}
```

In this response:
- `label` gives the name of the suggested completion item.
- `kind` specifies the type of the completion item.
- `detail` provides additional details about the item.
- `documentation` gives a short documentation of the item.
- `insertText` specifies the actual syntax that gets inserted when this completion is chosen.
- `insertTextFormat` states format of the insert text.

### Summary

The `textDocument/completion` request in LSP is a crucial feature for fast and error-free coding. It provides autocompletion suggestions in real-time as the developer codes, thereby improving coding speed and reducing common errors.