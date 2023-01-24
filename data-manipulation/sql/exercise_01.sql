-- Crie uma consulta com todas as disciplinas oferecidas no ano de 2018,
-- constando os nomes das disciplinas,
-- nomes e cidades dos professores responsáveis e nomes dos cursos das disciplinas.

use exercicio_selects;
show tables;

select t1.ano,
	   t2.prof_nome,
	   t2.prof_cidade,
       t3.disc_nome,
       t3.curso_nome
from exercicio_selects.professor_disciplina as t1
inner join exercicio_selects.professor as t2
on (t1.prof_numero = t2.prof_numero)
inner join exercicio_selects.disciplina as t3
on (t1.disc_codigo = t3.disc_codigo)
where t1.ano = 2018;
