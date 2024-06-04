### Code Action / Resolve

The `codeAction/resolve` request in Language Server Protocol (LSP) is used to obtain the full Information about a suggested `CodeAction`. This mainly comprises of computational expensive details like `edit`.

#### Purpose

The `codeAction/resolve` command is aimed to optimize the computing resource usage by avoiding unnecessary computation of detailed actions (like `edit`), which may not even be used by the client. This helps in keeping the list of suggested `CodeAction`s lightweight.

#### Example Scenario

An example scenario would be where an IDE identifies possible code refactorings or corrections within a piece of code. Initially, it just provides general information for the potential actions and when the user chooses a specific action, `codeAction/resolve` is called to compute and provide the extra details needed to apply the code action.

#### Request Structure

The request for `codeAction/resolve` includes the previously computed `CodeAction` which requires to add detailed information.

**Request:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "codeAction/resolve",
  "params": {
    "title": "Convert to anonymous function",
    "kind": "refactor.rewrite.function.anonymous",
    "diagnostics": [],
    "isPreferred": false
  }
}
```

In this request:
- `title` represents the title of the `CodeAction`.
- `kind` indicates the kind of the `CodeAction`.
- `diagnostics` shows the diagnostics to which this code action is applicable (if any).
- `isPreferred` indicates whether this is the preferred code action for its `kind`.

#### Response Structure

The response will be the resolved `CodeAction` with all the necessary details added, including computational expensive ones.

**Response:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "title": "Convert to anonymous function",
    "kind": "refactor.rewrite.function.anonymous",
    "edit": {
      "changes": {
        "file:///path/to/code.js": [
          {
            "range": {
              "start": {
                "line": 23,
                "character": 5
              },
              "end": {
                "line": 23,
                "character": 16
              }
            },
            "newText": "(function() { /* ... */ })"
          }
        ]
      }
    },
    "diagnostics": [],
    "isPreferred": false
  }
}
```

In this response:
- `title`, `kind`, `diagnostics`, and `isPreferred` are the same as in the request.
- `edit` represents the changes which need to be done as part of this `CodeAction`, including the file in which the change needs to be made and the new text that need to be inserted.

### Summary

The `codeAction/resolve` request in LSP is useful to compute and retrieve detailed information needed for a `CodeAction`, including potentially heavy computations. This can be particularly helpful in situations where the server wants to keep the initial list of code actions light and compute full details only when needed based on the user's choice.