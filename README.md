# Schemas Store StackSpot

Collection of JSON schema definition of Stackspot's contents


## Strucuture

We working with schema version at Stackspot. The directories is in line with this format:

`kind -> type -> version`


The kinds available are:

| kind        |types|  
|-------------|:------------|
| plugin      | app, infra  |



## How  to use

1. Install [RedHat's plugin](https://github.com/redhat-developer/vscode-yaml#associating-a-schema-to-a-glob-pattern-via-yamlschemas) to YAML reding on VSCode
2. Create a yaml file and referece on top of the file the json schema you will use: 
`# yaml-language-server: $schema=https://github.com/stack-spot/schemastore-stackspot/tree/main/plugin/infra/v1`