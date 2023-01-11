## Example

```yaml
schema-version: v1 #required #warning
kind: plugin #required
metadata: #required
  name: lambda-new-endpoint #required
  display-name: Endpoint para Lambda  #optional
  description: Add new endpoint to an existing Lambda API.  #required
  version: 1.0.0  #required
  picture: plugin.png  #optional
spec: #required
  type: app   #required
  compatibility: #optional
    - python
  about: docs/about.md  #optional #warning
  usage: docs/usage.md  #optional #warning
  implementation: docs/implementation.md  #optional #warning
  requirements: docs/requirements.md 	 #optional  #warning
  repository: https://github.com/stack-spot/stackspot-python-plugin  #optional
  release-notes: docs/release-notes-{{version}}.md #required
  technologies: #optional 
    - Api
  requires: #optional
    plugin: #optional
      - stackspot/mind/lambda-api@1.0.0
    connection-interface: #optional #warning
      - lambda-conn
    cli-only:true  #optional default false
  inputs: #optional
    - label: Type name of your resource #required
      name: resource #required
      type: text #required 
      required: true #optional #defautl false
      default: Client #optional
      pattern: '([A-Z][a-z]+)+' #optional
      help: 'Inform your resource name (e.g.: Client)' #optional
    - label: Choose http method of new endpoint
      name: method
      type: select
      items:
        - GET
        - POST
        - PUT
        - DELETE
        - PATCH
      default: GET
      required: true
      help: 'Inform the method of the endpoint (e.g.: post or delete)'
  computed-inputs: #optional
    method_sanitized: '{{ method | lower }}'
  env-inputs: #optional
      - label: Connection Pool #required
        name: connection-pool #required’
 ```

## Fields description

To understand about **schema-version**, **kind** and **metadata** fields, see [ADR Schema Definition](../../ADR_SCHEMA_DEFINITION.md)


 **spec:** A structure that contains specification about the domain, i.e. things that are specific of the domain. The precise structure of the spec depends on the schema-version and kind combination. It's a **required** information.



### spec fields

| field           |requirement|  
|-------------    |:----------|
| type            | required  |
| compatibility   | optional  | 
| about           | optional  | 
| usage           | required  |
| implementation  | optional  | 
| requirements    | optional  | 
| repository      | optional  | 
| release-notes   | optional  | 
| technologies    | optional  | 
| requires        | optional  | 
| inputs          | optional  | 
| computed-inputs | optional  |
| env-inputs      | optional  | 
