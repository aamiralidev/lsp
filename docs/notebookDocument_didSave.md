# Notebook Document / Did Save

The `notebookDocument/didSave` notification in the Language Server Protocol (LSP) is used to alert the server whenever a notebook document is saved. Notebook documents typically consist of code and rich text content that can be executed in place, such as Jupyter Notebooks.

## Purpose

The `notebookDocument/didSave` command helps in keeping the language server informed about the state of the document. This ensures that recommendations and programming assistance provided by the language server are based on the latest version of the document.

## Example Scenario

Imagine you have a data science Jupyter notebook which contains Python code. You made some modifications and saved the notebook. 


## Request Structure

There is no request as this is a notification. However, the protocol data sent over when `notebookDocument/didSave` is triggered includes information about the saved document.

**Notification:**

```json
{
  "jsonrpc": "2.0",
  "method": "notebookDocument/didSave",
  "params": {
    "textDocument": {
      "uri": "file:///path/to/notebook.ipynb"
    },
    "version": 2
  }
}
```

In this notification:

- `uri` specifies the location of the saved notebook document.
- `version` is the version number of the document after it has been saved.


## Response Structure
There is no response structure, as this is a notification and not a request.

## Summary
The `notebookDocument/didSave` notification in LSP is used to inform the language server whenever a notebook document is saved. This ensures the language server is always working with the latest version of the document, allowing for accurate programming assistance.