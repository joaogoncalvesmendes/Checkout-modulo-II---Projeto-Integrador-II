
/* PortalReforco.css - Estilizacao Responsiva e Acessivel */
:root {
  --primary-color: #003366;    /* Azul Institucional */
  --secondary-color: #0066CC;  /* Azul Destaque */
  --bg-light: #F8F9FA;
  --text-dark: #212529;
}

/* Layout Base Mobile (Coluna Unica) */
.container {
  width: 100%;
  padding: 16px;
  background-color: var(--bg-light);
  font-family: Arial, sans-serif;
}

.search-section input {
  width: 100%;
  padding: 12px;
  font-size: 1rem;
  border: 2px solid var(--primary-color);
  border-radius: 6px;
  min-height: 48px; /* Area deitoque acessível */
}

.grid-aulas {
  display: flex;
  flex-direction: column;
  gap: 16px;
  margin-top: 20px;
}

.card-aula {
  background: #FFFFFF;
  border-left: 5px solid var(--secondary-color);
  padding: 16px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

/* Breakpoint Tablet (Grid 2 Colunas) */
@media (min-width: 768px) {
  .grid-aulas {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
  }
}

/* Breakpoint Desktop (Grid 3 Colunas) */
@media (min-width: 1024px) {
  .container {
    max-width: 1200px;
    margin: 0 auto;
  }
  .grid-aulas {
    grid-template-columns: repeat(3, 1fr);
  }
}


4. Código-Fonte do Componente Principal em React

// PortalReforcoAAFARE.jsx - Componente Dinamico de Reforco Escolar
import React, { useState } from 'react';
import './PortalReforco.css';

export default function PortalReforcoAAFARE() {
  const [filtro, setFiltro] = useState('');
  const [aulas] = useState([
    { id: 1, prof: 'Prof. Carlos Silva', area: 'Matematica', horario: 'Segunda 14:00', vagas: 3 },
    { id: 2, prof: 'Profa. Ana Oliveira', area: 'Portugues', horario: 'Quarta 09:00', vagas: 5 },
    { id: 3, prof: 'Prof. Joao Mendes', area: 'Historia', horario: 'Sexta 15:30', vagas: 2 }
  ]);

  const aulasFiltradas = aulas.filter(aula =>
    aula.area.toLowerCase().includes(filtro.toLowerCase()) ||
    aula.prof.toLowerCase().includes(filtro.toLowerCase())
  );

  return (
    <div className="container">
      <header className="app-header">
        <h1>Educação para Todos - AAFARE</h1>
        <p>Plataforma Comunitaria de Conexao com Professores Voluntarios</p>
      </header>

      <main className="main-content">
        <section className="search-section" aria-labelledby="titulo-busca">
          <h2 id="titulo-busca" className="sr-only">Buscar Aulas de Reforco</h2>
          <label htmlFor="campo-busca">Buscar por Disciplina ou Professor:</label>
          <input
            id="campo-busca"
            type="text"
            placeholder="Ex: Matematica, Portugues..."
            value={filtro}
            onChange={(e) => setFiltro(e.target.value)}
          />
        </section>

        <section className="grid-aulas" aria-live="polite">
          {aulasFiltradas.map(aula => (
            <article key={aula.id} className="card-aula">
              <h3>{aula.prof}</h3>
              <p><strong>Disciplina:</strong> {aula.area}</p>
              <p><strong>Horário:</strong> {aula.horario}</p>
              <p><strong>Vagas Disponíveis:</strong> {aula.vagas}</p>
              <button
                type="button"
                className="btn-agendar"
                aria-label={`Agendar aula de reforco em ${aula.area} com ${aula.prof}`}
                onClick={() => alert(`Solicitacao enviada para ${aula.prof}!`)}
              >
                Agendar Reforco
              </button>
            </article>
          ))}
        </section>
      </main>

      <footer className="app-footer">
        <p>&copy; 2025 AAFARE - Associacao de Amparo as Familias Renovacao | Jardim Moema - Campo Grande/MS</p>
      </footer>
    </div>
  );
}

