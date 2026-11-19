# Sobre deletar autores
Ao deletar um autor o livro deve ter sua coluna "author" trocada para NULL pois o livro não deixa de existir quando o autor é 
deletado, mantendo a obra e seu conteúdo.

# Sobre trocar autores para ManyToMany
Ordem das ações:
1. adicionar no model um campo authors_tmp
2. criar uma migração para isso com makemigratios
3. criar uma migração vazia a qual eu edito criando uma função que passa por todos os livros, pega os autores e adiciona no campo authors_tmp
4. rodar as migrações com migrate
5. remover o campo authors do model
6. gerar a migração com makemigrations e aplicar com migrate
7. trocar o nome de authors_tmp para authors
8. gerar a migração com makemigrations e aplicar com migrate

# Que dados se perdem quando a migração é revertida? Por quê?

Se houver uma reverção para uma migração antes de haver o campo ManyToMany os dados de autores simplesmente
seriam perdidos, pois ele apagaria a tabela intermediaria que une dois campos quando há uma relação
ManyToMany, perdendo os dados que estvam nessa tabela

# Com ManyToMany, o que acontece com um livro quando o seu único autor é apagado? Como garantir que todo livro tenha pelo menos um autor?

no momento, nada acontece, um livro pode existir sem um autor mas podemos adicionar uma restrição ao livro para que permaneça com pelo menos um autor,
impedindo que o autor seja apagado caso ele seja o unico autor de algum livro.



# O formulário está protegido contra requisições forjadas. Teste e anote no README o que acontece quando essa proteção é removida do template.

O {% csrf_token %} protege o formulário de requisições forjada, o django rejeita requisições feitas sem essa proteção, não permitindo que o methodo POST 
funcione sem essa proteção.

# Atividade Sábado Letivo 1 -  validators, upload e CBV
1.2 a) Sim, o LivroModelForm mudou seguindo as mudanças do form; funcionam pois eles são baseados no model, se o model muda eles mudam para corresponder a ele.

b) O metódo  clean pode alterar um campo, já os validators apenas validam, retornando erros caso a validação encontre algum erro no que tiver sido digitado no input. 
Uma validação de algum campo que precise ser unico é um exemplo de algo que o clean_(campo) pode fazer e o validators não, o validators não tem acesso a 
instancias daquele objeto, já o clean tem acesso ao self.instance podendo saber se é uma edição ou criação de novo objeto. alem disso o validator 
não é capaz de alterar o campo, o normalizando em alguma regra especifica

c) 
1. O título não pode ser igual ao nome do autor.

clean: pois precisa de validação entre campos e não em apenas um campo;

2. O título deve ser salvo sem espaços no início e no fim.

clean_(campo): pode alterar o campo para remover esses casos problematicos, normalizando o campo e fazendo ele funcionar corretamente;

3. O número de páginas deve ser no máximo 5000.

validators: apenas retorna uma aviso no caso de uma quebra das regras estabelecidas (mais de 5000 páginas)

4. Um livro "indisponível" precisa ter o ISBN preenchido.

clean: pois precisa de validação entre campos e não em apenas um campo;

2.2 a) Esquecer qualquer um dos dois faz com que o arquivo nunca chegue ao servidor.
sem request.FILES a view instancia o formulário apenas com request.POST, sem passar request.FILES.
O Django trata o campo de arquivo como se nada tivesse sido enviado. caso o campo seja obrigatorio deve
retornar algum erro, caso não simplesmente vai passar e não enviar nada em imagens;
Sem o enctypo o request.FILES fica vazio pois o formulário não é de um tipo que aceite arquivos

b) O STATICFILES_DIRS / {% static %} são arquivos estaticos que a pessoa desenvolvedora coloca no projeto e que são utilizados dentro da propria aplicação sem grandes 
mudanças, por exemplo uma logo que fica no header da pagina; já o MEDIA_ROOT / .url é para dados que provem do back, dados que podem mudar, no caso da nossa biblioteca seriam as capas dos livros, uma nova edição pode ter uma capa diferente e precisar de uma edição ou inserção de dados no DB.

c) O arquivo continua pois o django em sí não guardo o arquivo, ele guarda o caminho para o arquivo e usa um volume para guardar esses arquivos,
ao editar uma capa ou apagar o livro o caminho para o arquivo correspondente deixa de apontar para ele mas o arquivo em si permanece no volume, isso, 
a longo prazo, pode ocasionar um grande volume de dados orfãos consumindo espaço em disco.

d) A extensão do arquivo não basta pois o lado do cliente que escolhe o nome e extensão para um arquivo, podendo sem grandes dificuldades apenas renomear o arquivo e mudar a extensão. PAra resolver esse problema é interressante que o backend leia os primeiros bytes do arquivo para entender sua real natureza. Além disso, uma boa pratica é evitar que a pasta de media tenha alguma permissão execução, evitando que algum possivel script que passe tenha capacidade de fazer algo de lá; Existem outros cuidados a serem feitos como evitar a descompressão de dados em loops grandes, limitando a 1 ou 2 vezes caso o sistema precise aceitar arquivos compactados, se não precisar é bom evitar que o sistema faça alguma descompactação automatica para evitar bombas zip