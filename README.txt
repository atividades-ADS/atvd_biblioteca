1.2-
a. Não. Foi foi utilizado o modelForm que já faz o form herdar as validações. O mesmo ocorre no admin.

b. O validator não consegue alterar o valor do input e consegue ser reutilizado. O clean consegue alterar o valor e não pode ser reutilizado.
Um exemplo em que apenas um clean pode ser utilizado é quando a validação de um campo depende de outro. Confirmar senha, por exemplo, depende do campo senha. O clean consegue fazer essa conexão; o validator, não.

c. i-clean(). Pois para validar um campo é necessário o valor de outro
ii-clean_<campo>(). Pois é necessário mudar o valor do input (remover os espaços)
iii-validator=[...]. Pois é uma validação simples que com validators do próprio django já pode ser assegurada (MaxValueValidator)
iv-clean(). Pois para validar um campo é necessário o valor de outro.