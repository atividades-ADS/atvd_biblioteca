1.2-
a. Não. Foi foi utilizado o modelForm que já faz o form herdar as validações. O mesmo ocorre no admin.

b. O validator não consegue alterar o valor do input e consegue ser reutilizado. O clean consegue alterar o valor e não pode ser reutilizado.
Um exemplo em que apenas um clean pode ser utilizado é quando a validação de um campo depende de outro. Confirmar senha, por exemplo, depende do campo senha. O clean consegue fazer essa conexão; o validator, não.

c. i-clean(). Pois para validar um campo é necessário o valor de outro
ii-clean_<campo>(). Pois é necessário mudar o valor do input (remover os espaços)
iii-validator=[...]. Pois é uma validação simples que com validators do próprio django já pode ser assegurada (MaxValueValidator)
iv-clean(). Pois para validar um campo é necessário o valor de outro.


2.2-

a. Sem o request.FILES os arquivos acabam não sendo enviados. Não ocorre erros.
Sem o enctype="multipart/form-data" apenas o nome do arquivo é enviado, não o caminho.
Reproduzi os erros e o formulário não avisa nada em nenhum. Apenas as imagens não são exibidas.

b. O STATICFILES_DIRS / {% static %} serve para os arquivos estáticos do projeto. MEDIA_ROOT / .url serve para os arquivos de media que são guardados de formulários, então não são estáticos. Na biblioteca os arquivs de capa de livro devem ser armazenados no MEDIA_ROOT / .url, já um eventual css ou js deveria estar em STATICFILES_DIRS / {% static %}.

c. Pois o excluir só exlcui o caminho que estava armazenado no banco de dados, não o arquivo que foi guardado no projeto. Isso pode causar problema de ocupação de espaço ou de nomes iguais em arquivos diferentes.

d. pois a extensão pode ser forjada, então o ideal é realmente checar o tipo de arquivo.
Além de proteção sobre o tipo é importante limite de tamanho.


3.3-

a. O dispatch() da CBV olha o método HTTP e chama get() ou post(). No post(), o FormMixin testa form.is_valid() e, se inválido, chama form_invalid(), que re-renderiza o mesmo template com o form e seus erros (status 200, nada é salvo).

b. Pois o CreateView já possui o request.FILES embutido.

c. Porque o POST é o método que autoriza alteração de estado. Se a exclusão fosse por GET, prefetch de navegadores, crawlers e um simples <img src="..."> de outro site (CSRF) apagariam dados sem o usuário confirmar.

d. Vantagem: reaproveitamento de comportamento comum (form, redirect, 404, paginação, mixins), com menos código repetido. Desvantagem: fluxo implícito e espalhado entre mixins/MRO, mais difícil de ler e depurar. Escolheria FBVs para quando o mais importante são views simples/únicas ou quando a legibilidade pesa mais.

