# Text Document / Did Open

The `textDocument/didOpen` command in the Language Server Protocol (LSP) is used when a client opens a document. This notification is sent to the language server from the client to signal that a new document is now managed by the client and the document's content is provided in the params of the request.

## Purpose

The `textDocument/didOpen` command informs the language server that a new text document was opened by the client. This allows the server to start providing language services for that document, such as syntax highlighting, code navigation, and error checking.

## Example Scenario

Imagine a developer opens a new source code file named `example.java` using an editor that uses LSP for language services. The editor (client) would use the `textDocument/didOpen` command to inform the language server about this newly opened file.

## Request Structure

The request for `textDocument/didOpen` typically includes the text document identifier, the language identifier, and the content of the document.

**Request:**

```json
{
  "jsonrpc": "2.0",
  "method": "textDocument/didOpen",
  "params": {
    "textDocument": {
      "uri": "file:///path/to/example.java",
      "languageId": "java",
      "version": 1,
      "text": "public class Example { ... }"
    }
  }
}
```

In this request:
- `uri` specifies the location of the file.
- `languageId` specifies the language of the text document.
- `version` is a version number of the document (clients increase the number each time they send a new version of the document).
- `text` is the content of the opened text document.

## Response Structure

Note that `textDocument/didOpen` is a notification, not a request, so there is no direct response. However, after the `textDocument/didOpen` notification is sent, the language server can start sending diagnostics information if it supports this feature.

```json
{
  "jsonrpc": "2.0",
  "method": "textDocument/publishDiagnostics",
  "params": {
    "uri": "file:///path/to/example.java",
    "diagnostics": [
       {
          "range": { 
              "start": { "line": 0, "character": 0 },
              "end": { "line": 0, "character": 1 }
          },
          "message": "Syntax error: unexpected symbol",
          "severity": 1
       }
    ]
  }
}
```

In this possible response:
- `uri` specifies the location of the file for which diagnostics information is provided.
- `diagnostics` is an array where each object represents a diagnostic (problem) in the document. It includes `range` specifying where in the document the problem is, `message` describing the problem, and `severity` indicating the severity of the problem.

## Summary

The `textDocument/didOpen` notification command in LSP informs the Language Server that a new document was opened by the Client and becomes managed by the Client. This allows the language server to provide relevant language services for that document.