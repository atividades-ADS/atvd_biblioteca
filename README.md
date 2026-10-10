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