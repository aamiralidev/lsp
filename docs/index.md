# Introduction

- Language Server Protocol governs the rules and associated structure required for communication between the Integrated Development Environment and the corresponding Language Server. 
- To be precise, the Language Server is just a specification of the request and response structure for communication between the Integrated Development Environment and the corresponding Language Server. 
- In this documentation, we present purpose of each request, json structure of the request and response. The IDE (usually VSCode) use the same protocol to communicate with the Language Server for syntax highlighting, code intellisence and other language features.