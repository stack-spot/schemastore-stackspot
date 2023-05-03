Guia Markdown

O Markdown é uma forma simples de formatar textos e tem uma aparência limpa em qualquer dispositivo. Ele não possui por padrão, qualquer formatação específica como tamanho, cor ou tipo de fonte.

As estruturas do seu texto são construídas por símbolos, confira a baixo a utilização de cada um.

Observações importantes:

1. É possível usar tags HTML e suas propriedades como linguagem de marcação, mas o seu uso não é recomendado em documentos por poluir a legibilidade do Markdown.

2. Para facilitar a edição do seu texto em Markdown, utilize um editor de texto como o Visual Studio Code e plugins para pré-visualização do Markdown.
___

Texto itálico: *Italic* ou _Italic_

Texto negrito: **Bold** ou __bold__

Cabeçalhos no Markdown possuem o total de 6 leveis:

H1:
# Heading level 1

ou

Heading 1
=========

H2:
## Heading level 2

ou 

Heading 2
---------

H3:
### Heading level 3

H4:
#### Heading level 4

H5:
##### Heading level 5

H6:  
###### Heading level 6

Link Web: [Texto do Link](https://linkaqui.com)

ou

[Texto do Link aqui][1]

[1]: https://linkaqui.com

Link para Imagens:

1- ![Texto da imagem](https://commonmark.org/help/images/favicon.png) 
2- ![Texto da imagem](/path/folder/image.png)

Ou

1- ![Texto da imagem][2]

[2]: https://commonmark.org/help/images/favicon.png

2- ![Texto da imagem][3]

[3]: /path/folder/image.png

Bloco de citação:

> Texto em bloco de citação

> Multiplas
> Linhas
> No bloco de citação

Listas não ordenadas:

- item 1
- item 2
- item 3

Ou 

* item 1
* item 2
* item 3


Listas numeradas:

1. Item 1
2. Item 2
3. Item 3

Ou

1) Item 1
2) Item 2
3) Item 3

Linha Horizontal:

---

Ou 

***

Código em linha:

`trechco de código` em linha.

Blocos de código:

```
# bloco de código
key: value
print some code
```
