# Text Document / Semantic Tokens / Range

The `textDocument/semanticTokens/range` request in the Language Server Protocol (LSP) is used to fetch semantic tokens for a given range. Semantic tokens are used to highlight the syntax of source code, where each token refers to a span of source code that has semantic meaning.

## Purpose

The `textDocument/semanticTokens/range` command facilitates the highlighting of programming syntax. This is especially useful for publishers and editors, converting plain code text into visually distinguishable parts, which have semantic meaning in the corresponding programming language.

## Example Scenario

Imagine you have a code editor, and you want to add syntax highlighting to the range [line: 5 character: 10, line: 20 character: 5] in a source code file.

## Request Structure

The request for `textDocument/semanticTokens/range` typically includes the text document identifier and the range within the document you wish to fetch semantic tokens for.

**Request:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "textDocument/semanticTokens/range",
  "params": {
    "textDocument": {
      "uri": "file:///path/to/myCode.js"
    },
    "range": {
      "start": {
        "line": 5,
        "character": 10
      },
      "end": {
        "line": 20,
        "character": 5
      }
    }
  }
}
```

In this request:
- `uri` specifies the location of the file.
- `range` specifies the range in the document for which you need the semantic tokens.

## Response Structure

The `textDocument/semanticTokens/range` response includes an array of integers which represent semantic tokens. Each semantic token is represented by five integers: deltaLine, deltaStart, length, tokenType, and tokenModifiers.

**Response:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "data": [
      0, 2, 5, 1, 0,  // A token in line 0, starting at character 2, of length 5, of type 1
      1, 1, 6, 2, 1,  // A token in line 1 (relative to the last token), starting at character 1 (relative), of length 6, of type 2, with modifier 1
      0, 1, 4, 3, 0   // Another token in line 1 (same line as above), starting +1 characters after, of length 4, of type 3
    ]
  }
}
```

In this response:
- `data` is an array of integers, with each group of five integers representing a semantic token.

## Summary

The `textDocument/semanticTokens/range` request in LSP supports publishers in displaying source code with correct syntax highlighting. The command fetches an array of semantic tokens for a specific range within a text document, and the response includes information such as the line, start position, length, token type, and token modifiers for each semantic token.