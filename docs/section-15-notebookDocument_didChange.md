# Notebook Document / Did Change

The `notebookDocument/didChange` event is a part of the Notebooks feature in the Language Server Protocol (LSP). It is generated when changes are made to a notebook, such as creating, deleting or reordering cells.

## Purpose

The `notebookDocument/didChange` event is used to notify the server about any changes made to the notebook document. It's useful for keeping track of modifications in real time, maintaining the document's state in the server to provide relevant analysis, diagnostics, and other language features.

## Example Scenario

Consider a Jupyter notebook `analysis.ipynb`. A user adds a new cell and types in a Python command. The `notebookDocument/didChange` event will be raised to notify the language server about this new cell.

## Request Structure

As an event, `notebookDocument/didChange` does not require a specific request from the client. However, it sends notification data containing the document URI and the array of content changes made.

**Notification:**

```json
{
  "method": "workspace/didChangeTextDocument",
  "params": {
    "textDocument": {
      "uri": "file:///path/to/analysis.ipynb"
    },
    "contentChanges": [
      {
        "range": {
          "start": {
            "line": 20,
            "character": 0
          },
          "end": {
            "line": 20,
            "character": 0
          }
        },
        "text": "print('Hello, World!')"
      }
    ]
  }
}
```

In this notification:
- `uri` specifies the location and name of the file.
- `contentChanges` is an array of changes. Each entry specifies the range of the change and the new text.

## Response Structure

As an event, `notebookDocument/didChange` does not elicit a direct response. However, the server may respond to this event by providing diagnostics or code completions based on the changes.

## Summary

The `notebookDocument/didChange` event in LSP is useful for notifying the server about changes made in a notebook document. The server can then use this information to provide relevant language features such as diagnostics, code analysis, and more. It plays a significant role in maintaining real-time interactivity and responsiveness in notebook environments.