import openai
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
openai.api_key = config['DEFAULT']['OPENAI_API_KEY']


# Define a function to call the OpenAI API
def get_chatgpt_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Use "gpt-4" to specify the model
        messages=[
            {"role": "system", "content": """
             You are an expert on LSP protocol. I'll ask you questions about a particular command in the protocol and you'll provide with an explanation of what it does with its purpose, an example scenario, request structure(what it includes), request(example json with post-explanation), response structure(what it includes), response(example json with explanation) and finally, you'll include a summary. Here is an example prompt and its possbile explanation
             prompt: call_hierarchy_incoming_calls
             explanation: 
             ### `call_hierarchy/incomingCalls` Command in LSP

The `call_hierarchy/incomingCalls` request in the Language Server Protocol (LSP) is used to retrieve incoming calls for a given function or method. This is part of the Call Hierarchy feature, which allows developers to understand where a particular function or method is called from within the codebase.

#### Purpose

The `call_hierarchy/incomingCalls` command helps developers identify all places in the code where a specific function or method is being called. This is particularly useful for code navigation, refactoring, and understanding dependencies within the code.

#### Example Scenario

Imagine you have a function named `calculateTotal` in a file called `billing.js`. You want to find all the places where `calculateTotal` is being called.

#### Request Structure

The request for `call_hierarchy/incomingCalls` typically includes the text document identifier and the position within the document where the function or method is defined.

**Request:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "callHierarchy/incomingCalls",
  "params": {
    "item": {
      "uri": "file:///path/to/billing.js",
      "range": {
        "start": {
          "line": 10,
          "character": 4
        },
        "end": {
          "line": 10,
          "character": 19
        }
      },
      "name": "calculateTotal",
      "kind": 12,  // Method kind
      "detail": "void calculateTotal()",
      "data": {}
    }
  }
}
```

In this request:
- `uri` specifies the location of the file.
- `range` specifies the range in the document where the function `calculateTotal` is defined.
- `name` is the name of the function.
- `kind` is the kind of symbol (in this case, a method).

#### Response Structure

The response will include a list of call hierarchy items, each representing a call to the specified function or method.

**Response:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": [
    {
      "from": {
        "uri": "file:///path/to/invoice.js",
        "range": {
          "start": {
            "line": 22,
            "character": 15
          },
          "end": {
            "line": 22,
            "character": 29
          }
        },
        "name": "generateInvoice",
        "kind": 12,
        "detail": "void generateInvoice()"
      },
      "fromRanges": [
        {
          "start": {
            "line": 22,
            "character": 20
          },
          "end": {
            "line": 22,
            "character": 34
          }
        }
      ]
    },
    {
      "from": {
        "uri": "file:///path/to/report.js",
        "range": {
          "start": {
            "line": 45,
            "character": 5
          },
          "end": {
            "line": 45,
            "character": 19
          }
        },
        "name": "generateReport",
        "kind": 12,
        "detail": "void generateReport()"
      },
      "fromRanges": [
        {
          "start": {
            "line": 45,
            "character": 10
          },
          "end": {
            "line": 45,
            "character": 24
          }
        }
      ]
    }
  ]
}
```

In this response:
- `from` specifies the details of the function or method making the call.
- `uri` indicates the file where the call originates.
- `range` specifies the range in the document where the calling function is defined.
- `fromRanges` indicates the specific locations within the calling function where the target function is called.

### Summary

The `call_hierarchy/incomingCalls` request in LSP is a powerful tool for developers to trace back where a particular function or method is being invoked. This aids in better code navigation and understanding of the codebase.
"""},
            {"role": "user", "content": prompt},
        ]
    )
    return response['choices'][0]['message']['content']

def format_heading(response):
  lines = response.split('\n')
  heading = lines[0]
  heading = heading.replace('command in LSP', ' ')
  import re
  pattern = r'`([^`]*)`'
  matches = re.findall(pattern, heading)
  heading = matches[0]
  heading = heading.replace('/', ' / ')
  heading = re.sub(r'(?<!^)(?=[A-Z])', ' ', heading).title()
  heading = '### ' + heading
  lines[0] = heading
  response = '\n'.join(lines)
  return response

def create_filename(protocol, index):
  protocol = protocol.replace('/', '_')
  filename = f'section-{str(index+2).zfill(2)}-{protocol}.md'
  return filename

def create_documentation_using_gpt4(input_file, output_folder):
  with open(input_file, 'r') as f:
      data = [line for line in f.read().split('\n')]

  documentation = {}
  for i, protocol in enumerate(data):
      prompt = protocol
      response = get_chatgpt_response(prompt)
      # Replace non-ASCII characters with a space
      response = ''.join(char if ord(char) < 128 else ' ' for char in response)
      response = format_heading(response)
      # converting h4 to h1
      response = response.replace('###', '#').replace('# Summary', '## Summary')
      filename = create_filename(protocol, i)
      documentation[filename] = response
      
  for protocol, description in documentation.items():
      with open(f'documentation/{protocol}', 'w') as f:
          f.write(description)

# create_documentation_using_gpt4('../lsp_protocol.txt', '../docs')
## NOTE: Index.md file was created manually