# Pink River Dolphin Simulation

**Disciplina**: FGA0210 - PARADIGMAS DE PROGRAMAÇÃO - T01 <br>

**Nro do Grupo**: 05<br>

**Paradigma**: Sistema Multiagentes<br>

<img src="https://user-images.githubusercontent.com/72623771/214444939-651a794f-e3fa-4f79-96e8-5e21fa6f34cb.png" min-width="350px" max-width="350px" width="350px" align="right" alt="Botinhos">

## Alunos

| Matrícula | Aluno |
| -- | -- |
| 19/0142421  | Artur Vinicius Dias Nunes |
| 19/0085291  | Caio César Oliveira |
| 18/0123203 | João Pedro Alves da Silva Chaves |
| 18/0123459  | João Vitor de Souza Durso |
| 19/0128712  | Leticia Assunção Aires Moreira |
| 19/0111836  | Luan Vasco Cavalcante |
| 19/0044390  | Victor Rayan Adriano Ferreira |
| 19/0011602  | Christian Fleury Alencar Siqueira |

## Sobre 

O presente projeto foi desenvolvido durante a disciplina de Paradigmas de Programação do curso de Engenharia de Software da Universidade de Brasília com o intuito de aplicar conhecimentos adquiridos no módulo de Sistema Multiagentes.<br> <br>

Nesse sentido, seguindo a temática de animais em risco de extinção aplicada nas duas últimas entregas, decidimos desenvolver um sistema que simule as rotas migratórias do Boto Cor de Rosa, tendo como base determinadas complicações por nós estabelecidas, como a qualidade da água, a disponibilidade de comida e a presença de pescadores.

## Screenshots

### Tela inicial 
<p>
<img width = "600" height "600" src ="https://user-images.githubusercontent.com/72623771/215625577-790d3ac7-8f95-41ef-9499-1fa243229573.png"
</p>


### Executando simulação
<p>
<img width = "600" height "600" src ="assets/executando.gif"
</p>

### Simulação em funcionamento
<p>
<img width = "600" height "600" src ="assets/em_andamento.gif"
</p>

### Configurações adicionais
<p>
<img width = "600" height "600" src ="assets/adicionais.png"
</p>

Como visto acima, você pode aumentar ou diminuir:
* A população de boto
* A população de cardumes
* A quantidade de poluentes
* Frames por segundo

## Instalação 
**Linguagens**: Python<br>
**Tecnologias**: Framework MESA<br>

### Pré-Requisitos

* Python 3
* Framework MESA
* Jupyter
* Matplotlib
* Numpy

### Instruções

