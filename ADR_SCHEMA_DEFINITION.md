# Schema Definition

* **Status:** proposed
* **Deciders:** 
* **Date:** 2023-01-10

## Context and Problem Statement

We want to define the best strucuture to our yaml schemas. 


## Decision Driver

- We always have a kind
- Some information will not change, regardless of kind.
- Some information will be different according with the kind
- We have schema versioning by kind

## Decision Outcome

```yaml
schema-version: v1 #required
kind: Plugin #required
metadata:
  name: lambda-new-endpoint #required
  description: Add new endpoint to an existing Lambda API.  #required
  display-name: Endpoint para Lambda  #required
  version: 1.0.0  #required
  picture: plugin.png  #optional  
spec:
  type: app   #required for Plugin kind
  ...      
 ```

Fields description

 **schema-version:** schema-version is the version of specification format for that particular domain (kind) that the specification is made of . The version is used for being able to evolve the format and maintain backwards compatibility. It's a **required** information.
 
 **kind:** is the domain being described. To see available kinds access [schema-store](https://github.com/stack-spot/schemastore-stackspot). It's a **required** information.

 [attention!] The tuple of **schema-version** and **kind** indicates how to interpret the contents of the rest of the data.

 **metadada:** A structure that contains metadata about the domain, i.e. things that are common between domains specification. It's a **required** information.


| field       |requirement|  
|-------------|:----------|
| name        | required  |
| description | required  | 
| display-name| optional  | 
| version     | required  |
| picture     | optional  | 


 **spec:** A structure that contains specification about the domain, i.e. things that are specific of the domain. The precise structure of the spec depends on the schema-version and kind combination. It's a **required** information.
