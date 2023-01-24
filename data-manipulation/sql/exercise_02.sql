-- Crie uma consulta que mostre todos os nomes dos professores do curso de CST Sistemas para Internet,
-- no ano de 2018,
-- e os nomes das disciplinas pelas quais são responsáveis.

use exercicio_selects;
show tables;

select t2.prof_nome,
       t3.disc_nome,
       t3.curso_nome
from exercicio_selects.professor_disciplina as t1
inner join exercicio_selects.professor as t2
on (t1.prof_numero = t2.prof_numero)
inner join exercicio_selects.disciplina as t3
on (t1.disc_codigo = t3.disc_codigo)
where t1.ano = 2018 and t3.curso_nome = 'CST Sistemas para Internet';
