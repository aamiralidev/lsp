### Workspace / Will Create Files

The `workspace/willCreateFiles` request is part of the Language Server Protocol (LSP) that is used during the creation of new files. This request is fired before the actual creation of files, allowing the server to provide edits that will get executed on the client side before the files are actually created.

#### Purpose

The `workspace/willCreateFiles` command allows the server to handle necessary operations or clean-ups before the client creates or opens files. This might include, for example, modifying the content of a file being created based on the file type or providing necessary templates for the type of file being created.

#### Example Scenario

Imagine you're developing in a language that needs a specific template or pre-set codes for every new file created. In such cases, the `workspace/willCreateFiles` request can be used to automatically add those codes when a new file is created.

#### Request Structure

The request for `workspace/willCreateFiles` typically includes an array of files (with URIs) to be created.

**Request:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "workspace/willCreateFiles",
  "params": {
    "files": [
      {
        "uri": "file:///path/to/newFile.js"
      },
      {
        "uri": "file:///path/to/anotherNewFile.xml"
      }
    ]
  }
}
```

In this request:
- `uri` specifies the location and the name of the file that will be created.

#### Response Structure

The response will include a list of `TextDocumentEdit` or `CreateFile` operations that should be applied to the workspace before the files are actually created.

**Response:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "documentChanges": [
      {
        "textDocument": {
          "uri": "file:///path/to/newFile.js",
          "version": 1
        },
        "edits": [
          {
            "range": {
              "start": {
                "line": 0,
                "character": 0
              },
              "end": {
                "line": 0,
                "character": 0
              }
            },
            "newText": "'use strict';\n"
          }
        ]
      }
    ]
  }
}
```

In this response:
- `uri` specifies the location of the file where the edits will happen.
- `range` specifies where the `newText` will be inserted in the file.
- `newText` contains the text/code that will be inserted.

### Summary

The `workspace/willCreateFiles` request in LSP allows the server to prepare the client workspace before the client creates or opens files. This facilitates automatic generation or insertion of code based on file requirements, enhancing developer productivity.