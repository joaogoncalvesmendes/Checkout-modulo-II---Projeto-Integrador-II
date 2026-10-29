Aplicação Web de Agendamento de Reforço Escolar – AAFARE
**Projeto Integrador II – Tecnologia da Informação (UFMS Digital)**
**Autor:** João Gonçalves Mendes | **Tutora:** Maria Marta de Souza Roque

---

Sobre o Projeto
Esta aplicação web foi desenvolvida para automatizar o agendamento de aulas de reforço escolar gratuitas para as crianças e adolescentes atendidos pela Associação de Apoio à Família e à Criança (AAFARE) em Campo Grande - MS.

Tecnologias Utilizadas
- **Framework:** React 18 / Next.js 14 (App Router)
- **Linguagem:** JavaScript (ES6+)
- **Estilização:** Tailwind CSS (Mobile-First e Acessível)
- **Acessibilidade:** Padrões eMAG e WCAG 2.1 AA

Pré-requisitos e Instalação
- **Node.js:** Versão 18.0.0 ou superior
- **npm** ou **yarn**

Passo a Passo para Execução Local:
1. Clonar o Repositório:
git clone https://github.com/joaogoncalvesmendes/Checkout-modulo-II---Projeto-Integrador-II.git
cd Checkout-modulo-II---Projeto-Integrador-II

2. Instalar Dependências:
npm install

3. Executar o Servidor de Desenvolvimento:
npm run dev

4. Acessar a aplicação no navegador em: http://localhost:3000

Estrutura do Projeto
src/
  app/              # Rotas e páginas do Next.js
  components/       # Componentes React (AgendamentoReforco.jsx)
  styles/           # Estilos globais Tailwind
public/               # Imagens institucionais da AAFARE
package.json          # Dependências
README.md             # Documentação oficial