1- Instalar [Python](https://www.python.org/);<br>
2- Instalar o Framework [MESA](https://mesa.readthedocs.io/en/latest/) e suas dependências, conforme [tutorial](https://mesa.readthedocs.io/en/latest/tutorials/intro_tutorial.html); <br>
````
pip install mesa
````
3- Clonar o presente repositório; <br>
````
git clone https://github.com/UnBParadigmas2022-2/2022.2_G5_SMA_Pink_River_Dolphin_Simulation.git
````
4- Usar o seguinte comando dentro do repositório:

````
python main.py
````
### E pronto, você já pode visualizar a simulação! <br>
![](https://github.com/UnBParadigmas2022-2/2022.2_G5_SMA_Pink_River_Dolphin_Simulation/blob/main/assets/pink-dolphin.gif)

## Participações

|Nome do Membro | Contribuição | Significância da Contribuição para o Projeto (Excelente/Boa/Regular/Ruim/Nula) |
| -- | -- | -- |
| Artur Vinicius Dias Nunes  | Adição da função de reprodução dos botos | Excelente |
| Caio César Oliveira | Contribuição no agente boto cor de rosa (Pink Dolphin), nas funções de caçar e comer o cardume. Além disso na função de caçar o boto no pescador e a função de pescar o boto em si | Excelente |
| João Pedro Alves da Silva Chaves | Adição da função que faz com que o boto fuja da água poluída e apoio na implementação dos agentes "pescador" e "água" |  Excelente |
| João Vitor de Souza Durso | Movimentação dos botos, do agente água, de pescar o boto e da reprodução dos botos.  | Excelente |
| Leticia Assunção Aires Moreira | Contribuição no agente boto cor de rosa (Pink Dolphin) em conjunto com o Caio. Implementação da função de movimentação do pescador, bem como a função de comer cardume e outras funcionalidades. Construção do README. | Excelente  |
| Luan Vasco Cavalcante | Movimentação dos botos. Implementação do agente água. Criação do Agente Poluente. Criação da função boto come cardume. | Excelente |
| Victor Rayan Adriano Ferreira | Slider de quantidade de cardumes iniciais, fugir da água com qualidade baixa, GUI. | Excelente |
| Christian Fleury Alencar Siqueira | Adição da função que faz com qu eo cardume morra ao ser cercado por poluição. | Excelente |

## Outros 
### Lições Aprendidas
|Nome do Membro | Lições Aprendidas | 
| -------- | -- | 
| Artur Vinicius Dias Nunes |  |  
| Caio César Oliveira | Além de aprender um pouco sobre a estrutura de modelagem baseada em agente Mesa, também aprendemos um pouco mais sobre orientação a objetos e trabalho em equipe.  |  
| João Pedro Alves da Silva Chaves | Aprendi a utilizar o Mesa, consegui entender o funcionamento e organização dos agentes e seus comportamento e tudo isso de forma prática. | 
| João Vitor de Souza Durso  | Eu já conhecia os sistemas multiagentes, pois havia feito a matéria de IA no semestre passado. No entanto, o assunto foi abordado de maneira mais prática e, assim, pude aprender melhor sobre o framework MESA e melhorar minhas habilidades em Python. |  
|Leticia Assunção Aires Moreira  | Por meio da construção do projeto, foi possível aprender a respeito do sistema multiagentes mais na prática, já que a teoria me parecia um pouco distante e complexa. Além disso, pude praticar um pouco o python, já que utilizamos o MESA, o que facilitou bastante a implementação do jogo. | 
| Luan Vasco Cavalcante  |  |
| Victor Rayan Adriano Ferreira  | Simular interações complexas entre vários agentes, Comunicação eficiente entre os agentes, conhecer biblioteca em python que facilita muito o desenvolvimento de sistemas multiagentes. | 
| Christian Fleury Alencar Siqueira | Eu não conhecia o paradigma de Sistemas multiagentes, então foi tudo novo para mim. Aprendi os principais coneitos e fundamentos do paradigma, algumas aplicações interessantes mostradas na disciplina, e no geral, mesmo que eu não desenvolva outros Sistemas multiagentes, todo o conhecimento adquirido serve de bagagem para diferentes áreas da programação. |  

### Percepções
|Nome do Membro | Percepções | 
| -------- | -- | 
| Artur Vinicius Dias Nunes |  |  
| Caio César Oliveira | Paradigma é diferente do que estava acostumado a mexer, muito curioso como os objetos se conectam e interessante a capacidade de conseguir replicar situações da vida real em nível lógico, de forma simplificada claro. |  
| João Pedro Alves da Silva Chaves | Paradigma interessante, porém desafiador. A necessidade de pensar em como uma pequena mudança no comportamento afeta os outros agentes é algo complexo/ | 
| João Vitor de Souza Durso  | Paradigma muito interessante, pois as aplicações são infinitas. Podemos explorar contextos distintos e programar sistemas que se comportem muito próximos da realidade. Podemos antecipar possíveis problemas! |  
|Leticia Assunção Aires Moreira  | Senti que a curva de aprendizado do paradigma foi um pouco mais lenta que dos outros e pude perceber como a mudança em 1 agente influencia o comportamento dos outros agentes, de modo que os ajustes precisam ser sistêmicos. | 
| Luan Vasco Cavalcante  |  |
| Victor Rayan Adriano Ferreira  | O MESA é uma ferramenta muito boa para o desenvolvimento de sistemas multiagentes, e trabalhar com ele nos ensinou lições importantes sobre modelagem, comunicação e análise de resultados. | 
| Christian Fleury Alencar Siqueira | Aprendi muito com as aulas no JADE, e mesmo usando o MESA para o trabalho, pelo tempo de entrega, achei o JADE muito legal. Foi meu paradigma preferido do semestre, porém ao mesmo tempo o que tive menos tempo para me dedicar. Gostaria muito de ver uma ascensão de sistemas multiagentes no mundo da programação, pois é incrível. |  

### Fragilidades
|Nome do Membro | Fragilidades | 
| -------- | -- | 
| Artur Vinicius Dias Nunes |  |  
| Caio César Oliveira | Por algum motivo que o grupo não descobriu algumas vezes o pescador foca no lixo e não sai de perto dele. |  
| João Pedro Alves da Silva Chaves | Em alguns casos os cardumes não estão se afastando dá água poluída. | 
| João Vitor de Souza Durso  | É muito dificíl debugar comportamentos inesperados do código. Você programa os agentes individualmente pensando que os agentes irão se comportar de tal maneira, mas quando você coloca tudo para se conectar, você percebe diversas reações que não imaginou. |  
|Leticia Assunção Aires Moreira  | As funções desenvolvidas devem levar em consideração todos os outros agentes que podem ser impactados. Um exemplo disso é que, após implementar a busca do pescador pelos botos, ele passa a se manter próximo do lixo. Contudo, antes de tal funcionalidade, o pescador se movimentava normalmente.  | 
| Luan Vasco Cavalcante  |  |
| Victor Rayan Adriano Ferreira  | Poderíamos ter feito uma pesquisa maior sobre golfinhos e migrações para deixar nosso trabalho mais aproximado de situações da vida real. | 
| Christian Fleury Alencar Siqueira | Como principal fragilidade tive o tempo da entrega, que apesar de não ter sido curto, por conflitar com trabalhos finais de outras disciplinas, acabou ficando bem pesado. Também tive dificuldade de utilizar o MESA, que apesar de bem simplifciado, é bem diferente do JADE que vemos nas aulas, e então apenas os conceitos são aproveitados, mas a programção em si tem que ser aprendida do zero. |  

### Trabalhos Futuros
|Nome do Membro | Trabalhos Futuros | 
| -------- | -- | 
| Artur Vinicius Dias Nunes |  |  
| Caio César Oliveira | Não sei se seria possível, mas utilizar os cenários gerados para os agentes irem aprendendo comportamentos por meio de machine learning. Dessa forma, qunato mais cenários fossem executados, melhor seriam os comportamentos dos agentes. |  
| João Pedro Alves da Silva Chaves | Seria interessante adicionar outras espécies como agentes. | 
| João Vitor de Souza Durso  | É possível melhorar o efeito dos poluentes, dando movimento a eles, tendo em vista que o rio se move, levando consigo os dejetos. Dessa forma, ficaria mais próximo da realidade. |  
|Leticia Assunção Aires Moreira  | Uma possível melhoria é a redução da dispersão do esgoto. | 
| Luan Vasco Cavalcante  |  |
| Victor Rayan Adriano Ferreira  | Implementar modelos de agentes mais avançados, exemplo incluir modelos como inteligência artificial, aprendizado por reforço para simular comportamentos mais complexos. | 
| Christian Fleury Alencar Siqueira | Quando o cardume morre por ser cerdado por poluição, seria interessante, na função takeDown, que o cardume avisasse os outros cardumes de onde morreu para que os outros pudessem evitar aquela área. É claro que isso daria poderes de telecinese para os cardumes, mas a dinâmica desses agentes ficaria muito interessante. |  

## Vídeo
[Apresentação](https://youtu.be/R-hHrqT8FRg)

## Referências

> KAZIL, Jackie; MASAD, David; ANDREW, Crooks. Utilizing Python for Agent-Based Modeling: The Mesa Framework. Cham: Springer International Publishing, 2020. Disponível em: https://mesa.readthedocs.io/en/stable/. Acesso em: 20 jan. 2023.

> Session 9A Lecture : Agent Based Simulation using MESA. Disponível em: https://www.youtube.com/watch?v=VeQkhfDYyMc. Acesso em: 20 jan. 2023.

> Grimm, Volker, Eloy Revilla, Uta Berger, Florian Jeltsch, Wolf M. Mooij, Steven F. Railsback, Hans-Hermann Thulke, Jacob Weiner, Thorsten Wiegand, and Donald L. DeAngelis. 2005. “Pattern-Oriented Modeling of Agent Based Complex Systems: Lessons from Ecology.” American Association for the Advancement of Science 310 (5750): 987–91. doi:10.1126/science.1116681.

> Hunt, Andrew, and David Thomas. 2010. The Pragmatic Programmer: From Journeyman to Master. Reading, Massachusetts: Addison-Wesley.

> Leek, Jeffrey T., and Roger D. Peng. 2015. “Reproducible Research Can Still Be Wrong: Adopting a Prevention Approach.” Proceedings of the National Academy of Sciences 112 (6): 1645–46. doi:10.1073/pnas.1421412111.
